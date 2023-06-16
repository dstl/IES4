from pathlib import Path
from typing import Tuple
from pyshacl import validate
from rdflib import Graph, RDF, RDFS, SH, OWL, XSD
from rdflib.term import URIRef, BNode, Literal, Node
from itertools import chain

SH_CLASS = URIRef("http://www.w3.org/ns/shacl#class")


def _insert_list_item(sh_graph: Graph, ont_graph: Graph, item: Node, tgt_typ: URIRef) -> Node:
    bnode = BNode()
    rest = ont_graph.value(subject=item, predicate=RDF.rest)
    value = ont_graph.value(subject=item, predicate=RDF.first)
    sh_graph.add((item, RDF.first, bnode))
    sh_graph.add((bnode, tgt_typ, value))
    sh_graph.add((item, RDF.rest, rest))
    return rest


def _add_shape_triples_to_graph(ont_graph, sh_graph, property_type, prop, targets, shape_suffix):
    tgt_typ = SH_CLASS
    if shape_suffix == "DomainShape":
        tgt = SH.targetSubjectsOf
    else:
        tgt = SH.targetObjectsOf
        if property_type is OWL.DatatypeProperty:
            tgt_typ = SH.datatype

    for target in targets:
        sh_graph.add((URIRef(str(prop) + shape_suffix), RDF.type, SH.NodeShape), )
        sh_graph.add((URIRef(str(prop) + shape_suffix), tgt, prop))
        sh_graph.add((URIRef(str(prop) + shape_suffix), SH.severity, SH.Warning))
        if type(target) is BNode:
            item = ont_graph.value(subject=target, predicate=OWL.unionOf)
            if item:
                # add the shacl 'or' pointing to the list bnode
                sh_graph.add((URIRef(str(prop) + shape_suffix), URIRef("http://www.w3.org/ns/shacl#or"), item))
                # add triples for first item in the list
                rest = _insert_list_item(sh_graph, ont_graph, item, tgt_typ)
                # add triples for remaining list items
                while rest != RDF.nil:
                    item = rest
                    rest = _insert_list_item(sh_graph, ont_graph, item, tgt_typ)
        else:
            sh_graph.add((URIRef(str(prop) + shape_suffix), tgt_typ, target))


def _create_node_shapes_for_properties(ont_graph, sh_graph, property_type):
    for prop in ont_graph.subjects(predicate=RDF.type, object=property_type):
        # process domains
        targets = ont_graph.objects(subject=prop, predicate=RDFS.domain)
        shape_suffix = "DomainShape"
        _add_shape_triples_to_graph(ont_graph, sh_graph, property_type, prop, targets, shape_suffix)
        # process_ranges
        targets = ont_graph.objects(subject=prop, predicate=RDFS.range)
        shape_suffix = "RangeShape"
        _add_shape_triples_to_graph(ont_graph, sh_graph, property_type, prop, targets, shape_suffix)


