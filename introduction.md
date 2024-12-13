[back to readme](README.md)

# Introduction
## Background

Across the UK Government there are many separate knowledge stores, including multiple stores within each organisation; and this will remain the case for many years. Many of the knowledge stores contain similar information about the real world but, for numerous technical and business reasons, there is no standardised way of representing such content – this is usually because different terminologies, formats and/or schemas are used for each of these stores.

Analysts across the police, defence and national security community need comprehensive access to the information distributed across these many knowledge stores so that they can concentrate their efforts on analysis and exploitation tasks without having to broker between different internal formats and schemas. Being able to exchange and share information effectively and efficiently is therefore imperative and needs to be achieved without the need for collaborating organisations to:

* develop numerous and bespoke bilateral interchange mechanisms;
* make costly and highly disruptive changes to their individual knowledge stores.
The Information Exchange Standard (IES) was developed in order to enable that collaboration.

## Purpose of the IES
The purpose of the IES is to make information exchange easier by providing a common vocabulary for data/information exchanges between knowledge stores. Information from each store is converted to/from the common vocabulary when it travels. Users and systems no longer need to understand many different formats and schemas. Each system only has to understand the relation between its own internal model and that of the IES, dramatically reducing complexity.

## A note on the name of the standard
The Information Exchange Standard, as its name suggests and as described in the earlier sections of the Introduction above, was originally devised as a specification for exchange of data/information amongst organisations that need to collaborate to best achieve their individual mandates, but which is independent of the way that the data/information might be retained within each organisation.

This initial purpose gave rise to the name of the standard. However, this does not preclude IES from being used as a specification for wider purposes beyond that of data/information exchange; in fact, IES has already been used as a specification for the way that data/information is persisted in several organisation deployments.

It has been suggested that the name of the IES standard be changed to reflect its wider applicability. Whilst this has been considered, it has been decided that for the time being, and as the standard continues to mature and be promoted, a name change would not be helpful. This decision may be re-addressed at some point in the future.

**Important**: Whilst the IES may be used as a specification for data/information persistence the standard itself does not provide any end-point implementation of such.

## Approach
The selection of information types included in the IES is orientated towards those felt to be of greatest interest to a majority of working-level analysts across HMG. The IES recognises that it would be unrealistic to attempt to model the whole world. Nor does it cover highly specialised information types; these will be covered by specialist communities. There are three criteria for including an information type in the IES:
* at least one organisation wants to share the information;
* at least one organisation wants to receive it;
* someone is able and willing to define it.
It is also accepted that users will need to exchange information beyond the scope of any specific version of the standard. The IES achieves this by including agile extension mechanisms that do not necessitate a potentially time-consuming revision of the standard itself.

## Implementation
From v4.0.0, the IES is specified as an RDF Schema. RDF is a standard published by the World Wide Web Consortium (W3C) and is the preferred data exchange format in UK Government. One of the major benefits of using RDF is that the W3C has specified a number of standard data serialisations which have been widely implemented in commercial and open source tools. This means that the IES specification no longer needs to specify its own serialisations. This does mean that any IES compliant interface should be able to read any of the W3C RDF standard serialisation formats. Given the amount of open-source RDF software that can already do this, that should not be a barrier to entry.

## Constraints
As with previous versions of IES, the model is only loosely constrained. The model specifies domains and ranges for relationships (RDF properties) but they are purely indicative. Similarly, for Event Participations, IES does not formally constrain which Entities can participate in particular Events - rather it indicates which should be used. The goal is to allow any sending party to express the information they want whilst still providing a framework. Receiving parties should expect to receive such data. In future releases, it is anticipated that the model will become more constrained as users feed comments back and the IES adapts to different usage patterns.

## Extending the Model
As with the previous version of IES, version 4 allows the model to be extended within a particular data exchange file. Unlike the previous versions though, IES 4 uses the W3C's RDF Schema which allows new classes and properties to be defined in data payloads. When extending the IES, users should subtype from the most appropriate class, and also specialise properties from existing properties. This will aid understanding by the receiving party, which is likely to only know about the core IES classes.

[back to readme](README.md)