def _create_node_shapes_for_classes(ont_graph: Graph, sh_graph: Graph) -> None:
    rdf_classes = ont_graph.subjects(predicate=RDF.type, object=RDFS.Class)
    owl_classes = ont_graph.subjects(predicate=RDF.type, object=OWL.Class)
    classes = chain(rdf_classes, owl_classes)

    for item in classes:
        if type(item) is not BNode:  # only create shapes for identified classes
            sh_graph.add((URIRef(str(item) + 'Shape'), RDF.type, SH.NodeShape))
            sh_graph.add((URIRef(str(item) + 'Shape'), SH.targetClass, item))
            sh_graph.add((URIRef(str(item) + 'Shape'), SH.severity, SH.Warning))
            superclasses = ont_graph.objects(subject=item, predicate=RDFS.subClassOf)
            for superclass in superclasses:
                if type(superclass) is BNode:  # i.e. it is a restriction
                    restriction = superclass
                    path = ont_graph.value(subject=restriction, predicate=OWL.onProperty)
                    cls = ont_graph.value(subject=restriction, predicate=OWL.onClass)
                    some = ont_graph.value(subject=restriction, predicate=OWL.someValuesFrom)
                    all_values = ont_graph.value(subject=restriction, predicate=OWL.allValuesFrom)
                    value = ont_graph.value(subject=restriction, predicate=OWL.hasValue)
                    minqc = ont_graph.value(subject=restriction, predicate=OWL.minQualifiedCardinality)
                    minc = ont_graph.value(subject=restriction, predicate=OWL.minCardinality)
                    maxqc = ont_graph.value(subject=restriction, predicate=OWL.maxQualifiedCardinality)
                    maxc = ont_graph.value(subject=restriction, predicate=OWL.maxCardinality)
                    qexact = ont_graph.value(subject=restriction, predicate=OWL.qualifiedCardinality)
                    exact = ont_graph.value(subject=restriction, predicate=OWL.cardinality)
                    property_shape = BNode()
                    if all_values:
                        list = BNode()
                        sh_graph.add((URIRef(str(item) + 'Shape'), SH.xone, list))
                        sh_graph.add((list, RDF.first, property_shape))
                        sh_graph.add((list, RDF.rest, RDF.nil))
                        sh_graph.add((property_shape, SH.path, path))
                        sh_graph.add((property_shape, SH_CLASS, all_values))
                    elif some:
                        sh_graph.add((URIRef(str(item) + 'Shape'), SH.property, property_shape))
                        sh_graph.add((property_shape, SH.path, path))
                        sh_graph.add((property_shape, SH.minCount, Literal(1, datatype=XSD.nonNegativeInteger)))
                        sh_graph.add((property_shape, SH_CLASS, some))
                    else:
                        sh_graph.add((URIRef(str(item) + 'Shape'), SH.property, property_shape))
                        if path: sh_graph.add((property_shape, SH.path, path))
                        if cls: sh_graph.add((property_shape, SH_CLASS, cls))
                        if value: sh_graph.add((property_shape, SH.hasValue, all_values))
                        if minc: sh_graph.add((property_shape, SH.minCount, minc))
                        if minqc: sh_graph.add((property_shape, SH.minCount, minqc))
                        if maxc: sh_graph.add((property_shape, SH.maxCount, maxc))
                        if maxqc: sh_graph.add((property_shape, SH.maxCount, maxqc))
                        if exact:
                            sh_graph.add((property_shape, SH.minCount, exact))
                            sh_graph.add((property_shape, SH.maxCount, exact))
                        if qexact:
                            sh_graph.add((property_shape, SH.minCount, qexact))
                            sh_graph.add((property_shape, SH.maxCount, qexact))


def process_n3_file(ontology: str | Path | Graph):
    if isinstance(ontology, (Path, str)):
        ont_graph = Graph().parse(ontology)
    else :
        ont_graph = ontology
    sh_graph = Graph()
    # bind namespaces from ontology to shape graph
    for name, ns in ont_graph.namespaces():
        sh_graph.bind(name, ns, replace=True)

    _create_node_shapes_for_classes(ont_graph, sh_graph)
    _create_node_shapes_for_properties(ont_graph, sh_graph, OWL.ObjectProperty)
    _create_node_shapes_for_properties(ont_graph, sh_graph, OWL.DatatypeProperty)

    # sh_graph.serialize(destination=Path("../IES Specification Docs/ont.file.ttl"), format="turtle")
    return ont_graph, sh_graph


def rdf_validate(data_file: str | Graph, ont_graph: str | Graph, sh_graph: str | Graph) -> Tuple[
    bool, Graph, str]:
    # run shacl validation
    conforms, results_graph, results_text = validate(data_file,
                                                     shacl_graph=sh_graph,
                                                     ont_graph=ont_graph,
                                                     inference='none',
                                                     abort_on_first=False,
                                                     allow_infos=False,
                                                     allow_warnings=False,
                                                     meta_shacl=False,
                                                     advanced=True,
                                                     js=False,
                                                     debug=False)

    return conforms, results_graph, results_text
