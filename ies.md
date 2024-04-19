[back to readme](README.md)

### Crown Copyright 2020-2022
![Logo](Images/ies-logo.png)

# IES Model version: 4.2.0
## Contents
* Introduction Diagrams
    * [Notation](#{9BEA56CA-2E23-47b6-AF37-991F72D7C4DD})
    * [Model Change Log](#{F2B6CFA8-1B10-4cb8-AF0D-FFAF0A28C247})
    * [IES Overview](#{E169A2F5-85CB-41a7-A8B5-5BFAC5330AB5})
    * [Relationships](#{164BAFC4-0C40-4900-8A83-2B62248BF22D})
    * [Period of Time](#{AC49DE36-990B-4c27-BA39-7C78A474C589})
    * [Where and When](#{37882C3A-2915-4112-8EB2-ABB1C071165C})
    * [Start and End](#{926F5679-25C6-47a6-AAB0-65F3A7406B99})
    * [Event Linkages](#{0EBD3547-89A5-45c0-ACA6-BC125D0E885E})
    * [Event Participation](#{1EE6C0C5-B494-4395-9C59-AEDC7B7971D9})
    * [Sometimes](#{C8ABE75C-87AF-4b36-9D4A-456CF2657B39})
    * [Types](#{55486513-19EB-4a97-AADB-62317E9EA00F})
    * [Representation and Content](#{393BD76E-39F3-4bd0-9BBA-7E1AC7C63F0A})
    * [Identifiers](#{A72D9272-DF55-4e58-9174-3F9F168438A0})
    * [Characteristics and Measures](#{80403A46-2297-4e05-8C9C-1F6EF5596779})
    * [Disposition](#{C9919009-48A5-4db1-8123-90396A6F3AD0})
    * [Attributes](#{1A40117E-E6F6-4ae0-A438-8583E896BE00})
    * [Source References](#{60CD4A4C-652B-40c9-A65B-321A73329D6E})
    * [Payloads and Groups](#{17F25B76-6D6D-4d6e-8BC8-F97C1B2DCC0B})
    * [Metadata](#{C58F08D6-9661-4b21-8576-B7620B7D84E3})
* [Entities](#{1167BC44-F4AF-4485-88BD-DBA2C4B5293E})
    * [Amount of Money](#{E9EC7882-A905-4bc5-ACF7-6AC9C28E8596})
    * [Assets](#{DC826580-C2BF-482e-ABF2-B90684A4CB74})
    * [Communications Account](#{A4475333-349B-4d3a-81FA-B899DC1961D1})
    * [Communications Device](#{9E7698FD-A154-4fb7-8054-A04D67EB71F1})
    * [Communications Identifier](#{3B36B41F-8E34-4a09-8586-5A8DF2FC3574})
    * [Communications Identifier Range](#{1810A643-CCD5-474b-AF1B-CE748179B427})
    * [Data Object](#{1F0FFC2A-9636-4070-BF77-E7503E68B9E1})
    * [Document](#{7A96DA48-8EEF-46d2-9362-C506781AF268})
    * [Financial Account](#{29646663-65CC-41b5-A127-F8C3D6DD4FF5})
    * [Identity Document](#{563B8C72-68EA-439b-88AF-424BF75DAA54})
    * [Location](#{12F41073-A280-42a2-A83B-A299C85B78F4})
    * [Online](#{8BE1A4EF-AD1D-4e9f-8681-AB9C658DA4D6})
    * [Organisation](#{AD64CF62-6430-44f1-8943-DF7C22C31DFB})
    * [Posts and Roles](#{58BAB7ED-90B7-4ec5-82E5-02208AA0D521})
    * [PaymentArtefact](#{282BC043-9277-4814-B98F-DFE588356C73})
    * [Person](#{D2CDD899-3080-4887-897F-63EA08B5E949})
    * [Ticket](#{A98C6576-D0D5-42cf-AF90-89CC2B1F47F3})
    * [Vehicle](#{6D8B1DC4-4361-4edb-818F-AC96863555AD})
    * [All Entities](#{D97110D9-791E-4e88-A92B-5139286E5F05})
* [Events](#{8CE69414-E291-4f34-B5C5-443FED062F40})
    * [Events Dear Boy, Events](#{4C6AEF32-6360-4671-82E3-019DF67D2496})
    * [Assessment](#{5DF03A2C-F6DF-4433-82D5-7E5C14B6045C})
    * [Authorisation](#{DF5AAB67-46EB-40a8-B96E-8F3B5382D145})
    * [Observation](#{6D55C5E7-D9D9-454a-97C7-B682D9334D78})
    * [Agreement](#{C8EE24EF-889D-4e8f-96DE-CCBE47D4BE4F})
    * [Disagreement and War](#{6EEF4705-72CE-4979-90FF-1966940B7C35})
    * [Business](#{2C2171E3-E7A6-4702-AD72-1E02B11AFAA7})
    * [Attendance](#{6780105E-2091-491e-AEBF-C68E03B0074E})
    * [Communication](#{D25935BF-2B8F-4315-A858-1FC4DC691DF3})
    * [Lifecycle](#{8DB48415-57E7-47d8-A6EE-97AD59CCA8B9})
    * [OnlineEvent](#{70DAFAB2-F28A-4822-A211-00731AD90D62})
    * [Criminal](#{852CA74F-2858-4145-908D-5DCEB1AA0589})
    * [Law Enforcement](#{460B1D00-10CB-4f93-A518-F2A96AF54CF7})
    * [Operational](#{45F6DECC-1D67-4037-83DE-0047C8815EF5})
    * [Political](#{F919DBEC-CE53-478f-8EEA-FB151D7B1102})
    * [Trade](#{B84B31E9-62DD-4a6b-89F3-459896232F75})
    * [Movement](#{41F61D94-0E76-4f81-A005-AE93346DB054})
    * [Travel Booking](#{0641B013-5267-4314-84C8-1856EBA51A47})
    * [All Events](#{D488BDAE-AAEA-4c4a-B866-ED79D154D547})
* [Relationships](#{9ED67AE2-F907-4f58-A67F-921186EC23FB})
    * [Familial](#{C6937856-2424-4e96-BFE1-8CA3611869D1})
    * [Interest](#{59F513B8-3ECE-4bac-8BD0-908306396A8F})
    * [Lifecycle Relationships](#{9E3102FC-46DC-4363-B0B4-D0EA7275D05D})
    * [Mutual Understanding](#{9D1812FF-691F-4847-B79C-9136091D93E0})
    * [Operational Part 1](#{461D38A7-E51F-4e68-AB15-CA7B0E27B1F6})
    * [Operational Part 2](#{BAD148FB-D906-45c4-9A2C-D79819F47655})
    * [Professional](#{DC8F8219-960A-4207-B9AF-98B9486529A8})
    * [Social](#{E92F9ED3-BB84-4e2f-B9FB-5B787D917BD0})
    * [Structural](#{BED9B9A0-547E-49d5-AB9D-2BD0A634A3EA})
    * [Topological](#{20BF4E8F-9683-4bf4-B59C-F7F2AB2FB8F3})
    * [All Relationships](#{DE627D02-C0D9-462a-9CB7-1C496714A13D})
* [All Elements](#{5F2E9C9F-780E-4de3-8B3B-017023D6259C})
## <a id="{9BEA56CA-2E23-47b6-AF37-991F72D7C4DD}"></a>Notation
![Notation Diagram](Images/EAID_9BEA56CA_2E23_47b6_AF37_991F72D7C4DD.png)

### IES elements in this diagram:

* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [Arrest](#{D8D7184C-2F7B-4a5d-AA8F-7EE7B5A04F94})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [ArrestingOfficer](#{5B3F41C3-91CC-442f-A4F8-615E77751734})
* [Arrested](#{B870A3B5-32FA-4aaf-86F1-7DB674585F3A})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [isParticipationOf](#{DF9F6056-CCD4-41aa-9A86-536F6150EC25})
* [isParticipantIn](#{BAEA86D9-C90E-4f8d-96F5-A01BB0C49711})

The IES4 model has been developed using the OMG's ontology definition meta-model (ODM) profile for UML. Whilst UML may be somewhat foreign to ontology developers, ODM seemed a reasonable compromise for presenting the model to both data architects and ontologists. 

<b>Notes for data modellers:</b>
Basic background reading on how to use RDF is the book "Semantic Web for the Working Ontologist".
Otherwise, things to watch out for in the UML are:
<ul>
	<li>Relationship definitions and attributes (properties in RDF speak) are shown as boxes rather than lines.</li>
	<li>Multiple inheritance and multiple classification is not just possible, but encouraged in ontology modelling</li>
	<li>Properties (relationships and attributes) can be specialised using the rdfs:subPropertyOf relationship</li>
</ul>
<b>
</b><b>Notes for ontologists:</b>
<ul>
	<li>The model uses RDF Schema in preference to OWL wherever possible - this ontology is not intended for reasoning / inference</li>
	<li>It is a formal 4D ontology using the BORO approach...</li>
	<li>...In other words, the emphasis is on real-world semantic and precision of description rather than any compromises to enable reasoning.</li>
	<li>The ontology is higher order (classes of classes of classes...etc.), and extensional.</li>
	<li>The Sparx ODM template uses something called uriReferenceNode to refer to an external resource. There are a few of these in the ontology, used where it makes reference to RDFS or RDF class definitions.</li>
	<li>There are several sub-classes of classes defined in RDF and RDFS, and also some sub-properties of rdf:type</li>
</ul>

<b>General notes on notation:</b>
<ul>
	<li>UML Stereotypes (e.g. &lt;&lt;rdfsClass&gt;&gt;) are used as a shortcut to indicate class membership (rdf:type). It means the thing you're seeing on the page (box or line) is an instance of the thing specified in the stereotype.</li>
	<li>There is an examples package (not exported with the RDF) that contains a number of instances used in example diagrams. Instances of <b>Elements </b>are shown with a black background. Instances of <b>ClassOfElement </b>are shown with a yellow background if they're <b>ClassOfEntity </b>and a pink background if they're <b>ClassOfEvent</b>.</li>
	<li>Stereotypes are used liberally (see above) as a shorthand for rdf:type</li>
	<li>rdfs:subClassOf (relates classes to their supertypes) is shown with a thick royal blue line</li>
	<li>rdfs:subPropertyOf (related properties to their subproperties) is shown with a thick dark blue line</li>
	<li>Sometimes, a pattern defined at a high-level is referred to using a UML:dependency. This has no formal semantics other than to indicate to the implementer that the pattern should be used in this case</li>
</ul>

## <a id="{F2B6CFA8-1B10-4cb8-AF0D-FFAF0A28C247}"></a>Model Change Log

<b>v4 Beta 1 - Released September 2018 to IES team for internal review</b>
<b>
</b><b>v4 Beta 2 - Released December 2018 to wider community for review, including some implementation trials</b>
<b>
</b><b>v4.0.0 - FIRST OFFICIAL RELEASE - Changes resulting from initial release and trial implementations</b>
<ul>
	<li>Rename iso3166-1Alpha-3 to iso3166_1Alpha_3 - hyphens may cause issues with some programming languages (e.g. Python)</li>
	<li>Rename UN-LOCODE to UN_LOCODE - hyphens may cause issues with some programming languages (e.g. Python)</li>
	<li>Addition of SubjectOfInterest - required for every inter-agency data exchange trial implementation</li>
	<li>Addition of isPrimaryForOrganisation - added to cover things like primary names, primary SOIs, etc. within context of an organisation</li>
	<li>"venue" attribute on Ticket changed to "venueStatedOnTicket" to make it clear this may not be the final venue of the event</li>
	<li>Attendance added as subtype of Presence for when the Entity present is a Person (particularly useful with unidentified people)</li>
	<li>Duration added - this was an oversight. It had been discussed and was supposed to have been added, but slipped through the net.</li>
	<li>Reversed the direction of all the representation relationships (names, IDs, etc.) as the existing direction was counter-intuitive in RDF TTL and JSON-LD</li>
	<li>vehicleIdentificationNumber had not been changed to an Identifier before initial release. This was an oversight. Now corrected.</li>
</ul>
<ul>
	<li>bookingReference had not been changed to an Identifier before initial release. This was an oversight. Now corrected.</li>
	<li>Added knownAssociate to the Social diagram</li>
	<li>isTeacherOf added to Professional diagram</li>
	<li>worksWith reinstated (was taken out in v4, but there are cases where it can't be replaced by organisation and employedBy)</li>
	<li>PeriodOfTime was causing problems in initial implementations around how to query it. This has now been fixed with the explicit addition of ArbitraryPeriod and the rationalisation of the attributes used.</li>
	<li>Added OnlineArtefactInEvent to cover when OnlineArtefacts participate in online events</li>
	<li>Added Cookie as an OnlineArtefact and also a relationship called cookieOnDevice</li>
	<li>Changed a lot of IDs and Names in the Online diagram that were attributes into Names and Identifiers.</li>
	<li>URI is now all upper-case</li>
	<li>Added subtypes of CommunicationsAccount - e.g. TelephoneAccount, EmailAccount, etc.</li>
	<li>Added hostedOn relating a WebResourceState to the OnlineService that hosts it</li>
	<li>WholeLifeState removed. Was never needed and was a hangover from early IES 4 development work.</li>
	<li>holderOfAccount direction changed and renamed to holdsAccount</li>
	<li>ClassOfState added to enable Roles</li>
	<li>Roles and Posts added</li>
	<li>OnlineAccountState added to cope with changing screen names, passwords</li>
</ul>

<b>v4.1.0 - Changes resulting from project engagements</b>
<ul>
	<li>Device - classes replace attributes - <i>make </i>property now points to Organisation, <i>installedSoftware </i>replaces <i>operatingSystem</i>, <i>model</i> now relates to ModelOfDevice</li>
	<li>Currency model revised to use classes, and link to ISO standard ID and country</li>
	<li>TelephoneCountryCode revised to uses classes and link to Country</li>
	<li>Documents - DocumentFormat added as class, title changed to subclass of Name, publicationDate now an objectProperty to ParticularPeriod</li>
	<li>DataObject - DataKey becomes an identifier and ObjectName a Name</li>
	<li>IdentityDocument - dates changed to objectProperties pointing at ParticularPeriod. idGender now an objectProperty. visaType now an objectProperty</li>
	<li>Person - Gender now a Class</li>
	<li>Communication / Online Event - there were two classes for Message - Message and Messaging. Messaging has been removed.</li>
	<li>vehicleColour now changed to objectProperty (hasColour) and moved up to AssetState</li>
	<li>GeoRepresentation, ISO19125-WKT and GeoJSON added (see Location page)</li>
	<li>Language is now a class and hasLanguageProficiency links a PersonState to their LanguageProficiency - also inLanguage property added to Representation, and called-out the proficiency as a class in its own right</li>
	<li>PaymentArtefact - branding now relationship to Organisation, cardType now relationship to a Class, areaOfCoverage now relationship to Location</li>
	<li>AgreementName added - now using naming pattern</li>
	<li>Business - transferType now an objectProperty (relationship)</li>
	<li>CriminalActivity - type of offence now managed as a class, and the offenceCode identifies the Class</li>
	<li>PartNumber now identifier on ModelOfDevice</li>
	<li>serviceIdentifier now TravelServiceIdentifier</li>
	<li>Observation pattern added</li>
	<li>Actor and ResponsibleActor replace PersonOrOrganisation</li>
	<li>serviceType now onlineServiceType and is now an objectProperty</li>
	<li>ClassOfFinancialAccount added. JointAccount added</li>
	<li>bookingMethod now implemented as ClassOfTravelBooking</li>
	<li>paymentMethod (TravelBooking) now replaced using the Trade model</li>
	<li>Rights and Reservations added</li>
	<li>Interest - now modelled as states so that attributes can be attached.</li>
	<li>altitude - now uses the measures and characteristics model</li>
	<li>PointOnEarthSurface, Latitude, Longitude and isCentroidOf added, replacing the old geoIdentity which was a hangover from IES3 and made no sense in 4.</li>
	<li>hasHeight (person) now uses characteristics and measures model - now PersonHeight</li>
	<li>hasTheme (Investigation, Communication, etc.) added to cover those things that are of interest post-event or thematically - e.g. the thing being investigated is not involved formally</li>
	<li>Definition for IPAddress still mentioned attribute qualifiers (from v3 of IES) for dealing with IPv4 and IPv6. These are now subtype of IPAddress</li>
	<li>A very large number of definitions were incomplete, wrong or just missing. These are now fixed</li>
	<li>GeoPoint added - supertype of PointOnEarthSurface - this allows for points above or below the surface of the earth</li>
	<li>PassengerName, SeatNumber and BoardingCardNumber are now identifiers and names of Passenger</li>
	<li>countryOfRegistration and countryWhereRegistered merged</li>
	<li>A basic model for characteristics, measures and units of measure has been added as the current reliance on strings and fixed units was seen to be inadequate by users</li>
	<li>PartOfFacility and RoomNumber added</li>
	<li>AssessToBeTrue and PossibleWorld added - straw-man models for working with probabilistic data and scenarios</li>
	<li>Disposition - Capability and Tendency added - way to deal with dispositional properties</li>
	<li>payLoadContents relationship added - provides way to hold more than one payload per file</li>
</ul>

<b>v4.2.0 - Changes resulting from project engagements</b>
<ul>
	<li><b>Possible Worlds Model Added - </b>placeholder for dealing with modal logic. This will grow over time. Shown on assessments page.</li>
	<li><b>TerroristOrganisation </b>now a subtype of OrganisationState to allow for different parties viewing and organisation as being terrorist at different times. This also allows the assessments model to be used.</li>
	<li><b>CriminalOrganisation added</b> - subtype of OrganisationState, working in a similar way to TerroristOrganisation</li>
	<li><b>LawEnforcementOrganisation </b>added - subype of Organisation.</li>
	<li><b>ClassOfOperation </b>added at request of Home Office Vivace. This enables them to manage multiple taxonomies of criminal investigations in used throughout the UK and international partners</li>
	<li><b>Authorisation </b>model added at request of HO Vivace - provides a high-level framework for things like warrants and other types of authorisations.</li>
	<li><b>EventState </b>added</li>
	<li>make and serialNumber now properties of Asset rather than Device</li>
	<li>staysAt added to show where a Person stays as opposed to where they legally reside.</li>
	<li><b>VersionOfDocument </b>added</li>
	<li><b>NetworkInterface </b>added</li>
	<li><b>RadioMast </b>and <b>CellularBaseStation </b>added</li>
	<li><b>RadioCoverageArea </b>added</li>
	<li><b>MapGridArea </b>and <b>OSGridReference </b>added (requested by Police / Home Office)</li>
	<li><b>Easting </b>and <b>Northing </b>added (requested by Police / Home Office)</li>
	<li>nephewOrNieceOf and cousinOf added</li>
	<li><b>Team </b>and <b>Department </b>added to organisation model</li>
	<li><b>ClassOfOrganisation </b>added  (requested by Police / Home Office)</li>
	<li><b>OrganisationIdentifier </b>added  (requested by Police / Home Office)</li>
	<li><b>Accent </b>added  (requested by Police / Home Office)</li>
	<li><b>DocumentSection </b>added  (requested by Police / Home Office)</li>
	<li><b>AuthorisationDocument </b>and <b>RequestDocument </b>added  (requested by Police / Home Office)</li>
	<li><b>EncodedData </b>and <b>JsonData </b>added  (requested by Police / Home Office)</li>
	<li>"model" property removed - now use rdf:type</li>
</ul>

## <a id="{E169A2F5-85CB-41a7-A8B5-5BFAC5330AB5}"></a>IES Overview
![IES Overview Diagram](Images/EAID_E169A2F5_85CB_41a7_A8B5_5BFAC5330AB5.png)

### IES elements in this diagram:

* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [isStateOf](#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [isParticipationOf](#{DF9F6056-CCD4-41aa-9A86-536F6150EC25})
* [isParticipantIn](#{BAEA86D9-C90E-4f8d-96F5-A01BB0C49711})
* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})

The Information Exchange Standard is based on 6 key items which are subtypes of ExchangedItem:

<ul>
	<li>Element - anything physical - i.e. things that have extent in space (and time)</li>
	<li>Entity - a tangible thing like a Person, a Device, Location, etc.</li>
	<li>ClassOfElement- a class or category of Element</li>
	<li>State - a temporal state of an Entity (e.g. a moment in a Person's life, a phase of a Project, etc.) and can be of any duration</li>
	<li>Event - an activity or incident, involving one of more participating Entities, that occurred/started at a specific point in time - e.g. a meeting or a telephone call.</li>
	<li>PeriodOfTime - a specific period of time (past, present or future)</li>
	<li>relationship - relates ExchangedItems.</li>
</ul>

## <a id="{164BAFC4-0C40-4900-8A83-2B62248BF22D}"></a>Relationships
![Relationships Diagram](Images/EAID_164BAFC4_0C40_4900_8A83_2B62248BF22D.png)

### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [isStateOf](#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E})
* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [BoundingState](#{892345CD-9FA7-4982-978D-B6D3ABAE839C})
* [isStartOf](#{D9E068B1-2A44-4523-B8FC-F9888212B35C})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [inPeriod](#{2F08EF25-A5C8-48ad-85E3-903DB008AA19})
* [worksFor](#{181AAC84-26CE-4531-AC32-A73B8FD8B858})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [ContinuousState](#{6E5AF4BB-BB7F-4387-A7BB-476B81FEC103})
* [PersonState](#{38F8B795-0BCE-4945-8C69-8678ED935C1A})
* [siblingOf](#{A0D40C4F-B513-4c9f-8D4A-79D0FA7CEF50})
* [familiallyRelatedTo](#{3AA26AC6-206D-4b6d-BDEC-C9E2B4814BE7})
* [Actor](#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B})
* [ActorState](#{7ED8BC7C-A85F-4ed5-AC6F-D640F2DF4B7B})

Relationships may exist between ExchangedItems in IES - and can be used to assert anything from structural to legal connections between things. The concept of a relationship should be familiar to anyone who has looked at data model or ontology before. However, as IES4 is a 4D ontology, the relationships may only apply to a certain phase (state) of the Element - e.g. someone working for an Organisation for a period of time. Unlike attributes, the majority of relationships fall into this category. There are exceptions, such as being the sibling of someone (it's for life for both of them) but it turns out the majority are temporal. Like attributes, we create a State of the Entity instance in question and then attach the relationship to the State. 

In the example below, Fred has always been Barry's sibling and will continue to be whilst they both exist so there is no need for a State. In the second relationship, Fred worked for Acme since 5th December 2011, and is still working there because there is no end date. 

Note: in the example below, Fred still works for Acme. But if Fred had left Acme, and we didn't know when, the end BoundingState should be created to show the Employed state had ended, even though there is no associated PeriodOfTime

## <a id="{AC49DE36-990B-4c27-BA39-7C78A474C589}"></a>Period of Time
![Period of Time Diagram](Images/EAID_AC49DE36_990B_4c27_BA39_7C78A474C589.png)

### IES elements in this diagram:

* [after](#{FA4DDF04-16DA-4b5c-AE9A-6AB8CD07DCDB})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [inPeriod](#{2F08EF25-A5C8-48ad-85E3-903DB008AA19})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [RecurringPeriod](#{986E66AC-9092-410b-88AD-30B86EFC32DD})
* [ParticularPeriod](#{2173F463-524C-457c-B106-51322F64F122})
* [Duration](#{7852A5E5-8684-49f2-82AE-3368032163B1})
* [ValueInSeconds](#{E485D394-B9D7-40b6-BD44-E5970B2118BD})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [ArbitraryPeriod](#{68BA678C-DCA8-453e-BFCC-D9FB48339D99})
* [recurrentPeriodRepresentation](#{442AC7F0-AE57-4090-88D6-55A3825ECEAA})
* [iso8601PeriodRepresentation](#{E9372543-434E-45d3-A1F0-8D711952D10A})
* [startsIn](#{861E3D08-3659-489a-B100-0E943CF3F3F0})
* [endsIn](#{6767DFCD-3FCB-42cc-BEE3-9FA9A324DF0B})

Periods of time are Elements in a 4D ontology. They can be treated like any other element -e.g.  assembled with isPartOf relationships. This is the big advantage to a 4D ontology - time is treated the same way as space, which allows complex temporal logic information to be expressed using very simple constructs. 

IES also allows a duration to specified even when the precise start and end are not known - e.g. we can specify a meeting lasted an hour and took place on a particular day, but we don't know what time it began and ended.

Note: to prevent duplicate periods being created, the uri of each period should reflect the ISO8601 datetime (encoded to % out the disallowed URI characters). So for example, the uri for January 2008 would be http://iso8601.iso.org#2008-01. For ParticularPeriod, this is fairly simple. For PeriodOfTime, the ISO8601 encoding for the period should be used.

In the first example below, we show that Fred began working for Acme in 2011, and that we know he left Acme, and we're not sure of the day he left, but it was before 2016-05-07.

Technically, a PeriodOfTime is all of space, for a specific (or recurring) period (see the second example below; a space-time diagram which has 3 particular days, and a recurring 1 minute period, every day):

## <a id="{37882C3A-2915-4112-8EB2-ABB1C071165C}"></a>Where and When
![Where and When Diagram](Images/EAID_37882C3A_2915_4112_8EB2_ABB1C071165C.png)

### IES elements in this diagram:

* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [inLocation](#{463F9B14-2D14-4364-B4F0-658A20DFCBFA})
* [inPeriod](#{2F08EF25-A5C8-48ad-85E3-903DB008AA19})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [happensIn](#{60A37745-8DD5-4e4c-9A4C-6957F71AD971})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [takesplaceIn](#{5D13DE13-CAAC-4879-9237-D20A6846F4D8})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})

Because IES4 is a 4D ontology, time and space (in fact spacetime) are handled in the same way*. If something happens entirely within a location, it is part of that location. If a person walks through a location, there is a state of them that is part of that location. Similarly, if something happens in a particular period of time, it is part of that period of time. IES4 specifies subproperties of the isPartOf relationship with slightly more intuitive names;<i> inLocation, happensIn, takesPlaceIn, inPeriod</i>, etc.

States are a key feature in all of this. States are special kinds of parts (in 4D) that are all of the space for some of the time - e.g. you yesterday, you today. They form the basis for temporal properties, participations, etc. 

<i>* Space is a relative thing - you may move around relative to other things, but the whole-life you is a single Entity instance. There are states of the that whole-life Entity that are part of different Locations though. </i>

## <a id="{926F5679-25C6-47a6-AAB0-65F3A7406B99}"></a>Start and End
![Start and End Diagram](Images/EAID_926F5679_25C6_47a6_AAB0_65F3A7406B99.png)

### IES elements in this diagram:

* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [BoundingState](#{892345CD-9FA7-4982-978D-B6D3ABAE839C})
* [BirthState](#{CFE53096-32FC-47c8-98BA-950EE6F988CB})
* [Departure](#{0FCBDA68-1B1C-40e1-9C5B-0E225CA827DB})
* [DeathState](#{F6173D27-D86D-40f8-A5B0-36DCCF85D396})
* [Arrival](#{F2C03DA3-B554-4bde-A0DE-EFB5BEE19C56})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [ContinuousState](#{6E5AF4BB-BB7F-4387-A7BB-476B81FEC103})
* [Movement](#{95B5ACC4-956A-4b29-AB9E-BDCD12EF319F})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [isStateOf](#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E})
* [isStartOf](#{D9E068B1-2A44-4523-B8FC-F9888212B35C})
* [isEndOf](#{EA859D48-5BA4-40b3-A52D-1465D1765262})

The starts and ends of Elements can be modelled using BoundingStates. A BoundingState can be connected to the Element via an <i>isStartOf </i>or and <i>isEndOf </i>relationship to indicate whether it begins or ends the Element. 

There are some special cases of BoundingStates such as BirthState, Departure, etc.

The use of BoundingStates in combination with the <i>after </i>relationship allow complex temporal logic to be expressed using very simple constructs - e.g. Elements starting before others, ending before others, etc.

## <a id="{0EBD3547-89A5-45c0-ACA6-BC125D0E885E}"></a>Event Linkages
![Event Linkages Diagram](Images/EAID_0EBD3547_89A5_45c0_ACA6_BC125D0E885E.png)

### IES elements in this diagram:

* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [after](#{FA4DDF04-16DA-4b5c-AE9A-6AB8CD07DCDB})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [isStateOf](#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [BoundingState](#{892345CD-9FA7-4982-978D-B6D3ABAE839C})
* [isStartOf](#{D9E068B1-2A44-4523-B8FC-F9888212B35C})
* [isEndOf](#{EA859D48-5BA4-40b3-A52D-1465D1765262})
* [ContinuousState](#{6E5AF4BB-BB7F-4387-A7BB-476B81FEC103})
* [EntertainmentEvent](#{78C33499-CD14-43cb-82AE-93A0F8CF022B})

IES 3 introduced the concept of EventLinkage - associations between Events. As of v3.2 of IES, few of these EventLinkages had been specified and those that had were covered by relationships in v4 - isPartOf and after. 

The example below shows two football matches that were part of the World Cup in 2018, and the fact that one happened (i.e. started <i>and </i>finished) before the other.

For more complex temporal logic, such as an Event <i>starting </i>before another one, the after relationship can be used between BoundingStates. In the example below, the Sweden vs England match started after the Russia V Croatia match

## <a id="{1EE6C0C5-B494-4395-9C59-AEDC7B7971D9}"></a>Event Participation
![Event Participation Diagram](Images/EAID_1EE6C0C5_B494_4395_9C59_AEDC7B7971D9.png)

### IES elements in this diagram:

* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [isStateOf](#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [isParticipationOf](#{DF9F6056-CCD4-41aa-9A86-536F6150EC25})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [isParticipantIn](#{BAEA86D9-C90E-4f8d-96F5-A01BB0C49711})
* [isParticipantStateIn](#{A77A19DA-2775-4dfa-A76C-41C158AC582C})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [ContinuousState](#{6E5AF4BB-BB7F-4387-A7BB-476B81FEC103})
* [BoundingState](#{892345CD-9FA7-4982-978D-B6D3ABAE839C})
* [isStartOf](#{D9E068B1-2A44-4523-B8FC-F9888212B35C})
* [isEndOf](#{EA859D48-5BA4-40b3-A52D-1465D1765262})
* [Meeting](#{6445E51F-3DDF-4dcf-ABDF-3ED123D53188})
* [CoLocation](#{3524D10D-D9B0-416d-ADED-D5AAEB99DD09})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [Role](#{0066A327-D497-42e0-9F50-D988F522F4A5})
* [hasRole](#{5C76592F-C47D-40ee-8D82-497962686D34})
* [MeetingChair](#{B499C172-310D-4c5f-BA92-93B1C7874EEB})
* [Attendance](#{626D5F2C-9153-40f4-9F2A-393B6DB072D3})
* [Actor](#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B})

Participation in Events is modelled in a similar way to temporal relationships. Just as with relationships, we care about the period of time that a participant (an Entity) was involved in an Event. A subtype of State (EventParticipant) connects the Entity to the Event.

This allows us to have many participants (Entities) in an Event, and for each of their participations to have a different start and end times. So, in the example below, we can see that Barry left the meeting after 12 minutes and that Vlad was only there for 2 of the 3 hours.

IES4 also has a subtype of EventParticipant called ActiveEventParticipant. Subtypes of this class are those participations where the participant is actively contributing to the event. Those participations that are not subtypes of ActiveEventParticipant are assumed to be passive.

The Role construct for states is inherited by EventParticipant allowing more specific roles to be defined for the EventParticipant. 

## <a id="{C8ABE75C-87AF-4b36-9D4A-456CF2657B39}"></a>Sometimes
![Sometimes Diagram](Images/EAID_C8ABE75C_87AF_4b36_9D4A_456CF2657B39.png)

### IES elements in this diagram:

* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [isStateOf](#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [inLocation](#{463F9B14-2D14-4364-B4F0-658A20DFCBFA})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [DiscontinuousState](#{52DB371E-71AC-4812-B3CF-0FD7D73F1BB0})
* [ContinuousState](#{6E5AF4BB-BB7F-4387-A7BB-476B81FEC103})
* [BoundingState](#{892345CD-9FA7-4982-978D-B6D3ABAE839C})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})

When modelling real world events, many models fail to distinguish between a specific Event or occurrence, and the more general case where something <i>usually </i>occurs. The 4D approach has an answer for this - temporally dissected states. These are like ordinary states, but are not contiguous in time. We also don't have to identify the individual occurrences, we just have to say that there are occurrences.

This is particularly useful with locations. If we want to say a vehicle is usually in a location, we don't want to have to identify every state of it when it was in that location. We can simply identify the collection of those temporally separated states, called a DiscontinuousState in IES 4. If we say that the DiscontinuousState of the car is in a location, we mean that all of the extent (which we haven't explicitly called out) is part of the location.

At first glance, this may seem contrary to the BORO mantra about always identifying the spatio-temporal extent of Elements. However, what this does allow us to identify an extent that we know exists, but we don't know the details. Like other States, we can identify the start and end times - e.g. saying a car usually parked in a particular location between one date and another.

## <a id="{55486513-19EB-4a97-AADB-62317E9EA00F}"></a>Types
![Types Diagram](Images/EAID_55486513_19EB_4a97_AADB_62317E9EA00F.png)

### IES elements in this diagram:

* [ClassOfClassOfEntity](#{1F9AC8FE-3862-48d6-A3DC-E429B08D2B26})
* [ClassOfClassOfElement](#{85305668-DE1A-454a-87EE-346A221E846C})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [ClassOfEntity](#{D1B2FB30-36CA-4012-B85F-514E270BF541})
* [ClassOfEvent](#{4EA194C6-BBF9-45ab-85DE-5802D8C3A531})
* [powertype](#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D})
* [TimeBoundedClass](#{E7A659A5-9059-4ea5-8FAB-8A29AFC47D9A})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [ParticularPeriod](#{2173F463-524C-457c-B106-51322F64F122})
* [beginBoundOfClass](#{2C441F0A-635D-41ef-B8CC-96AA07958F8E})
* [endBoundOfClass](#{F8109922-1CB1-490d-BBB5-FD5B76E19FD1})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [ClassOfState](#{0358DDAB-D22C-4ee5-8F9A-CF18F3E432BD})

IES4 allows new types (classes, categories, sets, whatever you want to call them) to be exchanged in the data payload. To do this, we "push up" a type level using the powertype relationship which formally specifies that one class is the set of all possible subsets of the other (see wikipedia entry for "powerset" and "Cantor's theorem"). 

<b>ClassOfEntity </b>is explicitly specialised for use in representation and identifiers, but otherwise <b>ClassOfEntity </b>and <b>ClassOfEvent </b>replace the old GeneralConcept Entity in IES3.

Hierarchies of <b>ClassOfElement </b>can be built using the <i>rdfs:subClassOf </i>relationship. Instances of the <b>ClassOfElement </b>can be asserted using <i>rdf:type</i>. See example below:

## <a id="{393BD76E-39F3-4bd0-9BBA-7E1AC7C63F0A}"></a>Representation and Content
![Representation and Content Diagram](Images/EAID_393BD76E_39F3_4bd0_9BBA_7E1AC7C63F0A.png)

### IES elements in this diagram:

* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [ClassOfEntity](#{D1B2FB30-36CA-4012-B85F-514E270BF541})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [WorkOfDocumentation](#{F0B48978-D4E4-45a4-8238-091A5B714D82})
* [isRepresentedAs](#{D106A0A9-55C4-454f-9E20-35BA54114036})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [ClassOfIndividualDocument](#{CCC8FA06-CDA8-491d-BFFC-0A88D6A565B1})
* [documentedBy](#{AC7C948A-F19C-4296-AC38-0FEE6A4C5E90})
* [ClassOfClassOfEntity](#{1F9AC8FE-3862-48d6-A3DC-E429B08D2B26})
* [ContentCategory](#{8CA5551A-EAEB-4145-A75F-2E7D7DAD5A57})
* [inCategory](#{D10B4B95-5BF1-4e3f-A2A8-8F52F045C31A})
* [inRepresentation](#{7238489D-6802-4733-9F7F-9B31D02B3C81})
* [GeoRepresentation](#{A8C07233-5D62-4ad4-B405-2D15CFC37497})
* [ClassOfRepresentation](#{4FFEB84D-B823-4829-9A3A-ADE51EF0F0F5})
* [Language](#{82652FF5-258F-459c-BC7F-6DAC65E1ECA1})
* [inLanguage](#{FF902F8E-6B22-4f17-9C16-48543251D22E})
* [DocumentSection](#{19FE20BA-D898-46d4-8916-3E73BC059D54})
* [EncodedData](#{8AF1DB0B-9BEB-4a33-A459-7EF2BE309E81})
* [GeoJSON](#{417C1F4E-6A5D-4631-B275-8E982252791A})
* [DataObject](#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2})
* [JsonData](#{6A9A065C-A31A-42be-B7E2-275F076DCA9D})

IES distinguished between things in the real world and our representations of them. In this case, a Representation is not a PhysicalThing (see Document for the distinction). Representations may be documents, videos, blog text, etc. The represents relationship links ExchangedItems to their Representations.

Sometimes it is important to establish arbitrary categories of Representation - such as "financial accounts", "pictures of kittens" or "educational films". ContentCategory is used to collect together all Representations of similar content.

## <a id="{A72D9272-DF55-4e58-9174-3F9F168438A0}"></a>Identifiers
![Identifiers Diagram](Images/EAID_A72D9272_DF55_4e58_9174_3F9F168438A0.png)

### IES elements in this diagram:

* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [ClassOfEntity](#{D1B2FB30-36CA-4012-B85F-514E270BF541})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [WorkOfDocumentation](#{F0B48978-D4E4-45a4-8238-091A5B714D82})
* [isRepresentedAs](#{D106A0A9-55C4-454f-9E20-35BA54114036})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [ClassOfClassOfEntity](#{1F9AC8FE-3862-48d6-A3DC-E429B08D2B26})
* [NamingScheme](#{222534A5-25C8-4ecd-BE55-27DA1534D402})
* [inScheme](#{7EB9FE85-127C-4918-AC56-62E1BE1DE825})
* [schemeOwner](#{8D42B4A8-30D3-459d-A729-F5C8FE16D418})
* [schemeMasteredIn](#{C2C5FF87-189C-478a-B3BF-4706D798087F})
* [System](#{F682A265-1AFE-4287-A9CD-0D4C83F54C52})
* [IndividualDocument](#{0F327324-6B4E-40b1-B96B-97A334BA5E4A})
* [ClassOfIndividualDocument](#{CCC8FA06-CDA8-491d-BFFC-0A88D6A565B1})
* [aCopyOf](#{22D9054C-AE5C-4afe-99D9-3C9D65C86CB9})
* [isIdentifiedBy](#{FBA54EEF-91BF-4ba2-8B67-79C899963149})
* [hasName](#{C3A36E36-0C73-4af7-88E3-81C9243CE456})
* [documentedBy](#{AC7C948A-F19C-4296-AC38-0FEE6A4C5E90})

IES4 distinguishes between things in the real world and representations of those things. The representation pattern allows any <b>ExchangedItem </b>to have multiple representations - e.g. a book about the Ministry Of Defence, the DUNS number for the Ministry Of Defence, etc. 

Representations specialise into <b>WorksOfDocumentation </b>(see Document diagram in Entities section), <b>Name</b>s, and <b>Identifier</b>s. <b>Name</b>s and<b> Identifier</b>s belong to <b>NamingScheme</b>s - this allows us to give context when an <b>Element </b>has more than one <b>Name </b>or <b>Identifier</b>. <b>NamingScheme</b>s may be implemented in <b>System</b>s and used by <b>Organisation</b>s. This replaces the idea of EnterpriseIdentity and SystemIdentity in IES3

## <a id="{80403A46-2297-4e05-8C9C-1F6EF5596779}"></a>Characteristics and Measures
![Characteristics and Measures Diagram](Images/EAID_80403A46_2297_4e05_8C9C_1F6EF5596779.png)

### IES elements in this diagram:

* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [Characteristic](#{A7F266E8-B1CB-4b9b-8AF1-1EF2A7D8F5EE})
* [Colour](#{B10D22FB-1D6A-47c9-B1C0-E870D43A5C52})
* [StandardMeasure](#{C441DE5B-739A-4a83-BE87-96BC63A530B3})
* [MeasureValue](#{3693B7DE-DCE7-4bf9-BC2A-A8914DA4A11E})
* [Length](#{5C21DE93-329F-4209-87FF-19610CB0D367})
* [Mass](#{AE8FC416-9650-472d-99C6-F0A46B7359EB})
* [Duration](#{7852A5E5-8684-49f2-82AE-3368032163B1})
* [ElectricCurrent](#{9442C4E6-A52B-4c93-B942-8B93D90B3B14})
* [measureUnit](#{161079F3-8089-4124-A67A-5D6A7A4EA511})
* [ValueInKilograms](#{E7A9BC2D-85E2-4999-90DC-B76C9CB57C42})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [hasCharacteristic](#{720D0AA3-81F7-4220-A7A5-34304E33B72F})
* [allHaveCharacteristic](#{81A1E70D-6ADB-4843-BCA6-C0A710E7716B})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [MeasureRange](#{CCBBF963-EB27-40d5-BE9F-47CDF4D352F8})
* [upperBound](#{D700FE64-4100-4ade-93CE-6219A7BC0BCB})
* [lowerBound](#{96717346-1DF4-4eae-A7CF-E389B4454B47})
* [hasValue](#{8FD84185-A7CE-4d5d-974B-55F693C4376D})
* [Temperature](#{3FEB0BB0-F127-431a-B117-CC986B11D61A})
* [AmountOfSubstance](#{324D0329-1299-45cc-92A5-270134E66512})
* [LuminousIntensity](#{8431C546-B6F9-406f-9ECD-383FE985D115})
* [Measure](#{6CF79FCE-E2C9-4e8b-848C-39BD8616F77D})
* [ClassOfMeasureValue](#{4520A91C-D956-46c1-9A81-93C4C0B12880})
* [UnitOfMeasure](#{9F2DE0F4-58B1-46b7-B25A-545D765381A8})
* [StandardMeasureValue](#{773272F0-DBAB-4c47-8E21-01171FC82245})
* [ValueInMetres](#{C8D4C3CB-16C2-44a7-B709-35CEBF219BF0})
* [ValueInCandela](#{391F91E4-768F-406c-A344-CC3331ABE2AC})
* [ValueInSeconds](#{E485D394-B9D7-40b6-BD44-E5970B2118BD})
* [ValueInAmperes](#{0C682BA6-23AB-459c-B8FF-A114AA27650B})
* [ValueInKelvin](#{32097C4D-A0FB-4024-BDB8-8E899DDCF217})
* [ValueInMoles](#{943CA047-F259-4181-BF04-F6D54065AAD4})

IES provides a basic set of classes for characteristics and measures. Characteristics are properties of Elements that are qualitative, Measures are quantitative. To support Measures, IES provides classes for all the SI units, a model for units of measure and an ability to specify measure ranges. 

The key points about this model are that the Measure is separate from its representation so the same measure can have more than value with different units of measure (e.g. 1kg and 2.2lbs). 

Characteristics and measures can be applied to an Element, or to a ClassOfElement in the case where all instances of the ClassOfElement share the same characteristic or measure - e.g. all London buses being red. 

This model is new in IES 4.1 - previously, there was no consistent way to do this, but mostly it relied on attributes. 

## <a id="{C9919009-48A5-4db1-8123-90396A6F3AD0}"></a>Disposition
![Disposition Diagram](Images/EAID_C9919009_48A5_4db1_8123_90396A6F3AD0.png)

### IES elements in this diagram:

* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [DispositionalClass](#{2855AF50-EEE4-4ced-B499-AE42423A4DE3})
* [ClassOfEntity](#{D1B2FB30-36CA-4012-B85F-514E270BF541})
* [ClassOfEvent](#{4EA194C6-BBF9-45ab-85DE-5802D8C3A531})
* [ClassOfState](#{0358DDAB-D22C-4ee5-8F9A-CF18F3E432BD})
* [Capability](#{91D62F08-ED05-4558-9321-368712A34A30})
* [isDisposedTo](#{B093F8DA-AE08-4819-8E1C-F119EF212566})
* [Tendency](#{2B451601-EC1D-4bd4-A782-6E0B7E0D416D})
* [allHaveDisposition](#{6F8504E0-E03C-43fa-AA81-C3341CA551E3})

A disposition is about an Element's capability or tendency to do something or to exhibit a property. It may be that the Element has never actually done the thing it is capable of - e.g. an aircraft capable of Mach 2 but that has not yet flown that fast. Similarly, a Person may be assessed as having a tendency towards violence based just on what they say and threaten to do, but may not have actually been violent.

Dispositions are managed in IES using DispositionalClass - something that was also in the international IDEAS ontology where capability was a key concept they had to model. Dispositional classes collect together all Elements that share the same disposition (e.g. all aircraft capable of Mach 2). 

## <a id="{1A40117E-E6F6-4ae0-A438-8583E896BE00}"></a>Attributes
![Attributes Diagram](Images/EAID_1A40117E_E6F6_4ae0_A438_8583E896BE00.png)

### IES elements in this diagram:

* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [ClassOfClassOfElement](#{85305668-DE1A-454a-87EE-346A221E846C})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})

Attributes can be applied to any Exchanged Item - Entities, Events and ClassOfEntity.

Attributes are RDF properties (actually, OWL datatype properties), typed by any XML Schema simple datatype - e.g. xsd:string, xsd:double, xsd:dateTime, etc. (refer to W3C XML Schema specification for complete list).

Attributes are not as widely used in IES4 as in IES3 where they were used for measures, identifiers and names. In IES4 they are only used for categorical statements - e.g. the purpose of a mission, the amount of currency, etc.

## <a id="{60CD4A4C-652B-40c9-A65B-321A73329D6E}"></a>Source References
![Source References Diagram](Images/EAID_60CD4A4C_652B_40c9_A65B_321A73329D6E.png)

### IES elements in this diagram:

* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [ClassOfEntity](#{D1B2FB30-36CA-4012-B85F-514E270BF541})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [WorkOfDocumentation](#{F0B48978-D4E4-45a4-8238-091A5B714D82})
* [isRepresentedAs](#{D106A0A9-55C4-454f-9E20-35BA54114036})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [ClassOfIndividualDocument](#{CCC8FA06-CDA8-491d-BFFC-0A88D6A565B1})
* [isIdentifiedBy](#{FBA54EEF-91BF-4ba2-8B67-79C899963149})
* [hasName](#{C3A36E36-0C73-4af7-88E3-81C9243CE456})
* [documentedBy](#{AC7C948A-F19C-4296-AC38-0FEE6A4C5E90})
* [DataObject](#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2})
* [Database](#{3099B032-4B0A-4aec-ABCD-3E862C4C1979})
* [DatabaseTable](#{D9E56CAA-4668-4248-B087-C041363816DD})
* [DatabaseItem](#{73F8D96C-A9EC-4301-9968-0F7BF9826C45})
* [inRepresentation](#{7238489D-6802-4733-9F7F-9B31D02B3C81})
* [DatabaseRow](#{1F23EB62-323B-402d-84BD-B4D417ED1A73})
* [hasSourceReference](#{16480E86-9FE4-4b37-ACFB-9E410F190664})
* [EncodedData](#{8AF1DB0B-9BEB-4a33-A459-7EF2BE309E81})

The IES3 Source Reference capability is maintained in IES4, but leverages the Representation pattern to achieve the same thing. The key relationship here is hasSourceReference  which links the Representation (Document, DataObject, etc.) to the ExchangedItem it was the source for.

Representations can be assembled into structures using the inRepresentation relationship.

<i>Note: As IES4 is modelled in RDF Schema, the data will be RDF (encoded as TTL, JSON, XML, etc.). Referring to relationships (i.e. triples) in RDF involves using the RDF reification pattern, so if sourceReferenceFor is to relate to an attribute or relationship then RDF reification is the approach that shall be used.</i>

## <a id="{17F25B76-6D6D-4d6e-8BC8-F97C1B2DCC0B}"></a>Payloads and Groups
![Payloads and Groups Diagram](Images/EAID_17F25B76_6D6D_4d6e_8BC8_F97C1B2DCC0B.png)

### IES elements in this diagram:

* [isPrimaryForOrganisation](#{D6974F5E-B24C-4a06-9AC1-DB6299E9BF55})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [SecurityLabel](#{CED628E4-8641-486b-BCD7-CB4E147E7AE6})
* [payloadLabel](#{259167E4-D0B3-4f03-9653-CAD778F5F6F3})
* [protectiveMarking](#{7E5590F8-B142-49d8-8FB0-414716CF9F16})
* [andGroup](#{1326576A-6240-47b0-AED7-5F3FC4E3884D})
* [orGroup](#{71249792-E0AF-4f98-86ED-17115F1734A7})
* [permittedNationality](#{FA623989-B6A4-40e2-A956-B8FFEA478895})
* [permittedOrganisation](#{90F3E89D-1456-41fe-9354-4E13C4D79564})
* [handlingCaveat](#{1C02B06E-3159-48f6-9575-64B62765498B})
* [statementLabel](#{7EC7FCEE-7C60-4233-8938-D6320BD951F2})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [GroupOfItems](#{04C2111A-D958-4a95-9271-7208B849DDD8})
* [inGroup](#{C21D2CA2-6F42-4b7c-9092-8B8C5B7BAF9F})
* [groupName](#{42463865-450C-4a9a-9EF0-5322222C2B97})
* [groupDescription](#{2F618A01-5D5F-483c-8652-8B81196AA086})
* [ExchangePayload](#{749B002E-37B1-4754-B3B2-96642B3CF4A7})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [System](#{F682A265-1AFE-4287-A9CD-0D4C83F54C52})
* [originator](#{4978D7F3-E686-4b30-9356-F0C4DC7A158D})
* [originatingSystem](#{D4A003A3-7FEF-409c-8935-743CD97299E7})
* [payloadContents](#{10DEB6B8-80CC-4bfc-B10F-1830B559C21F})

IES3 had the concept of an <b>ExchangePayload </b>object to which all the ExchangedItems and Groups were attached. In reality, there was only ever one payload in a file, so in IES4, whilst the <b>ExchangePayload </b>class is kept, it is simply an object in the RDF file to which meta-data about the whole file can be attached. The concept of <b>GroupOfItems </b>is retained from IES3.

It is sometimes important to specify the origins (organisation, system, etc.) of certain information. This is achieved using the <i>originator </i>and <i>originatingSystem </i>which link <b>rdf:Resource</b>s (i.e. anything) to their origin. These can be applied to GroupsOfItems also, but care must be taken not to put the same <b>ExchangedItem </b>in different <b>GroupOfItem </b>instances that have <i>originator </i>or <i>originatingSystem </i>properties linked to them. If the source of a relationship (triple) has to be specified, the originator and originatingSystem properties can be applied to rdf:Statement (see RDF documentation on reification).

## <a id="{C58F08D6-9661-4b21-8576-B7620B7D84E3}"></a>Metadata
![Metadata Diagram](Images/EAID_C58F08D6_9661_4b21_8576_B7620B7D84E3.png)

### IES elements in this diagram:


IES has classes for dealing with documents, and for dealing with representation of objects in a lot of different ways. However, when it comes to specifying meta-data about IES instances - e.g. who created, when it was created, etc. - the Dublin Code metadata standard is to be used.

The fact that IES has its own document referencing capability <i>and</i> Dublin Core may seem a little confusing. The example below attempts to clear this. 

## <a id="{1167BC44-F4AF-4485-88BD-DBA2C4B5293E}"></a>Entities


### <a id="{E9EC7882-A905-4bc5-ACF7-6AC9C28E8596}"></a>Amount of Money
![Amount of Money Diagram](Images/EAID_E9EC7882_A905_4bc5_ACF7_6AC9C28E8596.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [AmountOfMoney](#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8})
* [currencyDenomination](#{AE8A5533-9C08-46e7-8131-E3D119F6AAE3})
* [currencyAmount](#{C53F62D0-0817-404b-9624-95A89D94F9A2})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [Currency](#{A06EE74F-9A66-4b63-8DC3-3B1C2B362862})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [ISO639-3Code](#{ECFED94D-CC69-46b9-B09D-B282D5665787})
* [Country](#{92EBA9B9-48C2-4082-9FE5-603977BD6846})
* [isLegalTenderIn](#{2415B865-3C37-4595-9F38-11075EAB5D34})

This part of IEAS deals with  specific amounts of a given currency

### <a id="{DC826580-C2BF-482e-ABF2-B90684A4CB74}"></a>Assets
![Assets Diagram](Images/EAID_DC826580_C2BF_482e_ABF2_B90684A4CB74.png)

#### IES elements in this diagram:

* [Mass](#{AE8FC416-9650-472d-99C6-F0A46B7359EB})
* [Actor](#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [AssetState](#{CA196722-9531-4eb4-A8CF-B9A5145CDCFD})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [IndividualDocument](#{0F327324-6B4E-40b1-B96B-97A334BA5E4A})
* [PaymentArtefact](#{9882D901-1B22-4b89-81D1-031F840A20D0})
* [Vehicle](#{3B916F09-F3F4-43e9-9C84-99009C685396})
* [AmountOfMoney](#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [RealEstate](#{8E0DF17F-34EE-43c6-8DA4-30F698384FD3})
* [storedIn](#{2E33B6DC-54D5-4e5e-9894-B2801F174B00})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [owns](#{FDD94D9F-F343-4c1b-9688-752C896A3C7C})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [inPossessionOf](#{0A28624B-C5E3-461e-B84A-E55B550B5DD6})
* [userOf](#{01984617-C96D-48b3-ACDE-25F525719AEF})
* [hasAccessTo](#{CB7F872F-7999-4bfd-8274-2C0E0AFE22AB})
* [ValueInKilograms](#{E7A9BC2D-85E2-4999-90DC-B76C9CB57C42})
* [Colour](#{B10D22FB-1D6A-47c9-B1C0-E870D43A5C52})
* [Rights](#{487778E0-4BD7-4d9a-B7F7-63731478E1A2})
* [Nation](#{6AE6F8A5-F427-4ea6-BABD-5720F07430F5})
* [jurisdictionOfRights](#{62EF76B2-4AB0-4e1e-98C4-61C3A85BF980})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [rightsTo](#{04A80EF0-8E34-4bdb-8A8E-31D89028F9B6})

Assets are Entities that are either man-made or whose extent is defined in such a way as to specify ownership - e.g. a parcel of real estate.

### <a id="{A4475333-349B-4d3a-81FA-B899DC1961D1}"></a>Communications Account
![Communications Account Diagram](Images/EAID_A4475333_349B_4d3a_81FA_B899DC1961D1.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [TelephoneAccount](#{593AE684-C2E9-4e40-A7FD-549BFA64900D})
* [EmailAddress](#{36F61EDF-6E6E-4d8d-9E75-275A820F6D96})
* [IMSI](#{C817C1ED-863B-41f0-B5C1-14117E926A94})
* [TelephoneNumber](#{168D7B01-CD70-4f83-A414-19B6ABEB961C})
* [EmailAccount](#{FCBB35B9-704B-46c1-8054-10B7DA7EB8F8})
* [OnlineAccount](#{E95170B9-2599-46dc-BEDC-012B08F09D43})
* [MobileTelephoneAccount](#{9F5EDA24-5991-48e7-9303-C86E25A196CF})
* [LandlineTelephoneAccount](#{D7F83A2D-6428-4211-964D-E1E8A8089083})
* [VoipAccount](#{2DB8231F-0673-4788-AE41-3F52A3702A2B})
* [CommunicationsIdentifier](#{A82378B9-9774-46b9-9845-CC75BE882F06})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [DeviceState](#{6107EEA5-1A13-46e4-83FB-14740437B814})
* [AccountNumber](#{A72F0FF1-88F2-4b36-A2C4-26B4B0698A2C})
* [CustomerIdentifier](#{43560C95-66A3-4d69-A743-F0A166DE51FC})
* [associatedPersonName](#{022535DE-2100-420b-B4BC-10465DEEEC3C})
* [Account](#{31BFE794-924E-44e3-942E-ADC9ED19FBA1})
* [AccountState](#{0BCDB801-1F3B-4496-B04B-95EF545E9445})
* [CommunicationsAccount](#{8300451C-1DF9-4545-9174-D8AA69C58CCD})
* [CommunicationsAccountState](#{20BB42F0-3F2D-4bb7-88DD-F4D05377D59B})
* [hasRegisteredCommsID](#{E076AFB8-F6F8-4b06-82B3-7ED568D1EE73})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [accountProvider](#{0F9244C3-B2F5-4b8a-AED2-54B7FDAB9578})
* [holdsAccount](#{6314A9B0-4578-42a8-A553-1FDDF35AC7F1})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [PersonState](#{38F8B795-0BCE-4945-8C69-8678ED935C1A})
* [hasAccessTo](#{CB7F872F-7999-4bfd-8274-2C0E0AFE22AB})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [AccountHolder](#{C93379F2-6B01-4100-ABFA-BD26098AC1CB})

Communications Accounts are new for IES4. In most online and telecoms scenarios, the account, who holds it, and who provides it are more important than the device or handset (which IES 4 majored on). CommunicationsAccount inherits much from the generic Account class, then adds a relationship to CommunicationsIdentifier.

### <a id="{9E7698FD-A154-4fb7-8054-A04D67EB71F1}"></a>Communications Device
![Communications Device Diagram](Images/EAID_9E7698FD_A154_4fb7_8054_A04D67EB71F1.png)

#### IES elements in this diagram:

* [CommunicationsDevice](#{32EB46A5-0FA4-44e9-A9E9-9424E80BDE91})
* [MobileHandset](#{3BF8FC71-64BD-4fb5-BEFD-D7FCB936FA12})
* [SatellitePhoneHandset](#{3634DBF3-AA3A-402e-9D08-906C06FAFEDB})
* [LandlineHandset](#{57C9F8DF-AFE6-4374-9403-ACACAC26FCE4})
* [CBRadioHandset](#{18EB7B22-5927-4b0e-98A8-638D28BDCF87})
* [IPPhoneHandset](#{0B494F4A-9E82-4667-89AD-3D22FC9B5742})
* [PersonalRadioHandset](#{9D84921F-87A3-4ee9-8A3D-A88F564295FA})
* [SIMCard](#{3244F6B1-8636-4895-B3B1-283CF057F826})
* [SerialNumber](#{51F79BC9-9BB5-47d6-973B-6F86F289B5FB})
* [make](#{E0036B31-8D73-4268-8959-6E9A5EE55BB2})
* [IMEI](#{3987794E-6E2E-4457-8BF7-47813B51B139})
* [installedSoftware](#{B37ADF66-D5D0-4144-9539-DA91BA302914})
* [Software](#{B6014BB6-FD82-4748-8DFF-65401770515C})
* [OperatingSystem](#{4F83D781-7E46-4ad4-B2A5-ECD27565EA49})
* [DeviceState](#{6107EEA5-1A13-46e4-83FB-14740437B814})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [System](#{F682A265-1AFE-4287-A9CD-0D4C83F54C52})
* [CommunicationsIdentifier](#{A82378B9-9774-46b9-9845-CC75BE882F06})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [ClassOfDevice](#{09F9136C-9069-47ec-A58E-FC26CF9BA55E})
* [NetworkInterface](#{C544CCAC-91C5-4e82-B5D9-7A1B8D48E771})
* [RadioMast](#{F02CFF55-12A7-4308-9A60-E2353DE5BE58})
* [CellularBaseStation](#{9D4A1395-8687-4f0b-BC5D-61A756210B4D})
* [userOf](#{01984617-C96D-48b3-ACDE-25F525719AEF})
* [hasAccessTo](#{CB7F872F-7999-4bfd-8274-2C0E0AFE22AB})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [ModelOfDevice](#{7A879268-33C2-4f2b-8928-9E78AFF01E69})
* [PartNumber](#{772CD8A3-3DCA-4cc7-8BA3-17D1C57E94BC})

Devices are Assets that have been designed to perform one or more functions. IES then further sub-divides Device into <i>System </i>and <i>CommunicationsDevice</i>. A CommunicationsDevice is a self-contained device that acts as an endpoint for communication. A System is a collection of interacting Devices that together provide one or more functions. System components are generally removable / replacable.

### <a id="{3B36B41F-8E34-4a09-8586-5A8DF2FC3574}"></a>Communications Identifier
![Communications Identifier Diagram](Images/EAID_3B36B41F_8E34_4a09_8586_5A8DF2FC3574.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [CommunicationsIdentifier](#{A82378B9-9774-46b9-9845-CC75BE882F06})
* [Callsign](#{25F4F685-3931-4cdc-AF43-1A9194BBE15D})
* [IPAddress](#{451C4C40-4183-4130-B67C-6F746B8B8BCA})
* [EmailAddress](#{36F61EDF-6E6E-4d8d-9E75-275A820F6D96})
* [IMSI](#{C817C1ED-863B-41f0-B5C1-14117E926A94})
* [MACAddress](#{DE1EDE92-142C-4c05-AD61-BE58822B2E17})
* [TelephoneNumber](#{168D7B01-CD70-4f83-A414-19B6ABEB961C})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [DeviceState](#{6107EEA5-1A13-46e4-83FB-14740437B814})
* [CommunicationsAccount](#{8300451C-1DF9-4545-9174-D8AA69C58CCD})
* [CommunicationsAccountState](#{20BB42F0-3F2D-4bb7-88DD-F4D05377D59B})
* [hasRegisteredCommsID](#{E076AFB8-F6F8-4b06-82B3-7ED568D1EE73})
* [TelephoneCountryCode](#{79C84EC1-83EC-45a8-A3CE-F88CFFBF9434})
* [Country](#{92EBA9B9-48C2-4082-9FE5-603977BD6846})
* [countryUsingDialCode](#{8C3F2C71-C7A2-414a-85C2-DFCD2D91D8E5})
* [IPv4Address](#{142D6D4D-6EF3-48aa-8B7B-86DA73690E3E})
* [IPv6Address](#{78549D65-75F2-41c3-AC14-F0D441AD6354})

CommunicationsIdentifiers identify Devices (actually DeviceState, as the identifier may change over time). The identifiers are usually managed in a CommunicationsAccount, and again, we use the State rather than the WholeLife CommunicationsAccount as CommunicationsIdentifiers can move from account to account. 

### <a id="{1810A643-CCD5-474b-AF1B-CE748179B427}"></a>Communications Identifier Range
![Communications Identifier Range Diagram](Images/EAID_1810A643_CCD5_474b_AF1B_CE748179B427.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [CommunicationsIdentifierRange](#{DF388418-F296-46a5-A2A3-4297F084DD07})
* [IPAddressRange](#{BEC2FDBC-6F37-4446-AEE1-3D4627DDD5F2})
* [DomainName](#{42FFB9AC-2D28-453a-80A0-2A271DA32EB5})
* [TelephoneNumberRange](#{007F88AD-9CDF-4aa1-BE73-18C688DA8C05})
* [idLowerRange](#{6C79CE89-8E17-4ee7-ABA8-DDA5D4AFC78B})
* [idUpperRange](#{7615FB07-E0C5-4734-AFC8-FD52688DD2CC})
* [CommunicationsIdentifier](#{A82378B9-9774-46b9-9845-CC75BE882F06})
* [DeviceState](#{6107EEA5-1A13-46e4-83FB-14740437B814})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [CommunicationsAccountState](#{20BB42F0-3F2D-4bb7-88DD-F4D05377D59B})
* [hasRegisteredCommsID](#{E076AFB8-F6F8-4b06-82B3-7ED568D1EE73})
* [CommunicationsAccount](#{8300451C-1DF9-4545-9174-D8AA69C58CCD})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})

A CommunicationsIdentifierRange is a CommunicationsIdentifier that specifies a group of identifiers for Devices. 

### <a id="{1F0FFC2A-9636-4070-BF77-E7503E68B9E1}"></a>Data Object
![Data Object Diagram](Images/EAID_1F0FFC2A_9636_4070_BF77_E7503E68B9E1.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [DataObject](#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2})
* [objectContentReference](#{6B06ABDD-05CF-485c-A483-563C5E85F189})
* [GeoObject](#{EA165884-8DF6-4aa6-848C-C682F6969D9F})
* [SchemaObject](#{D3375BB5-6773-40e1-8CA2-B393DD02B98C})
* [MediaFile](#{CE2E2EB2-17F7-4054-9107-E8DC275B0B11})
* [objectContent](#{222FBD07-DCCF-40c6-BD15-4ADBC64A8AA5})
* [GeoRepresentation](#{A8C07233-5D62-4ad4-B405-2D15CFC37497})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [Database](#{3099B032-4B0A-4aec-ABCD-3E862C4C1979})
* [DatabaseItem](#{73F8D96C-A9EC-4301-9968-0F7BF9826C45})
* [DatabaseTable](#{D9E56CAA-4668-4248-B087-C041363816DD})
* [DatabaseRow](#{1F23EB62-323B-402d-84BD-B4D417ED1A73})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [ObjectName](#{9A372833-B327-4cb0-9950-786A2FBF7CC3})
* [DataKey](#{2D88DE83-F87F-48ad-A485-9FFA79ED90D8})

A DataObject is a Representationt that may contain internal structure that can be exploited using bespoke tools and/or applications. DataObjects might be geoobjects, video files, audio files, etc.

### <a id="{7A96DA48-8EEF-46d2-9362-C506781AF268}"></a>Document
![Document Diagram](Images/EAID_7A96DA48_8EEF_46d2_9362_C506781AF268.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [IndividualDocument](#{0F327324-6B4E-40b1-B96B-97A334BA5E4A})
* [Report](#{8D510CB0-C9BF-4de3-A442-9070ABB15732})
* [Book](#{22AB6EA2-B088-4ef6-AE3A-5843FBA5C8AE})
* [Warrant](#{4CAD884A-1EA7-473d-9881-8B76EBF8526F})
* [Title](#{30F5944F-75C3-4f12-A315-4E94ABCA809E})
* [publicationDate](#{CD6E380B-7AD4-43d6-A128-9C666ABD8223})
* [hasPublisher](#{07FD1DF6-BA77-4657-B3D3-D6D579FD4608})
* [ReferenceNumber](#{A0DC70DD-9237-480b-A712-F5381C5FFA1A})
* [formatOfIndividualDocument](#{F1F94713-6D95-4928-B537-4FBA55D09E34})
* [hasAuthor](#{9464D864-E76F-4e09-89E1-D3B2D3E63F3B})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [URL](#{C23AB49C-0734-45b7-A383-8EEA305CDBE4})
* [WorkOfDocumentation](#{F0B48978-D4E4-45a4-8238-091A5B714D82})
* [aCopyOf](#{22D9054C-AE5C-4afe-99D9-3C9D65C86CB9})
* [IdentityDocument](#{BDF4EBD9-7F41-4d90-91A7-571177330C1B})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [IndividualDocumentID](#{D68F4E10-957A-4e98-8447-8F2768940DA7})
* [TimeBoundedClass](#{E7A659A5-9059-4ea5-8FAB-8A29AFC47D9A})
* [beginBoundOfClass](#{2C441F0A-635D-41ef-B8CC-96AA07958F8E})
* [endBoundOfClass](#{F8109922-1CB1-490d-BBB5-FD5B76E19FD1})
* [VersionOfDocument](#{ADB16761-4981-4476-BC53-2843587D1C02})
* [VersionNumber](#{E4C44F5B-5D57-4283-B985-5A2DA87BF212})
* [versionOf](#{C01F47A2-F545-4fac-A707-469AD32FBF94})
* [DocumentFormat](#{ACB44E46-7A30-4911-A9F0-3D5412FB3725})
* [format](#{EF2C13D4-7106-4799-BB72-7CD47714F257})
* [ParticularPeriod](#{2173F463-524C-457c-B106-51322F64F122})
* [isRepresentedAs](#{D106A0A9-55C4-454f-9E20-35BA54114036})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [documentedBy](#{AC7C948A-F19C-4296-AC38-0FEE6A4C5E90})

In IES 3 there was just "Document", but it wasn't clear if this referred to a specific, individual copy of a document, or just the document in general (of which there may be many copies). For example, it wasn't clear if it was "my copy of War &amp; Peace" or just "War and Peace".

This has been rectified in IES4 and "Document" has been replaced by "Work of Documentation" (the general case) and "IndividualDocument" (a particular instance of a document). In the majority of cases, WorkOfDocumentation will be used, but where we care about a particular instance (e.g. forensics, evidence, historical interest, etc.) then IndividualDocument should be used. The IndividualDocument can be related to the WorkOfDocumentation it is an instance of using the "aCopyOf" property.

### <a id="{29646663-65CC-41b5-A127-F8C3D6DD4FF5}"></a>Financial Account
![Financial Account Diagram](Images/EAID_29646663_65CC_41b5_A127_F8C3D6DD4FF5.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [FinancialAccount](#{44DAC574-2A2E-44bc-ACD2-236811FA8D29})
* [AccountNumber](#{A72F0FF1-88F2-4b36-A2C4-26B4B0698A2C})
* [BranchCode](#{012F7F29-4F8E-4263-8224-126050EE175F})
* [IBAN](#{40E59970-04CE-4961-83FC-179739C4DEC3})
* [CustomerIdentifier](#{43560C95-66A3-4d69-A743-F0A166DE51FC})
* [Country](#{92EBA9B9-48C2-4082-9FE5-603977BD6846})
* [associatedPersonName](#{022535DE-2100-420b-B4BC-10465DEEEC3C})
* [holdsAccount](#{6314A9B0-4578-42a8-A553-1FDDF35AC7F1})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [accountProvider](#{0F9244C3-B2F5-4b8a-AED2-54B7FDAB9578})
* [countryOfRegistration](#{D33498ED-B6A0-41ea-864F-CE95E2B1E010})
* [Account](#{31BFE794-924E-44e3-942E-ADC9ED19FBA1})
* [AccountState](#{0BCDB801-1F3B-4496-B04B-95EF545E9445})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [DiscontinuousState](#{52DB371E-71AC-4812-B3CF-0FD7D73F1BB0})
* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})
* [hasAccessTo](#{CB7F872F-7999-4bfd-8274-2C0E0AFE22AB})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [BankBranch](#{02E3C3B8-8650-4867-8390-823E4B3360E6})
* [Bank](#{4E10343E-8350-4354-B3DB-A7F74B4535EF})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [AccountHolder](#{C93379F2-6B01-4100-ABFA-BD26098AC1CB})
* [ClassOfFinancialAccount](#{901334E9-238C-4d05-8F85-FE9A8E537BA1})
* [financialAccountType](#{94BC4F7F-3DC3-4e26-8E2B-26E7D9B1A760})
* [JointAccount](#{AD17E3D9-CAB2-4a60-99C9-109F4496F92F})

Accounts are ways to collect together transactions and other related Events. A FinancialAccount is an Account that is used to manage financial transactions.

### <a id="{563B8C72-68EA-439b-88AF-424BF75DAA54}"></a>Identity Document
![Identity Document Diagram](Images/EAID_563B8C72_68EA_439b_88AF_424BF75DAA54.png)

#### IES elements in this diagram:

* [IdentityDocument](#{BDF4EBD9-7F41-4d90-91A7-571177330C1B})
* [BirthCertificate](#{4457E8AF-EDBD-4ef1-B62B-59037829B961})
* [DrivingLicence](#{44C1DD59-354B-405a-9755-417240802DE4})
* [NationalIdentityCard](#{843EDE77-78C4-4a09-9866-DBCC726AD5E6})
* [NationalIdentityNumber](#{F2CF8705-DA4A-4131-AB60-CF1AC33BED95})
* [Passport](#{13ABC7CA-915E-4069-8EA7-FD205A5336C5})
* [TravelVisa](#{C066EEB4-91AF-4ee6-BB02-44A49087946B})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [hasCountryOfIssue](#{E7500475-8C4F-47a3-8AAB-C5679621FAE8})
* [idDateOfBirth](#{9E77B9DE-E76A-454d-B4B5-52496358FC65})
* [hasStatedPlaceOfBirth](#{F95710A9-B0A7-4f7b-ADAA-08A2DCBD9C35})
* [idAuthenticity](#{1185F43F-7EBB-4e38-A1B3-FF1421F3416D})
* [validFromDate](#{6ACC2ACC-46F2-4a02-A3E7-D16BE8EB723B})
* [validToDate](#{680F737D-A8AB-4410-9F1D-FAD7BDC98447})
* [idDateOfIssue](#{ACAC12AD-16C3-480d-8149-C026F8BE9F81})
* [wasAuthorisedBy](#{7A58C9AD-C198-4a61-8244-DE5BBC591416})
* [HealthServiceIdentifier](#{FBCCD717-E163-4129-B270-966F5D404260})
* [SocialServicesIdentifier](#{DF17458A-3BB8-4851-B88A-1E08C2EFA697})
* [idGivenNames](#{77CA0C8D-71F0-4cb9-8621-407396FAC5A1})
* [idFamilyName](#{CCD1F7FE-C42A-4503-BF24-00E8805BD5DD})
* [idGender](#{D5B27630-C222-45be-87C2-5C4F8592487B})
* [hasStatedAddress](#{0451B5D4-99CB-47a7-BB93-DF4DF6625837})
* [idEmergencyContactName](#{96B7C774-1FE0-4307-BB62-B5899F953FF2})
* [idEmergencyContactTelNo](#{0198C1BE-43A0-4841-925E-FA5C47991AC3})
* [hasEmergencyContactAddress](#{0AAF6757-AAC9-43c4-8B43-CB3358EADCA4})
* [hasStatedPlaceOfIssue](#{644B75E8-92A0-4f16-861E-3B4FDFDF572E})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [hasStatedCountryOfResidence](#{9A4EB722-0BDA-4ba7-B895-7A4E273865C9})
* [hasStatedNationality](#{C8AB9A91-97ED-4868-8167-44E71F40AFE7})
* [isAuthorisedForUseWithPassport](#{1CA57828-3B6B-450b-B477-C59A196EAE34})
* [visaType](#{2ED602C6-C93C-41f3-8A02-10F0CAD0D64A})
* [vafNumber](#{6DEB5776-59E6-4645-9566-65EC62A36330})
* [Country](#{92EBA9B9-48C2-4082-9FE5-603977BD6846})
* [RegionOfCountry](#{65D869DB-19EE-4886-98BA-E579C39C4A68})
* [Address](#{C90267B5-77A3-4b79-BD0D-7C50C3F4C333})
* [associatedPersonName](#{022535DE-2100-420b-B4BC-10465DEEEC3C})
* [IndividualDocument](#{0F327324-6B4E-40b1-B96B-97A334BA5E4A})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [idOnCard](#{92D9B068-F8D4-4cbc-AD57-1DA39D5CC1C7})
* [documentIdentifies](#{2F8738A6-5EBA-4d80-980B-AA9E6F28B81A})
* [ParticularPeriod](#{2173F463-524C-457c-B106-51322F64F122})
* [IndividualDocumentID](#{D68F4E10-957A-4e98-8447-8F2768940DA7})
* [Nation](#{6AE6F8A5-F427-4ea6-BABD-5720F07430F5})
* [Gender](#{8B4DB18E-DF46-4419-B0ED-0159A25F2319})
* [ClassOfTravelVisa](#{2BADCB50-7A19-4d7b-A46E-8369F8B00D57})

IdentityDocuments are IndividualDocuments that can be used to authenticate the identity of their bearers. 

### <a id="{12F41073-A280-42a2-A83B-A299C85B78F4}"></a>Location
![Location Diagram](Images/EAID_12F41073_A280_42a2_A83B_A299C85B78F4.png)

#### IES elements in this diagram:

* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [Country](#{92EBA9B9-48C2-4082-9FE5-603977BD6846})
* [ISO3166_1Alpha_3](#{B92D79E2-9E7D-4df7-8D38-3D884AA09AD2})
* [GeographicFeature](#{7EEE1EF7-C814-4eee-85B3-F48698FD52B6})
* [RegionOfWorld](#{18C405CE-CC09-4e02-A44D-0FB00C6F6B37})
* [RegionOfCountry](#{65D869DB-19EE-4886-98BA-E579C39C4A68})
* [Address](#{C90267B5-77A3-4b79-BD0D-7C50C3F4C333})
* [Facility](#{9CD2C1B1-85B1-4579-9376-07827AD68461})
* [Port](#{57860A04-0128-4c7e-9BFD-83D3BA432F8C})
* [Airport](#{82E3793F-D0D1-40ca-927C-7A6FEF913503})
* [UN_LOCODE](#{AEA785BB-B625-41aa-8738-FB0F3726A281})
* [IATACode](#{AA530BCE-02F2-4195-A431-573D13A5B41C})
* [ICAOCode](#{239A3A0C-183C-432f-9147-7259C9573AA2})
* [GeoIdentity](#{87251DA1-7293-445e-987F-F13E331B6BDF})
* [What3words](#{B2262900-BF01-4691-8DE1-46A726A6D1CB})
* [TOID](#{79D9049D-E63F-4c94-B348-49506A75B9F8})
* [PostalCode](#{6A0385E2-3FB1-4a42-A254-BC382D92E27A})
* [FirstLineOfAddress](#{8B6DD87E-3D76-4836-9201-1244B80CDC69})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [inLocation](#{463F9B14-2D14-4364-B4F0-658A20DFCBFA})
* [addressRegion](#{3E452516-2523-4a86-974D-1D2251057E6E})
* [regionCountry](#{B3B6D7F3-F5B0-49d6-886F-F5AF7C56F041})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [PlaceName](#{37DB1A2C-9382-4dac-8AE8-9DEC5A337E16})
* [RealEstate](#{8E0DF17F-34EE-43c6-8DA4-30F698384FD3})
* [Length](#{5C21DE93-329F-4209-87FF-19610CB0D367})
* [ValueInMetres](#{C8D4C3CB-16C2-44a7-B709-35CEBF219BF0})
* [Altitude](#{51B6F4C5-0DA3-437d-9507-38514BC2ABCD})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [LineOfAddress](#{E0D8895D-2230-4c80-8B06-351581C53436})
* [RadioCoverageArea](#{7A2CC7C7-6B82-4751-BDBE-A770B3AFBBEB})
* [RadioMast](#{F02CFF55-12A7-4308-9A60-E2353DE5BE58})
* [CellularBaseStation](#{9D4A1395-8687-4f0b-BC5D-61A756210B4D})
* [radioCoverage](#{3B5E5043-30C2-4e67-86C8-F59F55AEBA90})
* [MapGridArea](#{18A66904-823F-471d-A465-65ECD2D69867})
* [OSGridReference](#{697EAA12-8FD3-49e0-A4A2-A045B4570550})
* [Easting](#{A4502460-54B7-446b-A9AA-003B49F9682B})
* [Northing](#{09649FE9-DDD7-4493-B9EC-7A716B0FC616})
* [GeoRepresentation](#{A8C07233-5D62-4ad4-B405-2D15CFC37497})
* [GeoJSON](#{417C1F4E-6A5D-4631-B275-8E982252791A})
* [ISO19125-WKT](#{22B79CFD-DEDA-42e1-8864-E8421D36CF19})
* [GML](#{AE59CB88-3178-4bad-9F43-1276337C7944})
* [GeoPoint](#{9A9467C3-D5FC-4964-8943-FE63ADF38914})
* [isCentroidOf](#{44ADC197-D9FA-4889-B6AF-929C3546F4A0})
* [Latitude](#{BD14EF81-DDBC-4bdf-BC40-E5FAE937ADA6})
* [Longitude](#{B2C5522F-EA60-455a-B00F-9CC87A76E5B0})
* [PointOnEarthSurface](#{A11A426E-ED15-4aaf-B9A5-02A4060533AA})
* [PartOfFacility](#{3EFEA421-6B88-4e51-9B20-4FFA22E8C5CA})
* [RoomNumber](#{0B2564A8-9A95-4164-BB49-01900DD530AD})

Locations are physical chunks of the earth (and usually the airspace above) - i.e. they are defined by their extent. 

The model is intended to be used hierarchically - e.g. an Address should be part of (inLocation) a RegionOfCountry which should be part of (inLocation) a Country, etc. 

### <a id="{8BE1A4EF-AD1D-4e9f-8681-AB9C658DA4D6}"></a>Online
![Online Diagram](Images/EAID_8BE1A4EF_AD1D_4e9f_8681_AB9C658DA4D6.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [OnlineAccount](#{E95170B9-2599-46dc-BEDC-012B08F09D43})
* [OnlineService](#{27BEFD0A-B30B-47db-B863-13E48D1172F9})
* [Webpage](#{79098C74-E063-4c45-886D-D0B88A48E954})
* [onlineAccountProvider](#{2CF1B157-A2F6-41c8-8A87-7B82EEB71F40})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [onlineServiceProvider](#{DEE1404A-AAC3-4d46-9BA3-8E097A55C7F5})
* [onlineServiceType](#{2C9CEF7F-FA9A-4a0e-9E2C-AC3D3EB51D5C})
* [URL](#{C23AB49C-0734-45b7-A383-8EEA305CDBE4})
* [WebResource](#{46D508B4-F1CC-45d7-9E4B-BA8A3C88D82A})
* [uriScheme](#{D97141BD-F6CF-4b10-B4E5-B1ECF6DF5178})
* [ScreenName](#{8C1321B7-8686-4a21-B99A-6C4A98B411A7})
* [ServiceName](#{8F8428BA-8586-4e34-9C75-FBA7A647B8EA})
* [uriSchemeName](#{AAA8DE3D-31D8-4c1e-B114-72E8B37D6CAA})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Username](#{9D703CE2-DED0-4aba-BE21-474781670297})
* [OnlineArtefact](#{54500458-51CF-46b5-A5A3-14B1D5C7F755})
* [onlineLikeOf](#{4A3F24C6-EEC9-48ce-93FB-26FF64E1268A})
* [holdsAccount](#{6314A9B0-4578-42a8-A553-1FDDF35AC7F1})
* [Account](#{31BFE794-924E-44e3-942E-ADC9ED19FBA1})
* [SocialMediaPage](#{3DC012C3-E273-4ec2-A462-CEDEB27262C1})
* [SocialMediaPost](#{4B3AE19C-6369-49d0-B7B5-949714FFFC95})
* [OnlineComment](#{FF216817-5B58-4db5-88C5-20AE6A466265})
* [OnlineLike](#{5B50EECC-45FC-4e5b-933E-51BC0FEE0FCD})
* [LiveCast](#{ECC6E85E-CB08-464d-81A4-BA3ECDCB784C})
* [onlineCommentOn](#{0A4C12E6-CA4C-43f1-9C6C-FBE23197975F})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [WebResourceState](#{3BE61CCF-DCD0-411d-9D43-5DEABF8381F2})
* [representationValue](#{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4})
* [informationContent](#{5BEE4248-DC98-4625-8553-3BB2171A1EDE})
* [ContentCategory](#{8CA5551A-EAEB-4145-A75F-2E7D7DAD5A57})
* [inCategory](#{D10B4B95-5BF1-4e3f-A2A8-8F52F045C31A})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [AccountHolder](#{C93379F2-6B01-4100-ABFA-BD26098AC1CB})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [ParticularPeriod](#{2173F463-524C-457c-B106-51322F64F122})
* [BoundingState](#{892345CD-9FA7-4982-978D-B6D3ABAE839C})
* [cookieOriginSite](#{24E8B958-284F-4be2-AACD-A7B2A94B97D4})
* [onlinePublisher](#{34F13F26-7C4E-451a-BDA0-62BA7738039F})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [hostedOn](#{F5C27E55-623E-4fa7-95C3-DD0A722D1035})
* [OnlineAccountState](#{4C0D1724-B820-4a87-AD36-08C0612CE21E})
* [Cookie](#{C81B6EAD-8494-45ca-928C-21CB6D395C39})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [cookieOnDevice](#{76D8EA41-E338-4db5-BB30-D642CF0F90EB})
* [ClassOfOnlineService](#{FBE0CFC1-43C4-47e2-9EFE-20E291A1697C})

This diagram covers the online aspects of IES. 

### <a id="{AD64CF62-6430-44f1-8943-DF7C22C31DFB}"></a>Organisation
![Organisation Diagram](Images/EAID_AD64CF62_6430_44f1_8943_DF7C22C31DFB.png)

#### IES elements in this diagram:

* [LawEnforcementOrganisation](#{15806699-2F00-4891-B2A0-8A211CEDFC10})
* [CriminalOrganisation](#{3CEFB37C-D5EE-4c9d-848D-C8E2DB206482})
* [AssessToBeTrue](#{7150208D-A02E-45ed-8279-44843F4DA897})
* [Assessor](#{80F9B97D-2C7F-4978-83A3-BE934DD4E1FF})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [OrganisationName](#{065C9B64-96E2-47f5-9769-E7942C1A208F})
* [Country](#{92EBA9B9-48C2-4082-9FE5-603977BD6846})
* [countryOfRegistration](#{D33498ED-B6A0-41ea-864F-CE95E2B1E010})
* [GovernmentOrganisation](#{0D042066-06C8-48d6-8387-500CF8EE2592})
* [CommercialOrganisation](#{1456439C-65C9-4a39-A743-09A7D0FBF248})
* [NotForProfitOrganisation](#{C2B4A066-E4A7-4cf5-BD1F-8381364F5D30})
* [IntelligenceAgency](#{F87E3B6F-5872-47eb-89F8-6642DD7C8237})
* [MilitaryOrganisation](#{492AB59A-342E-4d74-B85B-E6CA95BBC3B2})
* [TerroristOrganisation](#{6467A4EF-46BA-401c-A5C7-668BAFB6E228})
* [ReligiousOrganisation](#{2978340B-C4AA-4331-A68D-54A158798DAC})
* [EducationalOrganisation](#{F30D350C-848D-4b02-AEA5-86575CEEEFB3})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [Government](#{D62DDBB8-53FC-405a-BC43-89CA337563A0})
* [governedRegion](#{72DC3E90-53CE-434d-A5F3-89BDCE08A201})
* [RegionalConstituency](#{FC55D479-07C4-4d98-B48C-5032190E493D})
* [Nation](#{6AE6F8A5-F427-4ea6-BABD-5720F07430F5})
* [governedPopulation](#{917C549C-259F-4850-9CFD-35E05485BF63})
* [ISO3166_1Alpha_3](#{B92D79E2-9E7D-4df7-8D38-3D884AA09AD2})
* [OrganisationState](#{F3DB6A59-B2DE-4743-A9A8-7DA9CCC68638})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [NamingScheme](#{222534A5-25C8-4ecd-BE55-27DA1534D402})
* [inScheme](#{7EB9FE85-127C-4918-AC56-62E1BE1DE825})
* [hasName](#{C3A36E36-0C73-4af7-88E3-81C9243CE456})
* [Team](#{7B20EC37-6D66-4cd9-97DF-2A30B324C421})
* [Department](#{6C7891C7-E095-41f4-A894-AA0C6A22F5D2})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [Actor](#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B})
* [ActorState](#{7ED8BC7C-A85F-4ed5-AC6F-D640F2DF4B7B})
* [ClassOfEntity](#{D1B2FB30-36CA-4012-B85F-514E270BF541})
* [ClassOfResponsibleActor](#{9FC2431D-63A4-4e1b-8D31-2BCD125853D9})
* [ClassOfOrganisation](#{5B21F148-72C1-45e6-A3E3-F2D8B33729D3})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [OrganisationIdentifier](#{13865B40-B57D-44e7-9658-00C45C8175C8})

This diagram covers the Organisation aspects of IES. 

### <a id="{58BAB7ED-90B7-4ec5-82E5-02208AA0D521}"></a>Posts and Roles
![Posts and Roles Diagram](Images/EAID_58BAB7ED_90B7_4ec5_82E5_02208AA0D521.png)

#### IES elements in this diagram:

* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [Role](#{0066A327-D497-42e0-9F50-D988F522F4A5})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [OrganisationalRole](#{C0B7C4B2-C067-4ca8-A9FB-E82782889250})
* [hasRole](#{5C76592F-C47D-40ee-8D82-497962686D34})
* [ActorState](#{7ED8BC7C-A85F-4ed5-AC6F-D640F2DF4B7B})
* [Post](#{7C28E83C-1895-4901-ABF8-9D78C9C12C62})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [InPost](#{6C1949B5-B86B-4940-8912-9008CCD67150})
* [PostState](#{DB51B007-E3E8-431f-9C23-3C0A7E83FB11})

Posts are parts of Organisations. A PersonOrOrganisation can be in post for a period of time - i.e. there is a state of the PersonOrOrganisation (InPost) that is part of the Post. Note that this is part of the Post, not a state of it, as there may be more than one PersonOrOrganisation in a given Post at the same time.

Roles are also defined. These are ClassOfStates that are used to categorise a given state in terms of it role. 

### <a id="{282BC043-9277-4814-B98F-DFE588356C73}"></a>PaymentArtefact
![PaymentArtefact Diagram](Images/EAID_282BC043_9277_4814_B98F_DFE588356C73.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [PaymentArtefact](#{9882D901-1B22-4b89-81D1-031F840A20D0})
* [BankCard](#{848A9E0F-F3B4-47c3-AA7E-2FF6BE92170C})
* [StoreCard](#{686293F8-123B-478f-9A67-A6074937B528})
* [TravelCard](#{E1D8A09D-C260-4dd8-B6FF-C2FA8968A00B})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [paymentArtefactProvider](#{C793E699-C27B-49cc-9358-C4A0E17E609E})
* [validFromDate](#{6ACC2ACC-46F2-4a02-A3E7-D16BE8EB723B})
* [validToDate](#{680F737D-A8AB-4410-9F1D-FAD7BDC98447})
* [CreditCard](#{C2174205-C96F-4427-A401-19C1DEF0E4AF})
* [DebitCard](#{F0C846E7-76B9-4ab6-988E-3694C95818E7})
* [FinancialAccount](#{44DAC574-2A2E-44bc-ACD2-236811FA8D29})
* [accountForCard](#{7891E893-56DB-4d47-80B4-C78A667767F6})
* [issuerIdentificationNumber](#{5E353B12-2503-429f-A683-F7C77E0DFBAD})
* [branding](#{62675B63-9169-4f05-9993-E1B17540A6C1})
* [Country](#{92EBA9B9-48C2-4082-9FE5-603977BD6846})
* [hasCountryOfIssue](#{E7500475-8C4F-47a3-8AAB-C5679621FAE8})
* [areaOfCoverage](#{C6BA7464-C00E-4ff6-AE7B-9CE9D4E08FDF})
* [hasStatedAddress](#{0451B5D4-99CB-47a7-BB93-DF4DF6625837})
* [Address](#{C90267B5-77A3-4b79-BD0D-7C50C3F4C333})
* [associatedPersonName](#{022535DE-2100-420b-B4BC-10465DEEEC3C})
* [ParticularPeriod](#{2173F463-524C-457c-B106-51322F64F122})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [CardNumber](#{087F3453-B1D7-41e6-B79F-31B123ED0D68})
* [ClassOfPaymentArtefact](#{46144D4F-5A9F-432b-B533-26C0399DBB34})
* [cardType](#{CF6B72ED-DF58-42e1-A72A-1F047287B80D})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [RegionOfCountry](#{65D869DB-19EE-4886-98BA-E579C39C4A68})

PaymentArtefacts are used in transactions, and also sometimes to identify people.

### <a id="{D2CDD899-3080-4887-897F-63EA08B5E949}"></a>Person
![Person Diagram](Images/EAID_D2CDD899_3080_4887_897F_63EA08B5E949.png)

#### IES elements in this diagram:

* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [Characteristic](#{A7F266E8-B1CB-4b9b-8AF1-1EF2A7D8F5EE})
* [nationality](#{45CDA5C1-624D-4f2f-81F6-EF19300820A9})
* [PersonTitle](#{CA36058B-835C-48ef-944A-2507708ADA71})
* [hasGeneticGender](#{8914E7DF-443B-4a3a-A945-AAD11B82A86A})
* [hasReligion](#{6D1839A4-342A-4e34-823C-BDB392483048})
* [hasEthnicity](#{BC3185CE-53F4-45de-A6D4-DAC8343B4D1C})
* [hasLanguageProficiency](#{2065B9A0-DCAD-45be-9F0D-BD4398261A7F})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [BirthState](#{CFE53096-32FC-47c8-98BA-950EE6F988CB})
* [DeathState](#{F6173D27-D86D-40f8-A5B0-36DCCF85D396})
* [Nation](#{6AE6F8A5-F427-4ea6-BABD-5720F07430F5})
* [GivenName](#{A01A5045-B09C-4bea-8C96-881C29F2EE60})
* [Surname](#{B5A0C08A-39B3-4bd1-9D19-CE87E0F7DEBB})
* [Nickname](#{BA4B97EE-58E2-4796-949C-F62EAAAE56C9})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [PersonState](#{38F8B795-0BCE-4945-8C69-8678ED935C1A})
* [Religion](#{BD538820-CE91-4b9a-ADB8-C105FE0F2E7B})
* [hasIdentifiedGender](#{7640DBFC-B520-458c-A7C1-16651DDF217F})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [NamingScheme](#{222534A5-25C8-4ecd-BE55-27DA1534D402})
* [inScheme](#{7EB9FE85-127C-4918-AC56-62E1BE1DE825})
* [hasName](#{C3A36E36-0C73-4af7-88E3-81C9243CE456})
* [PersonName](#{F114F86C-3BA8-4be7-A686-A1D80002DF28})
* [Length](#{5C21DE93-329F-4209-87FF-19610CB0D367})
* [ValueInMetres](#{C8D4C3CB-16C2-44a7-B709-35CEBF219BF0})
* [PersonHeight](#{57060AD9-A6D7-496d-A2BF-22B930400EEE})
* [SubjectOfInterest](#{BFFBC847-AD87-458e-9A86-690D659EB48F})
* [Ethnicity](#{8AC946A4-4C03-463c-9F32-37EA8593988A})
* [Gender](#{8B4DB18E-DF46-4419-B0ED-0159A25F2319})
* [Language](#{82652FF5-258F-459c-BC7F-6DAC65E1ECA1})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [ISO639-3Code](#{ECFED94D-CC69-46b9-B09D-B282D5665787})
* [LanguageProficiency](#{EB73AB32-8232-4b58-8271-640DDDDCC7DE})
* [spokenLanguage](#{FA149043-EA61-4497-A036-589DA1FD312E})
* [ilrProficiency](#{471CF113-1728-47fd-A763-D1FA69226FC4})
* [Accent](#{63409D9A-1779-444a-BF04-23C03B3B2F72})

This diagram covers people, and people pretending to be other people (aliases). Most personal attributes belong to a PersonState as they are things that can change throughout the Person's life. The two whole-life properties that cannot changed are their ethnicity and their genetic gender.

Two special states are identified - birth and death which are bounding states for the whole life person and can be used to identify the location and date of birth. 

### <a id="{A98C6576-D0D5-42cf-AF90-89CC2B1F47F3}"></a>Ticket
![Ticket Diagram](Images/EAID_A98C6576_D0D5_42cf_AF90_89CC2B1F47F3.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [Ticket](#{0BC61540-2AFB-42e6-A845-79771EE0268D})
* [EntertainmentTicket](#{96989C30-99CC-4606-A8D4-DFD9421F0E34})
* [TravelTicket](#{6C669BEF-9267-4612-9F29-B28918B203F5})
* [eventDateTime](#{07DCD4FC-938C-438d-ABE6-F7F64E66A255})
* [Facility](#{9CD2C1B1-85B1-4579-9376-07827AD68461})
* [venueStatedOnTicket](#{3345AECA-925E-4bfc-820E-2294D5921E71})
* [allocatedSeatNumber](#{518E9B39-58C0-4e89-831D-B6099C3B9892})
* [authorisesAccessTo](#{A2DA918D-843C-43c9-A974-4795601E9D65})
* [Port](#{57860A04-0128-4c7e-9BFD-83D3BA432F8C})
* [TheatreTicket](#{5CD50268-582A-426b-B4CC-F6EE308B84A3})
* [CinemaTicket](#{7E0C25C9-DD3A-463e-A481-7CA4EA4AC8C5})
* [FootballMatchTicket](#{DA626F73-5748-47db-813F-E1813577F41B})
* [ConcertTicket](#{8FF9DE7F-137B-4a03-AB24-7D84FCFB99C0})
* [FlightTicket](#{3A9A1BA9-465F-4f6d-BD55-9F3F8AE40AE0})
* [TrainTicket](#{A8715447-3583-45d0-9550-625CF96B3E2E})
* [FerryTicket](#{B2ED961F-245E-4e74-A32F-6B9CF1BBDF2B})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [associatedCarrier](#{2E464C7F-FC0B-4dcc-9B1C-5DCA87B4CE3A})
* [issuingAgency](#{74D86486-8E18-474a-8930-B92E759BBE06})
* [associatedPersonName](#{022535DE-2100-420b-B4BC-10465DEEEC3C})
* [ticketDepartureLocation](#{952E5981-257F-429e-9F22-8D2E3B9282C7})
* [ticketArrivalLocation](#{A4906B5E-8718-404e-8EEF-20AE29106383})
* [validFromDate](#{6ACC2ACC-46F2-4a02-A3E7-D16BE8EB723B})
* [validToDate](#{680F737D-A8AB-4410-9F1D-FAD7BDC98447})
* [EntertainmentEvent](#{78C33499-CD14-43cb-82AE-93A0F8CF022B})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [IndividualDocument](#{0F327324-6B4E-40b1-B96B-97A334BA5E4A})
* [IndividualDocumentID](#{D68F4E10-957A-4e98-8447-8F2768940DA7})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [TravelService](#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74})
* [ParticularPeriod](#{2173F463-524C-457c-B106-51322F64F122})

Tickets are IndividualDocuments that authorise access to Events - e.g. travel and entertainment.

### <a id="{6D8B1DC4-4361-4edb-818F-AC96863555AD}"></a>Vehicle
![Vehicle Diagram](Images/EAID_6D8B1DC4_4361_4edb_818F_AC96863555AD.png)

#### IES elements in this diagram:

* [Vehicle](#{3B916F09-F3F4-43e9-9C84-99009C685396})
* [RegistrationNumber](#{1E784B9C-1A5D-4035-B134-67A758FB869D})
* [RoadVehicle](#{830B2164-E880-4bef-A62C-B38CEB6A824D})
* [Aircraft](#{01A64A84-7A14-45a5-AAF2-F1AA614D5F30})
* [Ship](#{14098560-1FF3-4599-B9A5-41167861538B})
* [make](#{E0036B31-8D73-4268-8959-6E9A5EE55BB2})
* [VehicleName](#{9D24B4BE-2AD4-42d6-A906-8F6EFDA23EC5})
* [Country](#{92EBA9B9-48C2-4082-9FE5-603977BD6846})
* [countryOfRegistration](#{D33498ED-B6A0-41ea-864F-CE95E2B1E010})
* [VehicleState](#{D3275233-7381-483e-B2D2-77F13D73A52E})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [ModelOfDevice](#{7A879268-33C2-4f2b-8928-9E78AFF01E69})
* [DiscontinuousState](#{52DB371E-71AC-4812-B3CF-0FD7D73F1BB0})
* [Parked](#{B6A503E5-3FC4-4a45-8DC0-994EA31A895A})
* [UsuallyParked](#{FCE0D994-4838-48fa-A274-57DB092A2960})
* [AssetState](#{CA196722-9531-4eb4-A8CF-B9A5145CDCFD})
* [VehicleIdentificationNumber](#{AC9AB7B0-6C38-4b08-B2B9-CAA8486F0F4B})
* [Colour](#{B10D22FB-1D6A-47c9-B1C0-E870D43A5C52})
* [ClassOfDevice](#{09F9136C-9069-47ec-A58E-FC26CF9BA55E})

A means of transportation � e.g. car, aircraft, ship.

### <a id="{D97110D9-791E-4e88-A92B-5139286E5F05}"></a>All Entities
![All Entities Diagram](Images/EAID_D97110D9_791E_4e88_A92B_5139286E5F05.png)

#### IES elements in this diagram:

* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [CommunicationsDevice](#{32EB46A5-0FA4-44e9-A9E9-9424E80BDE91})
* [IndividualDocument](#{0F327324-6B4E-40b1-B96B-97A334BA5E4A})
* [FinancialAccount](#{44DAC574-2A2E-44bc-ACD2-236811FA8D29})
* [IdentityDocument](#{BDF4EBD9-7F41-4d90-91A7-571177330C1B})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [OnlineAccount](#{E95170B9-2599-46dc-BEDC-012B08F09D43})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [PaymentArtefact](#{9882D901-1B22-4b89-81D1-031F840A20D0})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Ticket](#{0BC61540-2AFB-42e6-A845-79771EE0268D})
* [Vehicle](#{3B916F09-F3F4-43e9-9C84-99009C685396})
* [WebResource](#{46D508B4-F1CC-45d7-9E4B-BA8A3C88D82A})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Account](#{31BFE794-924E-44e3-942E-ADC9ED19FBA1})
* [CommunicationsAccount](#{8300451C-1DF9-4545-9174-D8AA69C58CCD})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [RealEstate](#{8E0DF17F-34EE-43c6-8DA4-30F698384FD3})
* [AmountOfMoney](#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8})
* [Religion](#{BD538820-CE91-4b9a-ADB8-C105FE0F2E7B})
* [System](#{F682A265-1AFE-4287-A9CD-0D4C83F54C52})
* [Actor](#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B})



### <a id="{2CE240E2-1CC5-440e-B8BD-53DC6CFDF831}"></a>
In IES3 there was "User of" which connected a person to an OnlineService. In IES4, we use <i>hasAccessTo.</i>

As with "User of" this is a statement of occasional use (or access to) rather than a specific event.

For a single use of the account, the Account is related to an instance of a PersonState. To show ongoing (regular) account use, the instance of the PersonState should also be an instance of DiscontinuousState

### <a id="{A18A0572-BD13-48ea-AB51-0F14910EE79B}"></a>
The names relationship is used to apply a Name to any ExchangedItem (including a Person)

### <a id="{64C3BA25-D454-44ab-92FB-B556D3F0C584}"></a>
In IES3, AliasName was just an attribute of a Person. However, aliases are much more complex than this, and can have associated passports, etc. just like a real person.

Also, more than one Person may play the role of the Alias over time.

### <a id="{18C66463-11B9-4b80-B401-0F31AE856802}"></a>
The birthDateTime, deathDateTime, locations, etc. are now managed with states. The states have start and end times (a birth or death may not be an instantaneous thing) and can be related to Locations using the inLocation relationship. The stateOf relationship is used to link the states to the Person.

### <a id="{0067E48C-5E00-4350-965C-02171515379C}"></a>Entities : Document
See also: Document

### <a id="{D72C3B4C-D3A7-4d1c-9649-404268B44BCA}"></a>Entities : Identity Document
See also : Identity Document

### <a id="{0F5E052E-7103-44ed-AF91-1ECA6BFA002F}"></a>Entities : Person
See : Person

### <a id="{ED29A5AC-402F-44c5-AFC8-1D79F0CF54D3}"></a>IES v4 : Identifiers
See : Identifiers

### <a id="{484D67F7-1FE1-4e54-9B13-7AA48670208C}"></a>IES v4 : Identifiers
See : Identifiers

### <a id="{C5D2A38B-BA1C-4325-A60B-18E46C51366A}"></a>see: Assessment Diagram
See: Assessment

## <a id="{8CE69414-E291-4f34-B5C5-443FED062F40}"></a>Events


### <a id="{4C6AEF32-6360-4671-82E3-019DF67D2496}"></a>Events Dear Boy, Events
![Events Dear Boy, Events Diagram](Images/EAID_4C6AEF32_6360_4671_82E3_019DF67D2496.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [happensIn](#{60A37745-8DD5-4e4c-9A4C-6957F71AD971})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [isParticipationOf](#{DF9F6056-CCD4-41aa-9A86-536F6150EC25})
* [isParticipantIn](#{BAEA86D9-C90E-4f8d-96F5-A01BB0C49711})
* [takesplaceIn](#{5D13DE13-CAAC-4879-9237-D20A6846F4D8})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [EventState](#{FE668C24-D25C-4273-872A-EB77CB09341D})

An Event is an activity or incident involving one or more participants (i.e. Entities). The participating Entities are related to the Events via an EventParticipant subtype. To relate the EventParticipant to the Entity, use the isParticipationOf relationship. To relate the EventParticipation to the Event, use the isParticipantIn relationship. Rather than create sub-properties of these relationships for each type of EventParticipation, a simplified notation (UML Dependency - dashed line with arrow-head) is used in the Event diagrams to indicate the appropriate Events and Entities for each type of EventParticipation.

There are two key types of EventParticipant - Actor and ActedUpon. Actor relates a Person or Organisation to the Event they conduct. ActedUpon relates an Entity to the Event that has an effect upon them. These two EventParticipants generalise and replace a number of the participants specified in IES 3.x (see the specific Event subtypes for examples).

Locations of Events are handled with more precision in IES4. The happensIn relationship can be used to assert the encompassing Location for the whole Event - e.g. an arrest that takes place in Trafalgar Square. However, some Locations merely participate in the Event - e.g. departure and destination ports, weapon and target locations in attacks, etc. For this reason, happensIn should only be used when the Event takes place entirely within the envelope of the Location. This precision is necessary for interpreting Events in geo systems, timeline visualisations, etc.

### <a id="{5DF03A2C-F6DF-4433-82D5-7E5C14B6045C}"></a>Assessment
![Assessment Diagram](Images/EAID_5DF03A2C_F6DF_4433_82D5_7E5C14B6045C.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [Actor](#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B})
* [AssessToBeTrue](#{7150208D-A02E-45ed-8279-44843F4DA897})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Assessor](#{80F9B97D-2C7F-4978-83A3-BE934DD4E1FF})
* [assessed](#{669E3CD0-CD9D-496c-A711-ECDE3F589012})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [confidence](#{45FE24B3-B146-4199-B760-C1150CEF9AB2})
* [hmlConfidence](#{04F797E7-9B5C-48c5-A50D-A14CFF7725DE})
* [PossibleWorld](#{15E93B86-6969-47f2-8036-0B7B96E9BDA2})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [GroupOfItems](#{04C2111A-D958-4a95-9271-7208B849DDD8})
* [inGroup](#{C21D2CA2-6F42-4b7c-9092-8B8C5B7BAF9F})

The Assessment pattern breaks away from the usual IES EventParticipant pattern slightly. There is still an event (AssessToBeTrue) and a participant (Assessor) but the thing that is being assessed isn't necessarily a participant - it could be something intangible such as Class or relationship, so a simple owl:objectProperty is used to link the event to the thing that has been assessed to be true.

A high, medium, low rating must be provided for all assessments. Whilst it is realised that these values may have different meanings between various parties - e.g. medical, policing, intelligence, etc., there has to be some rough indicator, so hmlConfidence will have to be it. 

A further (e.g. more specific) confidence indicator may also be provided. IES does not mandate how that confidence is measured. 

This model also introduces (new to IES 4.1.0) the idea of a PossibleWorld (as used in ISO15926, IDEAS and Prof Matthew West's guide to high quality data models). A PossibleWorld is a scenario - something that may are may not have occurred, and encompasses a number of events and entities that would have existed in that world. The likelihood of a PossibleWorld is defined using AssessToBeTrue.

In the example shown, there are three scenarios. In scenario 1, Fred is assessed to have carried out the hacking alone. In 2, Barry did it alone. In 3, they both did it. Vladimir has assessed the scenarios with HIGH MEDIUM and LOW confidence. 

### <a id="{DF5AAB67-46EB-40a8-B96E-8F3B5382D145}"></a>Authorisation
![Authorisation Diagram](Images/EAID_DF5AAB67_46EB_40a8_B96E_8F3B5382D145.png)

#### IES elements in this diagram:

* [beginBoundOfClass](#{2C441F0A-635D-41ef-B8CC-96AA07958F8E})
* [endBoundOfClass](#{F8109922-1CB1-490d-BBB5-FD5B76E19FD1})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [EndToEndAuthorisation](#{D75F18D1-95D6-481b-84D5-F8D7F3A5A389})
* [AuthorisationStage](#{2D5069F2-FE77-477f-A607-FA6458E64173})
* [AuthorisationRequest](#{1D6BAE08-B8F1-4eee-928E-991B3B46EADF})
* [GrantOfAuthority](#{F5EAAEEE-C0B2-469f-9048-3E0731ED8342})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [AuthorisationReviewer](#{8E4CC036-C4C5-4222-8532-9B6C53EEC56E})
* [AuthorisationRequester](#{81BF6EA6-996D-4148-8F5D-8B41156637F6})
* [ClassOfEvent](#{4EA194C6-BBF9-45ab-85DE-5802D8C3A531})
* [requestedActivityType](#{132AFC03-7A64-45fa-9F87-93171BBFBE3D})
* [TimeBoundedClass](#{E7A659A5-9059-4ea5-8FAB-8A29AFC47D9A})
* [AuthorisedEventClass](#{057C04F9-EB8A-4e21-9CF8-2D98038570FB})
* [Actor](#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [allAuthorisedAgainst](#{97E2E16A-5D4C-41bd-AF32-8DF2057A35BA})
* [grantedActivityType](#{289608A2-3F9D-413a-98AB-25579C370924})
* [Authoriser](#{466DCDFB-B642-468b-A47A-E83291A86C6B})
* [AuthorisedActor](#{F69279D2-BA11-4a31-8739-0D91EF5B9BEF})
* [ParticularPeriod](#{2173F463-524C-457c-B106-51322F64F122})
* [Warrantry](#{CA2023C6-1677-4d24-A1E6-22BC4D595E6F})
* [Warrant](#{4CAD884A-1EA7-473d-9881-8B76EBF8526F})
* [WorkOfDocumentation](#{F0B48978-D4E4-45a4-8238-091A5B714D82})
* [AuthorisationDocument](#{8177A2FB-CA54-4dc5-9884-33FBA660B174})
* [RequestDocument](#{C0273975-049B-40f0-817C-DFBFA4A3E5CE})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})

The Authorisation Model (added in v4.2 of IES) is about capturing the end-to-end authorisation process from request, through grant of authority to act, through to the actions that take place under that authority. The primary need for this model is in Police warrantry, though the model is general and can be used for other forms of authorisation. 

The EndToEndAuthorisation is composed of (using isPartOf) the AuthorisationRequest and the GrantOfAuthority. Any other Events that occur under that authority should also be made part of the EndToEndAuthorisation - i.e. it encompasses not only the administration of the authorisation but also the actions that take place under it. 

The request and grant events are linked to the AuthorisedEventClass (or classes) they authorise - e.g. requesting authorisation to travel would mean the travel EventClass is then related to AuthorisationRequest via a requestedActivityType relationship.  It is usual for authorisations (esp. warrants) to be time-bounded. Hence, any AuthorisedEventClass will usually also be an instance of a TimeBoundedClass.

### <a id="{6D55C5E7-D9D9-454a-97C7-B682D9334D78}"></a>Observation
![Observation Diagram](Images/EAID_6D55C5E7_D9D9_454a_97C7_B682D9334D78.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [Observation](#{8CA40CCF-A099-49fd-80CB-CA6DA733FAB4})
* [Observer](#{C58A1AB4-19E2-48d0-B606-3BDFC5DD3860})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [Observed](#{CC05ABD0-7BAB-4484-8E8C-ED07C1AA3C93})
* [Actor](#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B})

The Observation pattern specialises the EventParticipation pattern. There is an Event (activity) of Observation, in which one or more Entities can be involved as Observer. Elements (Events or Entities) also participate as the Observed role.

The use of the EventParticipation pattern allows for the locations of Observer and Observed to be different.

### <a id="{C8EE24EF-889D-4e8f-96DE-CCBE47D4BE4F}"></a>Agreement
![Agreement Diagram](Images/EAID_C8EE24EF_889D_4e8f_96DE_CCBE47D4BE4F.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [happensIn](#{60A37745-8DD5-4e4c-9A4C-6957F71AD971})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [EndToEndAgreement](#{1B39630B-B00F-4def-9C65-48082C4AD2E0})
* [AgreementStage](#{422B4F1C-DA90-400b-8FFD-43C90B4F10F4})
* [Negotiation](#{FB2EA8AE-164A-4642-82E3-D2622DC6FCCB})
* [Ratification](#{31977608-5432-4d6f-AEE0-19838197C813})
* [AgreementExecution](#{93F71FAF-AEF4-4e41-8CEB-FC6447B20428})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [PartyToAgreement](#{AF57E842-9BF7-4f6e-B180-DDEACB0F5386})
* [Signatory](#{C55A12C9-CF85-4b7c-B422-1D41054E9570})
* [Negotiator](#{D4B25AAF-F083-45ba-8188-25DE9D86013D})
* [Treaty](#{59599C4B-F3DE-49a0-B76F-BE4CB1293CBA})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [Nation](#{6AE6F8A5-F427-4ea6-BABD-5720F07430F5})
* [RegionalConstituency](#{FC55D479-07C4-4d98-B48C-5032190E493D})
* [NonDisclosureAgreement](#{672C510D-8836-4a41-8921-C732DF430278})
* [RentalAgreement](#{F38D2E58-C29A-4e3c-93BF-C33800969720})
* [Renter](#{E2FC3A09-EC9D-4ab9-B273-A526CB511B5A})
* [RentalProvider](#{8ECC64A4-CED0-4122-AB54-64EA870837FC})
* [Rented](#{E5C65CAB-65BE-4502-8B46-5C5CC3C73B00})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [PoliticalAgreement](#{686C8BFB-6CB2-4185-9FCF-89D2D4BB3051})
* [TradeAgreement](#{54A4E900-7E8E-49fd-91F4-23ADDDF2DA60})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [AgreementName](#{7A750064-E711-4871-AFC3-39057342FB9E})

In IES4, Agreements are handled using a pattern of AgreementStages that form part of an EndToEndAgreement. 

### <a id="{6EEF4705-72CE-4979-90FF-1966940B7C35}"></a>Disagreement and War
![Disagreement and War Diagram](Images/EAID_6EEF4705_72CE_4979_90FF_1966940B7C35.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [Nation](#{6AE6F8A5-F427-4ea6-BABD-5720F07430F5})
* [RegionalConstituency](#{FC55D479-07C4-4d98-B48C-5032190E493D})
* [Disagreement](#{E73C74A9-B356-40a4-BDBB-40567592BBD0})
* [InDisagreement](#{F12D45EA-66D5-4016-BDF7-E1CD8F48CCF5})
* [War](#{D4F568F5-7BC4-489d-94BC-AE1305E5C0C2})
* [InternationalCoalition](#{AE70547D-8E7E-474e-B7FD-F0A81F470157})
* [AtWar](#{89953404-8A71-46ef-8F7B-90C12EE286FD})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [DeclarationOfWar](#{5E25DC95-E376-420f-9991-F5175476B386})
* [MilitaryEvent](#{8EA1764B-26BE-4a72-ADEF-385C4CD657C3})
* [MilitaryAttack](#{8787BE51-8FE0-4d76-97B4-608311434F5B})
* [Casualty](#{61D00F47-977E-43f6-BD30-77CBAAA74CC1})
* [WeaponLocation](#{B513F0D8-E527-4548-8453-D905775E3A4F})
* [TargetLocation](#{9BEF1C80-3823-4611-9349-AA1E11E41BE7})
* [OperationalEvent](#{59121C21-38E4-4224-8C2D-4D3E94A3A0D9})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [Attacker](#{73D38C0E-3291-4de9-8920-F37980CB3A9E})

IES3 listed disagreements and war in the event tables. IES4 has maintained these two concepts, making War a specialisation of Disagreement. There are two accompanying EventParticipations (inDisagreement and atWar) also.

### <a id="{2C2171E3-E7A6-4702-AD72-1E02B11AFAA7}"></a>Business
![Business Diagram](Images/EAID_2C2171E3_E7A6_4702_AD72_1E02B11AFAA7.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [BusinessEvent](#{94CEDBD1-8E3D-4cb4-8155-FBD621DA6A0D})
* [AccountAdminEvent](#{19E90CA4-F0EB-4245-826E-EDC278642B41})
* [OpenAccount](#{A8B06392-A9A3-4de4-93FB-24F08A546434})
* [CloseAccount](#{2A5450A7-5B26-4605-A109-5CB26DD9A70F})
* [UpdateAccount](#{E2D19BE1-B1BF-4e0b-8D44-AFFD739756BA})
* [holdsAccount](#{6314A9B0-4578-42a8-A553-1FDDF35AC7F1})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [accountProvider](#{0F9244C3-B2F5-4b8a-AED2-54B7FDAB9578})
* [FinancialAccount](#{44DAC574-2A2E-44bc-ACD2-236811FA8D29})
* [MoneyTransfer](#{D94ED70F-8CCA-4c6e-8AE5-65450BBA62D7})
* [transferType](#{9574377B-6752-4317-94DC-E075C408442D})
* [transferValue](#{A9D01DAB-281E-48ae-BB33-8518701ABBDE})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [SendingAccount](#{F7172876-85F6-4d29-B11F-A1B36616416A})
* [ReceivingAccount](#{25965198-3FE0-4bb9-BCA9-808E15A3EE49})
* [AdministeredAccount](#{D779F547-C1FB-4d48-9BB8-CB37B9D2F82C})
* [happensIn](#{60A37745-8DD5-4e4c-9A4C-6957F71AD971})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [Account](#{31BFE794-924E-44e3-942E-ADC9ED19FBA1})
* [AmountOfMoney](#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8})
* [AccountHolder](#{C93379F2-6B01-4100-ABFA-BD26098AC1CB})
* [BankBranch](#{02E3C3B8-8650-4867-8390-823E4B3360E6})
* [ClassOfMoneyTransfer](#{F1AACA77-BA24-41cb-9AB8-7AF9C1B9971D})

The BusinessEvent model is really about Events that affect accounts - opening them, closing them and updating them. It also covers money transfers between FinancialAccounts.

### <a id="{6780105E-2091-491e-AEBF-C68E03B0074E}"></a>Attendance
![Attendance Diagram](Images/EAID_6780105E_2091_491e_AEBF_C68E03B0074E.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [EntertainmentEvent](#{78C33499-CD14-43cb-82AE-93A0F8CF022B})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [CoLocation](#{3524D10D-D9B0-416d-ADED-D5AAEB99DD09})
* [happensIn](#{60A37745-8DD5-4e4c-9A4C-6957F71AD971})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Presence](#{8404464D-3904-4c59-AE0E-B3FAFB46AC4E})
* [CheckIn](#{87308A03-5C79-4d94-99E1-660042AC7929})
* [IdentityDocument](#{BDF4EBD9-7F41-4d90-91A7-571177330C1B})
* [IdUsedInCheckIn](#{F481C966-058B-4caf-A427-9E492CAD0D63})
* [TicketUsedInCheckIn](#{92470C59-DFA6-47f7-A525-50CDABC8F852})
* [Ticket](#{0BC61540-2AFB-42e6-A845-79771EE0268D})
* [Meeting](#{6445E51F-3DDF-4dcf-ABDF-3ED123D53188})
* [MeetingChair](#{B499C172-310D-4c5f-BA92-93B1C7874EEB})
* [Name](#{7D7CC966-56EB-4220-A650-A993E598F2E2})
* [NamingScheme](#{222534A5-25C8-4ecd-BE55-27DA1534D402})
* [inScheme](#{7EB9FE85-127C-4918-AC56-62E1BE1DE825})
* [Attendance](#{626D5F2C-9153-40f4-9F2A-393B6DB072D3})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [hasTheme](#{654CB83B-75CF-4940-A2CF-C7820141C5AE})

The attendance model in IES4 introduces some new concepts form IES3 - Meeting and CheckIn. These events weren't explicitly called out in IES3 - being colocated doesn't necessarily mean people are meeting.

### <a id="{D25935BF-2B8F-4315-A858-1FC4DC691DF3}"></a>Communication
![Communication Diagram](Images/EAID_D25935BF_2B8F_4315_A858_1FC4DC691DF3.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [Communication](#{6698805F-F492-4f1f-954C-E1EB3C53E148})
* [Message](#{70AEDFC7-2B17-43d8-BF49-B5ACF8812317})
* [SMS](#{4C19E163-710B-4ccb-9F1C-569F8E348BDC})
* [InteractiveCommunication](#{6D5E11EE-C61A-4e38-913F-BBAF2A34A288})
* [VoiceCall](#{F186E39F-A251-4b84-85E9-577C7290F6D9})
* [messageContent](#{E1A85BEA-C374-4727-A189-E536BA248D98})
* [CommunicationsIdentifier](#{A82378B9-9774-46b9-9845-CC75BE882F06})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [Sender](#{44C93DB5-8DFA-4585-9060-EEC789E0A5AC})
* [Recipient](#{AAC709FB-0B88-4517-B5BB-FE2320992073})
* [Caller](#{03DDC2F5-F961-47c2-B8F8-B27A752AEC34})
* [Callee](#{F50BAD6D-EBE0-4fd8-B54C-3E24A62491A6})
* [PartyInCommunication](#{A5713B2C-E098-4dd2-BD46-42DA51899FEA})
* [PersonInCommunication](#{0383D09B-8C40-417d-8C1A-75220EAF496E})
* [PersonState](#{38F8B795-0BCE-4945-8C69-8678ED935C1A})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [TeleConference](#{6EAC8930-3D16-4e44-9706-989BDF6564A5})
* [VideoConference](#{1ED09A3D-7EE9-4b7a-8F0B-8590023C9F81})
* [ConferenceParticipant](#{5C76FE3F-FE06-4abc-B495-0D4F35FB5252})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [ServiceProvider](#{496683C9-EB89-46ac-87D0-4864F1B54ED4})
* [ConferenceHost](#{B59AB165-6D9C-423f-9CB2-85B4E1B37D93})
* [dialInNumber](#{73F2438B-77F5-49ee-B70D-84D5D50B378F})
* [DeviceState](#{6107EEA5-1A13-46e4-83FB-14740437B814})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [DeviceInCommunication](#{0073BD83-64CB-433c-BF4D-A6BB01862F14})
* [CommunicationsDevice](#{32EB46A5-0FA4-44e9-A9E9-9424E80BDE91})
* [CommunicationsAccount](#{8300451C-1DF9-4545-9174-D8AA69C58CCD})
* [CommunicationsAccountState](#{20BB42F0-3F2D-4bb7-88DD-F4D05377D59B})
* [hasRegisteredCommsID](#{E076AFB8-F6F8-4b06-82B3-7ED568D1EE73})
* [AccountInCommunication](#{942FBF46-A7EF-432b-99DD-1E0E3E874C21})
* [Account](#{31BFE794-924E-44e3-942E-ADC9ED19FBA1})
* [OnlineAccount](#{E95170B9-2599-46dc-BEDC-012B08F09D43})
* [TelephoneNumber](#{168D7B01-CD70-4f83-A414-19B6ABEB961C})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [hasTheme](#{654CB83B-75CF-4940-A2CF-C7820141C5AE})

The Communication Event consists of two or more PartyInCommunication events - each being an "end" of the communcation. A PartyInCommunication may involve the participations of people, accounts or devices. 

In the example shown, Fred calls Brenda (we know they were both on the call). We also know which phone Fred used, but we don't know for Brenda, so all we can do is assume she has a US phone account that had a particular number.

### <a id="{8DB48415-57E7-47d8-A6EE-97AD59CCA8B9}"></a>Lifecycle
![Lifecycle Diagram](Images/EAID_8DB48415_57E7_47d8_A6EE_97AD59CCA8B9.png)

#### IES elements in this diagram:

* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [LifecycleEvent](#{FA07AB7A-0EE8-4258-BE8B-260F9A1192A7})
* [Create](#{AF60517B-E4EF-48ca-BE0F-56E0A89660FD})
* [Modify](#{3EF09CE4-79B0-42be-9AA1-12B97611BF2B})
* [Destroy](#{27000BBA-F3F9-4355-B466-92CE04477C9B})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [FoundOrganisation](#{5054AFA3-8FC7-449d-93EE-C69B9D2AE118})
* [Forgery](#{78686D99-2AAC-4f5b-8EE0-456BDCC6F99E})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [happensIn](#{60A37745-8DD5-4e4c-9A4C-6957F71AD971})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [preModificationState](#{4E954855-D50A-42ab-9401-4B1C890542AD})
* [postModificationState](#{2B02EF33-E12A-42ec-B047-533F6D8F159D})
* [Customer](#{76689446-5969-49d3-8E7E-A92C86C244D5})
* [Created](#{46DE5D1F-B3CE-4858-A6D1-64A0B891A00F})
* [Destroyed](#{E70CA8CD-51DC-4f77-982C-C233F9493FF9})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [Creator](#{850DB6D5-C8E8-4aa8-87A0-4E7680FF854A})
* [Destroyer](#{C029299D-5946-48dd-94CB-80EC23A56300})
* [Modifier](#{21A341AE-9A38-4f45-BCB5-B29B02DC1B90})
* [BoundingState](#{892345CD-9FA7-4982-978D-B6D3ABAE839C})

Lifecycle Events cover the creation, modification and destruction of things.

Some of the roles originally in IES3 have been simplified in IES4 (see table at the bottom of the diagram)

### <a id="{70DAFAB2-F28A-4822-A211-00731AD90D62}"></a>OnlineEvent
![OnlineEvent Diagram](Images/EAID_70DAFAB2_F28A_4822_A211_00731AD90D62.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [OnlineEvent](#{24499751-7D9B-4f2e-B880-8D5BC4FCEF30})
* [Logon](#{43CDB7F8-E77E-4eba-A92E-C6A74AF954CA})
* [Notify](#{15EF63E0-1223-4874-A2D4-43F75ACF5315})
* [OnlineAccount](#{E95170B9-2599-46dc-BEDC-012B08F09D43})
* [OnlineService](#{27BEFD0A-B30B-47db-B863-13E48D1172F9})
* [OnlineAccountInUse](#{BCFD5BED-785D-4c5d-B004-2C8A5C7B40C3})
* [onlineAccountProvider](#{2CF1B157-A2F6-41c8-8A87-7B82EEB71F40})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [Account](#{31BFE794-924E-44e3-942E-ADC9ED19FBA1})
* [PersonState](#{38F8B795-0BCE-4945-8C69-8678ED935C1A})
* [DiscontinuousState](#{52DB371E-71AC-4812-B3CF-0FD7D73F1BB0})
* [OnlineArtefactInEvent](#{FE21E354-7770-4e6b-A7EA-E012F759E835})
* [OnlineContentCreation](#{DB70D7EE-5076-4eb2-950B-63C71A3C8859})
* [Logoff](#{8010625F-BA25-457a-93CF-7EC1E99261D7})
* [OnlineContentEvent](#{2176DEAE-6B5A-4906-AE37-FC76B0A50C0D})
* [LifecycleEvent](#{FA07AB7A-0EE8-4258-BE8B-260F9A1192A7})
* [Webpage](#{79098C74-E063-4c45-886D-D0B88A48E954})
* [OnlineArtefact](#{54500458-51CF-46b5-A5A3-14B1D5C7F755})
* [SocialMediaPage](#{3DC012C3-E273-4ec2-A462-CEDEB27262C1})
* [SocialMediaPost](#{4B3AE19C-6369-49d0-B7B5-949714FFFC95})
* [OnlineComment](#{FF216817-5B58-4db5-88C5-20AE6A466265})
* [OnlineLike](#{5B50EECC-45FC-4e5b-933E-51BC0FEE0FCD})
* [LiveCast](#{ECC6E85E-CB08-464d-81A4-BA3ECDCB784C})
* [Created](#{46DE5D1F-B3CE-4858-A6D1-64A0B891A00F})
* [Create](#{AF60517B-E4EF-48ca-BE0F-56E0A89660FD})
* [CreatedContent](#{1EBC6375-B26C-4506-B4DE-85B74E476362})
* [DeviceOnline](#{700BC564-35E1-4921-8759-5DAFA51B4E83})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [Message](#{70AEDFC7-2B17-43d8-BF49-B5ACF8812317})

OnlineEvents are activities such as logging in, notifications, etc. 

### <a id="{852CA74F-2858-4145-908D-5DCEB1AA0589}"></a>Criminal
![Criminal Diagram](Images/EAID_852CA74F_2858_4145_908D_5DCEB1AA0589.png)

#### IES elements in this diagram:

* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [typeOfCriminality](#{07BDCB73-1CDA-4057-9D7E-EC088D304B04})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [CriminalActivity](#{43E58528-16E4-48b3-8F13-10500879EA83})
* [Hacking](#{2AC7FDAB-7BB8-41ee-B558-AEBFE01274F2})
* [TerrorAttack](#{F8454637-80DD-44a7-AD91-6DECE44F0171})
* [Perpetrator](#{D625B538-7D72-4d7d-BA50-D79712A264ED})
* [Victim](#{3B47FCD0-E7D1-4b2b-BC07-C96D3F07ABC3})
* [Forgery](#{78686D99-2AAC-4f5b-8EE0-456BDCC6F99E})
* [Stalking](#{9B232210-27A3-410a-A713-EFDE7922C61C})
* [CyberStalking](#{8CF52FB7-69F2-4ef2-8074-FB90EE924139})
* [OnlineAccount](#{E95170B9-2599-46dc-BEDC-012B08F09D43})
* [OnlineAccountInUse](#{BCFD5BED-785D-4c5d-B004-2C8A5C7B40C3})
* [MaliciousAccountUse](#{F0C08ADE-7EE5-4392-9877-5FD8FB4076E9})
* [Created](#{46DE5D1F-B3CE-4858-A6D1-64A0B891A00F})
* [ClassOfCriminalActivity](#{69868D83-C3BD-4877-AB5C-374B4C6F4A7E})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [OffenceCode](#{66A24EF2-F417-46c7-A68D-D4540260F64F})

Criminal Activity covers any Event that involves breaking the law

### <a id="{460B1D00-10CB-4f93-A518-F2A96AF54CF7}"></a>Law Enforcement
![Law Enforcement Diagram](Images/EAID_460B1D00_10CB_4f93_A518_F2A96AF54CF7.png)

#### IES elements in this diagram:

* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [happensIn](#{60A37745-8DD5-4e4c-9A4C-6957F71AD971})
* [LawEnforcement](#{3876B81C-E316-4e11-A6C4-8024E52F769B})
* [Arrest](#{D8D7184C-2F7B-4a5d-AA8F-7EE7B5A04F94})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Witness](#{9C9ED058-4BB5-43d0-A311-FF7A532ED6D6})
* [Prosecution](#{024133FE-9D0B-4e5d-A97D-A34B5EA01C41})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [Prosecutor](#{ABDC5FD5-3281-4cd5-A9B0-188292D8C6B7})
* [ArrestingOfficer](#{5B3F41C3-91CC-442f-A4F8-615E77751734})
* [Prisoner](#{885EA1C2-29D7-4b7c-B479-D43E4F77B5BD})
* [Incarceration](#{06972684-050B-4f36-9393-B8790D510F5C})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [IncarceratingOrganisation](#{321CB600-140F-452f-96B7-640DE8289ECF})
* [IncarcerationFacility](#{B5C15382-451A-4446-BBE6-C67FBDB04402})
* [Accused](#{A4D8A62A-DC98-410c-80D2-57C98C1E95C0})
* [Arrested](#{B870A3B5-32FA-4aaf-86F1-7DB674585F3A})
* [Facility](#{9CD2C1B1-85B1-4579-9376-07827AD68461})
* [RealEstate](#{8E0DF17F-34EE-43c6-8DA4-30F698384FD3})

In IES3, law enforcement came under OperationalEvent, but has been separated out for IES4. 

### <a id="{45F6DECC-1D67-4037-83DE-0047C8815EF5}"></a>Operational
![Operational Diagram](Images/EAID_45F6DECC_1D67_4037_83DE_0047C8815EF5.png)

#### IES elements in this diagram:

* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [happensIn](#{60A37745-8DD5-4e4c-9A4C-6957F71AD971})
* [OperationalEvent](#{59121C21-38E4-4224-8C2D-4D3E94A3A0D9})
* [IntelligenceOperation](#{A0A9CD13-A4B4-415b-9187-64C9B72E2F4E})
* [missionPurpose](#{A6DED556-12B8-45b7-A69C-A6A3D813269B})
* [Surveillance](#{AD0F575E-5C28-4594-B346-50E9F22C2A8E})
* [IndividualDocument](#{0F327324-6B4E-40b1-B96B-97A334BA5E4A})
* [EvidentialPhotograph](#{AFFFF30F-B274-4466-B0F2-D2A6A78E1832})
* [SurveillanceWarrant](#{A86EC717-55AF-456c-BEC4-E1BA295D0227})
* [Investigation](#{2912E599-436D-4b79-B94F-02FA2319F201})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [MilitaryEvent](#{8EA1764B-26BE-4a72-ADEF-385C4CD657C3})
* [Reconnaisance](#{88E8F5E6-AFE5-4376-8112-EC294A673923})
* [SubjectOfOperation](#{11F2A275-650F-407d-8E86-F99DDEF4AAAF})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [Operator](#{6730B57A-3E53-4bd2-B784-78C4FB239DBF})
* [Investigator](#{3525F314-87ED-43c8-9A84-68EDCD203B30})
* [LeadInvestigator](#{E1AF7AFE-FA2F-40f7-88A3-CA6988BC2E0D})
* [Arrest](#{D8D7184C-2F7B-4a5d-AA8F-7EE7B5A04F94})
* [ClassOfEvent](#{4EA194C6-BBF9-45ab-85DE-5802D8C3A531})
* [ClassOfOperationalEvent](#{64CE6FEA-7B05-4813-BD55-D56C02A54486})
* [ClassOfCriminalActivity](#{69868D83-C3BD-4877-AB5C-374B4C6F4A7E})
* [typicallyTargets](#{AE6D5097-F555-48af-AFBA-88ECAA31BFF3})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [hasTheme](#{654CB83B-75CF-4940-A2CF-C7820141C5AE})

Operational Events are conducted against targets (SubjectOfOperation). They specialise into IntelligenceOperations and MilitaryEvents.

### <a id="{F919DBEC-CE53-478f-8EEA-FB151D7B1102}"></a>Political
![Political Diagram](Images/EAID_F919DBEC_CE53_478f_8EEA_FB151D7B1102.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [PoliticalEvent](#{3A0E6FDD-5B3B-4092-9549-C05E8A5FED41})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [PoliticalAgreement](#{686C8BFB-6CB2-4185-9FCF-89D2D4BB3051})
* [TradeAgreement](#{54A4E900-7E8E-49fd-91F4-23ADDDF2DA60})
* [PoliticalAnnouncement](#{53D5957B-E4B6-4cbb-8CE9-887F7152820F})
* [DeclarationOfWar](#{5E25DC95-E376-420f-9991-F5175476B386})
* [PolicyAnnouncement](#{345E8F46-AC41-452b-B2F9-694DBED556FD})
* [Nation](#{6AE6F8A5-F427-4ea6-BABD-5720F07430F5})
* [RegionalConstituency](#{FC55D479-07C4-4d98-B48C-5032190E493D})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [DeclaringParty](#{82139547-0CA1-448d-997F-3386EFDF049C})
* [DeclaredTarget](#{19B808BB-348E-4ea3-B62E-ED6356F7D4A0})
* [ChangeOfGovernment](#{7FA15F56-86C4-47f4-9032-999C17703368})
* [DemocraticChangeOfGovernment](#{33C68A39-AF9C-4f37-97EA-1DE4BAC4F7FB})
* [Government](#{D62DDBB8-53FC-405a-BC43-89CA337563A0})
* [OutgoingGovernment](#{A5516CD2-940B-4827-B38A-AD86AF934E99})
* [IncomingGovernment](#{BC752C7E-611B-47d6-BA89-05E58CD23803})
* [Election](#{7D9E328D-345E-43f5-8163-9657E4D016BD})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [ElectoralCandidate](#{E035D766-CB68-49c3-AC69-A56F3487C625})
* [ElectoralRegion](#{515468C2-B4D9-449d-8AC4-575973EFBF6B})
* [WinningCandidate](#{9FC35E2C-3D28-4f21-8FF7-3BAA51860958})
* [IncumbentRepresentative](#{5C4C2871-5F61-4704-83D0-9F8CF42890BF})
* [Summit](#{78D65599-BCBB-491a-8C34-75B9F7AB60D5})
* [VotingAttendee](#{B94FF143-3681-41eb-8264-D3E85C558EFC})
* [ObserverStatus](#{FB2FDA67-B258-4b18-9E95-3B9DFAB8FB14})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [EndToEndAgreement](#{1B39630B-B00F-4def-9C65-48082C4AD2E0})
* [Treaty](#{59599C4B-F3DE-49a0-B76F-BE4CB1293CBA})
* [PeaceTreaty](#{10FBBF98-4604-46d9-AD12-211597532B9E})

PoliticalEvents are Events that take place in local or national government, or in intergovernmental interactions.

### <a id="{B84B31E9-62DD-4a6b-89F3-459896232F75}"></a>Trade
![Trade Diagram](Images/EAID_B84B31E9_62DD_4a6b_89F3_459896232F75.png)

#### IES elements in this diagram:

* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [TradeEvent](#{CA86862B-DA7E-487c-907B-26FA5D0564CD})
* [TradedAsset](#{57ADBC97-C089-4d1a-A334-A9C44EAEC38A})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [OfferForSale](#{1D589649-490D-4558-91D5-2D977B2B42DE})
* [RequestForQuotation](#{300203EC-607A-4d77-AE6F-7EAE7FA44DF2})
* [Delivery](#{F428ADA5-2349-4cd0-815F-8F768B08C6E6})
* [tradedItemType](#{A92F03F0-CB9E-4667-B985-25377303416A})
* [Address](#{C90267B5-77A3-4b79-BD0D-7C50C3F4C333})
* [WithdrawFromSale](#{9416F72A-9BF9-4c99-839C-76905F02B63B})
* [PaymentArtefact](#{9882D901-1B22-4b89-81D1-031F840A20D0})
* [Supplier](#{E4D44720-DBEE-434e-A61E-35FE8B66A4BE})
* [Retailer](#{BA2472AB-56F0-462e-9460-F0192ABCD979})
* [Purchaser](#{B10A694D-31AA-456c-8C51-B7B5F101A39F})
* [OnlineShop](#{980404C4-C512-4f36-B3B1-5088CC754DCF})
* [Carrier](#{91DC18F6-3E35-411c-814D-5ACEE83BE316})
* [DeliveryRecipient](#{63289363-A4D6-4abf-BE19-6DCDDCF9B28F})
* [DeliveryAddress](#{096F83D3-F25E-4d48-96E8-566731C06DB1})
* [Purchase](#{0A9A9F7D-A6F1-4629-BD2B-7990D2D36493})
* [quantityOffered](#{AEC476A1-AE39-4a9e-9EE3-DD45B50B0F26})
* [quantityPurchased](#{0D2231E8-6AF1-4e59-B8FA-86A26334CC71})
* [quantityDelivered](#{7550DA0F-DF0E-4c61-9198-5DE767677A3A})
* [AmountOfMoney](#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8})
* [CashPayment](#{62A9AA44-6C36-448b-805F-E13203CFB4FC})
* [ClassOfEntity](#{D1B2FB30-36CA-4012-B85F-514E270BF541})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [EndToEndTransaction](#{911EB3DE-A001-493d-850D-3CF5A848791D})
* [FinancialAccount](#{44DAC574-2A2E-44bc-ACD2-236811FA8D29})
* [MoneyTransfer](#{D94ED70F-8CCA-4c6e-8AE5-65450BBA62D7})
* [SendingAccount](#{F7172876-85F6-4d29-B11F-A1B36616416A})
* [ReceivingAccount](#{25965198-3FE0-4bb9-BCA9-808E15A3EE49})
* [transferValue](#{A9D01DAB-281E-48ae-BB33-8518701ABBDE})
* [ModelOfDevice](#{7A879268-33C2-4f2b-8928-9E78AFF01E69})
* [ClassOfAsset](#{F999F59A-7C7B-40f3-8F86-5B2592889E95})
* [ClassOfDevice](#{09F9136C-9069-47ec-A58E-FC26CF9BA55E})
* [Device](#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [PartNumber](#{772CD8A3-3DCA-4cc7-8BA3-17D1C57E94BC})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [Rights](#{487778E0-4BD7-4d9a-B7F7-63731478E1A2})

TradeEvents cover the whole sales lifecycle from RFQ to delivery. Individual TradeEvents can be grouped into an EndToEndTransaction 

### <a id="{41F61D94-0E76-4f81-A005-AE93346DB054}"></a>Movement
![Movement Diagram](Images/EAID_41F61D94_0E76_4f81_A005_AE93346DB054.png)

#### IES elements in this diagram:

* [IdUsedInCheckIn](#{F481C966-058B-4caf-A427-9E492CAD0D63})
* [CheckIn](#{87308A03-5C79-4d94-99E1-660042AC7929})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [TravelService](#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74})
* [Flight](#{375B0887-712F-43f0-BBF4-5C544D75AC39})
* [Sailing](#{803AF0E7-01EC-4123-B888-3FB6369C840F})
* [TrainTravel](#{F2D6CFE4-BCE9-4bce-ADB0-075656038A55})
* [scheduledDepartureTime](#{340CF0CC-BA75-40b7-8B8A-167CD65C1830})
* [Port](#{57860A04-0128-4c7e-9BFD-83D3BA432F8C})
* [scheduledDeparturePort](#{1312D263-F609-4df3-A1DB-AA0557B3B94B})
* [scheduledArrivalPort](#{6BC73189-2B25-4e1c-A935-EDA8106F3EB3})
* [scheduledArrivalTime](#{DB3878D9-FF24-4069-A8DD-C24F5D074C0C})
* [carrierService](#{76C31798-780C-41b0-A985-0AE3B1C3A478})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [Journey](#{8B571665-0AA1-40be-A7A0-A35BE86B7192})
* [Facility](#{9CD2C1B1-85B1-4579-9376-07827AD68461})
* [BoundingState](#{892345CD-9FA7-4982-978D-B6D3ABAE839C})
* [Arrival](#{F2C03DA3-B554-4bde-A0DE-EFB5BEE19C56})
* [Departure](#{0FCBDA68-1B1C-40e1-9C5B-0E225CA827DB})
* [Transit](#{7693D2C9-0F06-4005-BB8D-B5B572B2281A})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [TravelLeg](#{55384377-146A-47c9-8706-18A1343A219C})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Passenger](#{D6D07656-1866-4cb4-97A7-FC4C1CB65416})
* [Movement](#{95B5ACC4-956A-4b29-AB9E-BDCD12EF319F})
* [Moving](#{D06C3801-F91C-436d-9D7F-DFDE29B48E5C})
* [Airport](#{82E3793F-D0D1-40ca-927C-7A6FEF913503})
* [CarTravel](#{F5E2BCD3-4529-42f2-9ED9-95801B42ED3F})
* [PersonInTransit](#{9888A3F3-7E9B-4806-BD4E-2FC4D87A5902})
* [VehicleController](#{93A816A9-EB7B-4250-8A1A-8919488029A7})
* [Vehicle](#{3B916F09-F3F4-43e9-9C84-99009C685396})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [VehicleUsed](#{2202F5B0-DF49-4db5-A8F9-31FC2CC89005})
* [RoadVehicle](#{830B2164-E880-4bef-A62C-B38CEB6A824D})
* [Aircraft](#{01A64A84-7A14-45a5-AAF2-F1AA614D5F30})
* [Ship](#{14098560-1FF3-4599-B9A5-41167861538B})
* [EntityInTransit](#{74169219-A47C-48ce-A25F-3948E7E873B6})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [OnJourney](#{80AFD655-A969-46be-BE72-035C053C1C4F})
* [IdentityDocument](#{BDF4EBD9-7F41-4d90-91A7-571177330C1B})
* [TravelServiceIdentifier](#{680FD822-C1F6-4d09-94D5-5D586C947DE1})
* [PassengerName](#{E5C1270D-35AD-4f86-B0E4-1DC0039174E3})
* [SeatNumber](#{03D1711E-F9A7-41b1-B82F-B442FDF82EBF})
* [BoardingCardNumber](#{683E5B90-2514-4342-AE34-894D2DAC2AF0})

The Travel model in IES4 is based on that from IES3, but combines the concepts on TravelService an Travel into one model. As a result of this merging, the model can appear somewhat daunting, but is really made up four basic concepts:

* Movement - an event where one or more Entities move from one location to another. Pretty much everything about this is optional - we may not know what moved, where it started or where it ended.
* Moving - the state of an Entity when it is moving. This can be (and usually will be) part of a Movement event (when we want to say more about the other participants). However, it can be used on its own, as the state of an Entity just to say we knew the Entity moved.
* Journey - a Movement which is made up of two or more TravelLegs (also Movements). Journeys are used to collect together individual movements into an end-to-end journey
* TravelService - the end to end provision of a regular, scheduled travel function - this could be a bus route, a numbered flight (e.g. BA123) or a regular sailing.

All the above can have Departure and Arrival states, and those states can be in a Location, and in a Period. Additionally, IES allows for the specification of the actual Vehicle used, and in the case of People in transit, whether a person was driving / piloting or was simply as passenger.

Overall, much like the rest of IES, this model has been designed to work with as much or as little detail as is available. The (moderately complex) example below shows Fred's Journey to Los Angeles. The first leg is by car to Heathrow Airport, then by plane to LAX. We don't know what happened to him after his arrival in LAX.

### <a id="{0641B013-5267-4314-84C8-1856EBA51A47}"></a>Travel Booking
![Travel Booking Diagram](Images/EAID_0641B013_5267_4314_84C8_1856EBA51A47.png)

#### IES elements in this diagram:

* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [TravelBooking](#{76DC9A0C-F6E8-4ff4-ADD6-072DC1EBE3AB})
* [contactDetailsOnBooking](#{B54BB629-E007-4099-BC01-B512894F1E89})
* [BookedPassenger](#{53C6BCA9-4D66-4bac-B946-0A8541CF510A})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [BookingAgent](#{0AF87601-5B3E-4c5e-8149-D0D3C0073C42})
* [AmountOfMoney](#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8})
* [BookingPayment](#{61BDEBA6-BE87-44e3-A1C7-246D0CE60ADC})
* [Identifier](#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E})
* [BookingReference](#{D31E959A-6354-40e7-8370-1FE5246624AD})
* [ClassOfTravelBooking](#{44D4DD7C-201A-447d-8BCE-C8B3E3E6A890})
* [bookingType](#{C52879E4-919A-4dee-82EB-3CB11DD69E56})
* [Rights](#{487778E0-4BD7-4d9a-B7F7-63731478E1A2})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [Reservation](#{CDF94674-D458-4996-9A99-6CBFFF3907EB})
* [TradeEvent](#{CA86862B-DA7E-487c-907B-26FA5D0564CD})
* [TradedAsset](#{57ADBC97-C089-4d1a-A334-A9C44EAEC38A})
* [Purchase](#{0A9A9F7D-A6F1-4629-BD2B-7990D2D36493})
* [TravelReservation](#{8B290363-239E-415e-9F2D-8267D1BA2ECB})

The booking of planned travel arrangements.

TravelBookings may include bookings for Flights, Ferry Crossings, Train Journeys (i.e Travel Services), and also Hotels, Hire Cars etc. when these have been modelled. These will be included on the booking as relationships to the appropriate other entities.

TravelBooking is currently an Entity though there is some debate as to whether it really should be an Event

### <a id="{D488BDAE-AAEA-4c4a-B866-ED79D154D547}"></a>All Events
![All Events Diagram](Images/EAID_D488BDAE_AAEA_4c4a_B866_ED79D154D547.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [TravelBooking](#{76DC9A0C-F6E8-4ff4-ADD6-072DC1EBE3AB})
* [TravelService](#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74})
* [BusinessEvent](#{94CEDBD1-8E3D-4cb4-8155-FBD621DA6A0D})
* [Communication](#{6698805F-F492-4f1f-954C-E1EB3C53E148})
* [LifecycleEvent](#{FA07AB7A-0EE8-4258-BE8B-260F9A1192A7})
* [OperationalEvent](#{59121C21-38E4-4224-8C2D-4D3E94A3A0D9})
* [CriminalActivity](#{43E58528-16E4-48b3-8F13-10500879EA83})
* [LawEnforcement](#{3876B81C-E316-4e11-A6C4-8024E52F769B})
* [PoliticalEvent](#{3A0E6FDD-5B3B-4092-9549-C05E8A5FED41})
* [OnlineEvent](#{24499751-7D9B-4f2e-B880-8D5BC4FCEF30})
* [EntertainmentEvent](#{78C33499-CD14-43cb-82AE-93A0F8CF022B})
* [CoLocation](#{3524D10D-D9B0-416d-ADED-D5AAEB99DD09})
* [TradeEvent](#{CA86862B-DA7E-487c-907B-26FA5D0564CD})
* [Movement](#{95B5ACC4-956A-4b29-AB9E-BDCD12EF319F})
* [AgreementStage](#{422B4F1C-DA90-400b-8FFD-43C90B4F10F4})
* [Disagreement](#{E73C74A9-B356-40a4-BDBB-40567592BBD0})
* [CheckIn](#{87308A03-5C79-4d94-99E1-660042AC7929})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [Competition](#{98421510-0A8A-4942-9743-191EA0DCA9E6})
* [Cooperation](#{F650B9E3-2669-455e-B20C-92737CFD9A08})
* [PartyInCommunication](#{A5713B2C-E098-4dd2-BD46-42DA51899FEA})
* [Purchase](#{0A9A9F7D-A6F1-4629-BD2B-7990D2D36493})

The diagram below shows all the immediate subtypes of Event

### <a id="{832A60AA-2F61-4a7f-BC86-A58E8D7FCFDA}"></a>
In IES3 there was "User of" which connected a person to an OnlineService. In IES4, we use hasAccessTo, and this connects to the OnlineAccount rather than directly to the service.

As with "User of" this is a statement of occasional use (or access to) rather than a specific event.

For a single use of the account, the Account is related to an instance of a PersonState. To show ongoing (regular) account use, the instance of the PersonState should also be an instance of DiscontinuousState

### <a id="{392C98BE-E511-4e53-88FE-44ABF7BF7616}"></a>
Sometimes we don't know anything about a CommunicationAccount other than there must have been one. To help prevent duplication as more information comes in, it is therefore best to just create the participation (a state of the account) and attach the comms ID to that, rather than second-guessing the Account itself. 

### <a id="{77E90A65-705B-4838-AFD5-02B77B8CC98E}"></a>
IES 3.x presented a number of different Event roles for Lifecycle events - e.g. DestroyedDocument, etc. This has been slightly simplified in IES4, see below...

<b>IES3.x 						IES4</b>
Founder						Creator
NewOrganisation					Created
Forger							Creator
ForgedIdentityDocument				Created
Modifier	of					Modifier
Destroyer of						Destroyer
DestroyedCommunicationsIdentitifier		Destroyed

Note that the CreationLocation/PlaceOfChange is handled using happensIn

### <a id="{26821289-4446-4092-911B-CDB41A467DE5}"></a>
In IES4, happensIn replaces:

ArrestLocation
TrialLocation
Prison

### <a id="{4C9E3526-D763-4ad5-A48D-3396E6261D87}"></a>
happensIn should only be used when the Location complete envelops the Event. In other cases (e.g. departure and arrival locations for a travel event) the appropriate EventParticipant subtype should be used

### <a id="{6092B3D7-05E4-41fb-AE7B-E3CB42AE3D01}"></a>
In IES4, happensIn replaces CreationLocation from IES3

### <a id="{1A23D669-160A-47b2-A903-9436ED4F2E72}"></a>
In IES3 there was an attribute called natureOfEvent. In IES4, the approach is to create subtypes of the Event in your data and then instantiate those.

### <a id="{B583A07C-4088-4ca9-A0A9-3342B8CFF612}"></a>
See also visits, socialises, and worksIn in the Operational relationships diagram

### <a id="{62284CB2-4E40-4369-9A52-F96BEFBA5AA0}"></a>
In IES4, happensIn replaces:

ArrestLocation
TrialLocation
Prison
AttackLocation (area of attack in general rather than weapon/target location)

### <a id="{B4A59386-B831-41ed-9604-03B4BD97CEB8}"></a>
More often than not, authority to act is only granted for a period of time - or requested for a period of time. To reflect this, an instance of an AuthorisedEventClass will most likely also be an instance of TimeBoundedClass (see Types diagram)

### <a id="{1074785F-032F-41a3-A1AA-F7E7E68117F3}"></a>
IES 3.x presented a number of different Event roles for Operational events. In IES4, these are just covered by two roles - Operator and SubjectOfOperation:

<b>IES3.x 						IES4</b>
SurveillngOrganisation				Operator
LocationUnderSurveillance*			SubjectOfOperation
OrganisationUnderInvestigation**		SubjectOfOperation
InvestigatingOrganisation				Operator
Target***						SubjectOfOperation
Instigator						Operator

*note, this is not the location <i>of </i>the surveillance, for that use <b>happensIn</b>
** in IES4 this also allows for an investigation against an individual person
*** note that the location of the target and the weapon can also now be specified in IES4

### <a id="{E0ADF541-B93C-44a4-8A23-5ED7475D3B5C}"></a>
UML Dependency is used to indicate which Entities are appropriate for a given type of EventParticipant - i.e. a shortcut for isParticipationOf

### <a id="{99A0962F-65B1-4252-B929-D85CEED655A1}"></a>
ies:seatNumber

### <a id="{13182B8F-DA31-4bba-93E0-E6EBCEE53E94}"></a>
"LOW"

### <a id="{97D446C7-3BDA-46d0-8775-E83BBF6C9AC2}"></a>
"33B"

### <a id="{D82FE095-D5C4-434c-9538-017A42C5AF22}"></a>
"MEDIUM"

### <a id="{FB50E4D6-B478-4185-B1D1-C7E04ACA2D95}"></a>
"HIGH"

### <a id="{9A26AB2C-2C95-457d-BACF-D29C3FD26B61}"></a>Entities : Amount of Money
See also : Amount of Money

### <a id="{1A8010BB-7AA4-40fc-B821-40594F97DDA1}"></a>Entities : Assets
See: Assets

### <a id="{B1600689-297E-46af-B18C-9AA4DDA82FFF}"></a>Entities : Communications Device
See also : Communications Device

### <a id="{4A89B4DF-249B-43c0-84F1-7580449234E8}"></a>Entities : Communications Identifier
See also : Communications Identifier

### <a id="{5AA4F729-B191-4ec4-AB70-97C3DC74DA8B}"></a>Events : Agreement
See also : Agreement

### <a id="{79136301-AC55-4e8e-9AE0-1307A3B70EA1}"></a>Events : Communication
See also : Communication

### <a id="{CAEFBF64-6AB1-48e3-9ADE-528B3FFB35FD}"></a>Events : Criminal
See : Criminal

### <a id="{33C5A358-7945-4af1-8FA9-F5FA76B3524E}"></a>Events : Disagreement and War
See also : Disagreement and War

### <a id="{07F84688-05BA-4256-90AE-8FC82231ED2E}"></a>Events : Operational
See also : Operational

### <a id="{D08EA2CA-FA75-40c7-A2AC-F4B5576DC175}"></a>IES v4 : Event Participation
See also : Event Participation

### <a id="{66904BF0-3FCF-4ded-8217-15C0A231D87D}"></a>Relationships : Operational Part 2
Operational Part 2

## <a id="{9ED67AE2-F907-4f58-A67F-921186EC23FB}"></a>Relationships


### <a id="{C6937856-2424-4e96-BFE1-8CA3611869D1}"></a>Familial
![Familial Diagram](Images/EAID_C6937856_2424_4e96_BFE1_8CA3611869D1.png)

#### IES elements in this diagram:

* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [siblingOf](#{A0D40C4F-B513-4c9f-8D4A-79D0FA7CEF50})
* [Married](#{D03A0D8B-79F5-4901-97BC-2767FD46CD5F})
* [parentOf](#{6F13083C-505A-473e-9EDB-B0E534A341FB})
* [ancestorOf](#{15388C46-262D-4f70-8F65-83758A5AEAF5})
* [familiallyRelatedTo](#{3AA26AC6-206D-4b6d-BDEC-C9E2B4814BE7})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [PersonState](#{38F8B795-0BCE-4945-8C69-8678ED935C1A})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [EndToEndActivity](#{A88ABE99-1D6C-4843-A2E4-7531626D3859})
* [Marriage](#{9DFEDF24-1203-4341-B282-BD37C1B9CDF5})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [nephewOrNieceOf](#{1995033D-7AF2-468c-998D-61E86FB51B16})
* [cousinOf](#{32A625FA-3159-4b36-B551-3742BA11C7A8})
* [ActorState](#{7ED8BC7C-A85F-4ed5-AC6F-D640F2DF4B7B})
* [Actor](#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B})

Most of the familial relationships from IES3 end up being relationships in IES4 - in fact the blood relations end up being between whole-life Person entities as the relationship lasts for life. The one exception is Marriage which has been modelled as an EndToEndActivity due to its temporal nature and the fact that the "relationship" is bidirectional. 

### <a id="{59F513B8-3ECE-4bac-8BD0-908306396A8F}"></a>Interest
![Interest Diagram](Images/EAID_59F513B8_3ECE_4bac_8BD0_908306396A8F.png)

#### IES elements in this diagram:

* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [PersonState](#{38F8B795-0BCE-4945-8C69-8678ED935C1A})
* [interestedIn](#{7BD2B884-F02C-4da2-AF6A-21B790FBF669})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [Dislikes](#{30A0F2DA-DB31-40fd-8723-88A24B2F8448})
* [Likes](#{B292748F-D41E-4c3b-9335-04D4B06A1F34})
* [attribute](#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA})
* [strengthOfInterest](#{49B3D340-AADC-4fcd-80CC-283AE0FC85DF})
* [natureOfInterest](#{0C0728AF-B9F2-418f-A03E-107689F0ACA0})
* [Loves](#{E543978A-06D0-4c79-BCCD-A62DE9294A85})
* [Hates](#{6939AE2F-D74D-4446-8A88-5C26669689BA})
* [ActorState](#{7ED8BC7C-A85F-4ed5-AC6F-D640F2DF4B7B})
* [Interested](#{B1D011F9-9585-49eb-97C4-86E82D6F0BCF})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})

The InterestedIn relationship links a PersonOrOrganisationState to something they are interested in (any ExchangedItem). The state is used, as people tend not to be interested in something for their whole lives. 

GeneralConcepts are often the things of interest (e.g. football, finance, animal husbandry, etc.), but there may be Entities that are also of interest (e.g. a financier being interested in Vodafone plc)

### <a id="{9E3102FC-46DC-4363-B0B4-D0EA7275D05D}"></a>Lifecycle Relationships
![Lifecycle Relationships Diagram](Images/EAID_9E3102FC_46DC_4363_B0B4_D0EA7275D05D.png)

#### IES elements in this diagram:

* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [LifecycleEvent](#{FA07AB7A-0EE8-4258-BE8B-260F9A1192A7})
* [Create](#{AF60517B-E4EF-48ca-BE0F-56E0A89660FD})
* [Creator](#{850DB6D5-C8E8-4aa8-87A0-4E7680FF854A})
* [Destroyer](#{C029299D-5946-48dd-94CB-80EC23A56300})
* [Modifier](#{21A341AE-9A38-4f45-BCB5-B29B02DC1B90})
* [Modify](#{3EF09CE4-79B0-42be-9AA1-12B97611BF2B})
* [Destroy](#{27000BBA-F3F9-4355-B466-92CE04477C9B})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})

All of the Lifecycle relationships from IES3 end up being EventParticipants in IES4

### <a id="{9D1812FF-691F-4847-B79C-9136091D93E0}"></a>Mutual Understanding
![Mutual Understanding Diagram](Images/EAID_9D1812FF_691F_4847_B79C_9136091D93E0.png)

#### IES elements in this diagram:

* [EndToEndAgreement](#{1B39630B-B00F-4def-9C65-48082C4AD2E0})
* [Negotiation](#{FB2EA8AE-164A-4642-82E3-D2622DC6FCCB})
* [Ratification](#{31977608-5432-4d6f-AEE0-19838197C813})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [PartyToAgreement](#{AF57E842-9BF7-4f6e-B180-DDEACB0F5386})
* [Signatory](#{C55A12C9-CF85-4b7c-B422-1D41054E9570})
* [Negotiator](#{D4B25AAF-F083-45ba-8188-25DE9D86013D})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [War](#{D4F568F5-7BC4-489d-94BC-AE1305E5C0C2})
* [AtWar](#{89953404-8A71-46ef-8F7B-90C12EE286FD})
* [ActiveEventParticipant](#{3360DCC9-D39B-4280-8872-2FE122240407})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [InDisagreement](#{F12D45EA-66D5-4016-BDF7-E1CD8F48CCF5})
* [Disagreement](#{E73C74A9-B356-40a4-BDBB-40567592BBD0})

All of the Mutual Understanding relationships from IES3 end up being EventParticipants in IES4

### <a id="{461D38A7-E51F-4e68-AB15-CA7B0E27B1F6}"></a>Operational Part 1
![Operational Part 1 Diagram](Images/EAID_461D38A7_E51F_4e68_AB15_CA7B0E27B1F6.png)

#### IES elements in this diagram:

* [TravelService](#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74})
* [Flight](#{375B0887-712F-43f0-BBF4-5C544D75AC39})
* [Sailing](#{803AF0E7-01EC-4123-B888-3FB6369C840F})
* [TrainTravel](#{F2D6CFE4-BCE9-4bce-ADB0-075656038A55})
* [Transit](#{7693D2C9-0F06-4005-BB8D-B5B572B2281A})
* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [charters](#{48223A62-12E6-4953-8F80-8C7A48151825})
* [excludedFrom](#{883B5479-62DD-47a4-BC14-9A11835D820B})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [hasAccessTo](#{CB7F872F-7999-4bfd-8274-2C0E0AFE22AB})
* [Movement](#{95B5ACC4-956A-4b29-AB9E-BDCD12EF319F})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [maintains](#{727175D4-0998-49a0-BAEE-6B8F1F1FD8D4})
* [residesIn](#{6BC3DDD8-477E-4c8a-B85D-E637CF9DB6DF})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [AssetState](#{CA196722-9531-4eb4-A8CF-B9A5145CDCFD})
* [storedIn](#{2E33B6DC-54D5-4e5e-9894-B2801F174B00})
* [TravelTicket](#{6C669BEF-9267-4612-9F29-B28918B203F5})
* [authorisesAccessTo](#{A2DA918D-843C-43c9-A974-4795601E9D65})
* [Ticket](#{0BC61540-2AFB-42e6-A845-79771EE0268D})



### <a id="{BAD148FB-D906-45c4-9A2C-D79819F47655}"></a>Operational Part 2
![Operational Part 2 Diagram](Images/EAID_BAD148FB_D906_45c4_9A2C_D79819F47655.png)

#### IES elements in this diagram:

* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [owns](#{FDD94D9F-F343-4c1b-9688-752C896A3C7C})
* [inPossessionOf](#{0A28624B-C5E3-461e-B84A-E55B550B5DD6})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [userOf](#{01984617-C96D-48b3-ACDE-25F525719AEF})
* [worksFor](#{181AAC84-26CE-4531-AC32-A73B8FD8B858})
* [visits](#{92FC2C35-D40B-4393-BA0B-88849743FEB6})
* [inLocation](#{463F9B14-2D14-4364-B4F0-658A20DFCBFA})
* [socialisesAt](#{1D9F0978-EFD2-4e27-9242-219637C574EF})
* [worksAt](#{55161540-8869-4af9-B159-51857E0B0BDB})
* [usesServicesAt](#{958E4D57-8A19-4855-B9B3-6BB2F93F77B7})
* [worshipsAt](#{475617C7-BEE3-4c5e-8749-9386B68A8DA5})
* [hasAccessTo](#{CB7F872F-7999-4bfd-8274-2C0E0AFE22AB})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [staysAt](#{90332C00-0188-4773-8A71-F9ED15F5ED33})



### <a id="{DC8F8219-960A-4207-B9AF-98B9486529A8}"></a>Professional
![Professional Diagram](Images/EAID_DC8F8219_960A_4207_B9AF_98B9486529A8.png)

#### IES elements in this diagram:

* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [visits](#{92FC2C35-D40B-4393-BA0B-88849743FEB6})
* [worksFor](#{181AAC84-26CE-4531-AC32-A73B8FD8B858})
* [PersonState](#{38F8B795-0BCE-4945-8C69-8678ED935C1A})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [worksAt](#{55161540-8869-4af9-B159-51857E0B0BDB})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [employedBy](#{74721DF1-18D6-4c1b-93CC-71C888C6D405})
* [contractedTo](#{0876AE1F-7202-41d9-A00F-208B118BBF79})
* [managedBy](#{8991D995-1915-47b7-B180-D9EBC4A1FD1F})
* [supplierTo](#{4F013D3F-E237-489a-96D5-5E9E54C6A388})
* [isTeacherOf](#{B8650A61-3B08-4f62-8EAB-0F9D007B20CE})
* [worksWith](#{25DD07E3-2500-4b9b-AF50-446EEC927AD2})



### <a id="{E92F9ED3-BB84-4e2f-B9FB-5B787D917BD0}"></a>Social
![Social Diagram](Images/EAID_E92F9ED3_BB84_4e2f_B9FB_5B787D917BD0.png)

#### IES elements in this diagram:

* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})
* [ResponsibleActorState](#{100B93CD-937E-4fdd-8851-02D1DC07F5B6})
* [ResponsibleActor](#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9})
* [PersonState](#{38F8B795-0BCE-4945-8C69-8678ED935C1A})
* [Person](#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2})
* [OrganisationState](#{F3DB6A59-B2DE-4743-A9A8-7DA9CCC68638})
* [Organisation](#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F})
* [enemyOf](#{7F1A6A06-5223-4bf9-B903-1061A127D62C})
* [friendOf](#{13EB3439-497F-49ad-A7F4-DEF8A600F640})
* [fearfulOf](#{A589F81D-DC15-4b71-80B5-BA4CD46B2E41})
* [respectfulOf](#{EEBCE0A4-4882-4c95-9C2D-93CE5EB7A275})
* [disrespectfulOf](#{369D2CA7-BFFD-4bc3-941F-47262C3DBF1F})
* [trusts](#{37CEEA2E-93E7-446d-A181-A55A091C3B22})
* [distrusts](#{3499FB8A-AA42-4367-BBBC-79A69338BD70})
* [alliedTo](#{7F818F57-2C3B-4629-8EEC-F5F8310AE655})
* [Alliance](#{3D83E15F-ACA8-48e4-8C7B-84580807E06F})
* [coercedBy](#{9E413787-42C8-4cd4-B7B1-63E38F6A02D9})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [Competition](#{98421510-0A8A-4942-9743-191EA0DCA9E6})
* [EventParticipant](#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB})
* [Competitor](#{763C82F1-5CE0-4652-8A93-D56D93DE1544})
* [Cooperation](#{F650B9E3-2669-455e-B20C-92737CFD9A08})
* [Cooperator](#{2B96182A-9363-4c6a-BE62-132B072A7520})
* [influencedBy](#{411F5C4C-9AD0-462a-BE10-3F43958B7D66})
* [intimidatedBy](#{39D0AC05-01DB-423a-861A-26E6125DF906})
* [opposedTo](#{436E6ABB-C1E3-484e-B15B-63E700B27EA8})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [knownAssociateOf](#{57F3607C-0204-4590-9442-24F372A35931})

The nearest an ontologist gets to Tinder

### <a id="{BED9B9A0-547E-49d5-AB9D-2BD0A634A3EA}"></a>Structural
![Structural Diagram](Images/EAID_BED9B9A0_547E_49d5_AB9D_2BD0A634A3EA.png)

#### IES elements in this diagram:

* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [isStateOf](#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E})
* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [assessedToBeTheSameAs](#{6A1C6C65-D671-4ea3-9184-044AE2A802CF})
* [ClassOfElement](#{3C13E07D-5796-4d03-9EBC-C75277E87CA4})
* [Asset](#{40231334-5ACC-4dd4-A8C1-05012E2170E0})
* [IndividualDocument](#{0F327324-6B4E-40b1-B96B-97A334BA5E4A})
* [ClassOfEntity](#{D1B2FB30-36CA-4012-B85F-514E270BF541})
* [Representation](#{675A5C23-0746-43d0-96D0-AF0DF72CD697})
* [ClassOfIndividualDocument](#{CCC8FA06-CDA8-491d-BFFC-0A88D6A565B1})
* [WorkOfDocumentation](#{F0B48978-D4E4-45a4-8238-091A5B714D82})
* [aCopyOf](#{22D9054C-AE5C-4afe-99D9-3C9D65C86CB9})
* [SimilarEntities](#{A4B13044-00FD-4868-8147-1A3C9E84DAAB})
* [similarEntity](#{333E73AD-563F-443c-A9B3-CA122FDF75B9})
* [after](#{FA4DDF04-16DA-4b5c-AE9A-6AB8CD07DCDB})
* [successorTo](#{BEC84E4F-F407-4a20-BC68-AD1723A3F860})

The way that structural relationships handled (as defined in IES3) has changed in IES 4. Care must be taken in how these are used.
&nbsp;
<ul>
	<li>assessedToBeTheSameAs - in a 4D (extensional) ontology if two things are the same, there should only be one instance. In most (IES3) cases, things that were deemed to be the same were often just two states of the same whole-life thing. In other cases, they were just two sets of identifiers for the same thing, used by different naming schemes. That said, in very rare circumstances (usually when data arrives from more than one place) two things genuinely are the same (same spatial and temporal extents). If possible, these should be merged into one, and their original identifiers kept. If not, and when all other approaches are not possible, then the assessedToBeTheSameAs relationship may be used. Please try not to though. Thanks.</li>
	<li>Copy of (IES3) is simply two instances of the same class. So for documents, this would be two IndividualDocument instances from one WorkOfDocumentation, using the aCopyOf relationship.</li>
	<li>"Similar to" is now handled by creating a SimilarEntities class and using similarEntity to link the Entity instances to the class. This allows for more than two similar entities to be modelled.</li>
	<li>"Part of" is now "isPartOf" and is used in a similar way as to IES3, but has many subtypes that are used for putting things in locations, periods of time, etc.</li>
</ul>



### <a id="{20BF4E8F-9683-4bf4-B59C-F7F2AB2FB8F3}"></a>Topological
![Topological Diagram](Images/EAID_20BF4E8F_9683_4bf4_B59C_F7F2AB2FB8F3.png)

#### IES elements in this diagram:

* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})
* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [ArbitraryOverlap](#{F8FABF60-63D3-42ae-BA6A-54CFD0C036BF})
* [Location](#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A})
* [Crossing](#{B85F065A-6A18-433e-9195-7B6BCBB91C7C})
* [crossingOf](#{5A0E8F10-EE46-49bd-8E25-A67040D4A40B})
* [inLocation](#{463F9B14-2D14-4364-B4F0-658A20DFCBFA})
* [nearTo](#{E3BB8B07-9CC5-407a-8CC7-E2B0E1B69476})
* [nextTo](#{F33CAAA7-85A7-4e41-B0D4-3EAC4E6F73CC})

As with the Structural Relationships, Topological Relationships are handled differently in IES4 due to the criteria of identity (space and time - if "two things" occupy precisely the same space for the same period of time, they are the same thing and only one instance should be created). 
&nbsp;
<ul>
	<li>"Equal to" is a case in point. Here, there should be just one location with multiple identifiers. Note that the examples in IES3 are not always exactly the same extent, so sometimes, these would be <i>isPartOf </i>relationships</li>
	<li>"Crosses" is a case of two extents having shared parts, and is modelled using the <b>Crossing </b>Entity and <i>crossingOf </i>relationship</li>
	<li>For "is within", use the more general <i>inLocation </i>relationship</li>
</ul>



### <a id="{DE627D02-C0D9-462a-9CB7-1C496714A13D}"></a>All Relationships
![All Relationships Diagram](Images/EAID_DE627D02_C0D9_462a_9CB7_1C496714A13D.png)

#### IES elements in this diagram:

* [isPartOf](#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC})
* [isStateOf](#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E})
* [after](#{FA4DDF04-16DA-4b5c-AE9A-6AB8CD07DCDB})
* [inPeriod](#{2F08EF25-A5C8-48ad-85E3-903DB008AA19})
* [relationship](#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A})
* [hasPublisher](#{07FD1DF6-BA77-4657-B3D3-D6D579FD4608})
* [hasAuthor](#{9464D864-E76F-4e09-89E1-D3B2D3E63F3B})
* [hasCountryOfIssue](#{E7500475-8C4F-47a3-8AAB-C5679621FAE8})
* [hasStatedPlaceOfBirth](#{F95710A9-B0A7-4f7b-ADAA-08A2DCBD9C35})
* [wasAuthorisedBy](#{7A58C9AD-C198-4a61-8244-DE5BBC591416})
* [hasStatedAddress](#{0451B5D4-99CB-47a7-BB93-DF4DF6625837})
* [hasEmergencyContactAddress](#{0AAF6757-AAC9-43c4-8B43-CB3358EADCA4})
* [hasStatedPlaceOfIssue](#{644B75E8-92A0-4f16-861E-3B4FDFDF572E})
* [hasStatedCountryOfResidence](#{9A4EB722-0BDA-4ba7-B895-7A4E273865C9})
* [hasStatedNationality](#{C8AB9A91-97ED-4868-8167-44E71F40AFE7})
* [isAuthorisedForUseWithPassport](#{1CA57828-3B6B-450b-B477-C59A196EAE34})
* [countryOfRegistration](#{D33498ED-B6A0-41ea-864F-CE95E2B1E010})
* [paymentArtefactProvider](#{C793E699-C27B-49cc-9358-C4A0E17E609E})
* [accountForCard](#{7891E893-56DB-4d47-80B4-C78A667767F6})
* [venueStatedOnTicket](#{3345AECA-925E-4bfc-820E-2294D5921E71})
* [associatedCarrier](#{2E464C7F-FC0B-4dcc-9B1C-5DCA87B4CE3A})
* [issuingAgency](#{74D86486-8E18-474a-8930-B92E759BBE06})
* [ticketDepartureLocation](#{952E5981-257F-429e-9F22-8D2E3B9282C7})
* [ticketArrivalLocation](#{A4906B5E-8718-404e-8EEF-20AE29106383})
* [scheduledDeparturePort](#{1312D263-F609-4df3-A1DB-AA0557B3B94B})
* [scheduledArrivalPort](#{6BC73189-2B25-4e1c-A935-EDA8106F3EB3})
* [carrierService](#{76C31798-780C-41b0-A985-0AE3B1C3A478})
* [transferValue](#{A9D01DAB-281E-48ae-BB33-8518701ABBDE})
* [governedRegion](#{72DC3E90-53CE-434d-A5F3-89BDCE08A201})
* [governedPopulation](#{917C549C-259F-4850-9CFD-35E05485BF63})
* [tradedItemType](#{A92F03F0-CB9E-4667-B985-25377303416A})
* [interestedIn](#{7BD2B884-F02C-4da2-AF6A-21B790FBF669})
* [isRepresentedAs](#{D106A0A9-55C4-454f-9E20-35BA54114036})
* [schemeOwner](#{8D42B4A8-30D3-459d-A729-F5C8FE16D418})
* [schemeMasteredIn](#{C2C5FF87-189C-478a-B3BF-4706D798087F})
* [idOnCard](#{92D9B068-F8D4-4cbc-AD57-1DA39D5CC1C7})
* [hasRegisteredCommsID](#{E076AFB8-F6F8-4b06-82B3-7ED568D1EE73})
* [documentIdentifies](#{2F8738A6-5EBA-4d80-980B-AA9E6F28B81A})
* [influencedBy](#{411F5C4C-9AD0-462a-BE10-3F43958B7D66})
* [opposedTo](#{436E6ABB-C1E3-484e-B15B-63E700B27EA8})
* [assessedToBeTheSameAs](#{6A1C6C65-D671-4ea3-9184-044AE2A802CF})
* [inRepresentation](#{7238489D-6802-4733-9F7F-9B31D02B3C81})
* [Entity](#{F4EDE167-6F5A-417d-9984-0221CCDF752C})
* [ExchangedItem](#{485CBF1A-04FF-4741-8471-46A03D28C406})
* [Element](#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21})
* [State](#{47301D66-CBD5-4d10-9481-B66966A3F3A2})
* [nationality](#{45CDA5C1-624D-4f2f-81F6-EF19300820A9})
* [hasReligion](#{6D1839A4-342A-4e34-823C-BDB392483048})
* [nearTo](#{E3BB8B07-9CC5-407a-8CC7-E2B0E1B69476})
* [intimidatedBy](#{39D0AC05-01DB-423a-861A-26E6125DF906})
* [coercedBy](#{9E413787-42C8-4cd4-B7B1-63E38F6A02D9})
* [alliedTo](#{7F818F57-2C3B-4629-8EEC-F5F8310AE655})
* [distrusts](#{3499FB8A-AA42-4367-BBBC-79A69338BD70})
* [trusts](#{37CEEA2E-93E7-446d-A181-A55A091C3B22})
* [disrespectfulOf](#{369D2CA7-BFFD-4bc3-941F-47262C3DBF1F})
* [respectfulOf](#{EEBCE0A4-4882-4c95-9C2D-93CE5EB7A275})
* [fearfulOf](#{A589F81D-DC15-4b71-80B5-BA4CD46B2E41})
* [friendOf](#{13EB3439-497F-49ad-A7F4-DEF8A600F640})
* [enemyOf](#{7F1A6A06-5223-4bf9-B903-1061A127D62C})
* [visits](#{92FC2C35-D40B-4393-BA0B-88849743FEB6})
* [userOf](#{01984617-C96D-48b3-ACDE-25F525719AEF})
* [authorisesAccessTo](#{A2DA918D-843C-43c9-A974-4795601E9D65})
* [informationContent](#{5BEE4248-DC98-4625-8553-3BB2171A1EDE})
* [isParticipantIn](#{BAEA86D9-C90E-4f8d-96F5-A01BB0C49711})
* [inLocation](#{463F9B14-2D14-4364-B4F0-658A20DFCBFA})
* [crossingOf](#{5A0E8F10-EE46-49bd-8E25-A67040D4A40B})
* [PeriodOfTime](#{3FDFA898-C340-4279-8B3C-275359D5B02D})
* [isParticipationOf](#{DF9F6056-CCD4-41aa-9A86-536F6150EC25})
* [Event](#{B376370E-F5E8-4287-A3EC-AC35532919B1})
* [hasName](#{C3A36E36-0C73-4af7-88E3-81C9243CE456})
* [documentedBy](#{AC7C948A-F19C-4296-AC38-0FEE6A4C5E90})
* [hasSourceReference](#{16480E86-9FE4-4b37-ACFB-9E410F190664})



### <a id="{B01D5F55-BF7F-4bcd-B5A3-ACEEBB67F37E}"></a>
Changes from IES 3:

<ul>
	<li>For "In contact with", see Communication diagram</li>
</ul>


&nbsp;
<ul>
	<li>For "Subscriber to" see Online diagram</li>
</ul>




### <a id="{71F3F3B1-ADEC-480e-B9A4-99E68B8F2E44}"></a>
Changes from IES 3:

<ul>
	<li>For Located At, use inLocation - see the WhereAndWhen diagram</li>
</ul>

<ul>
	<li>For "Used to Verify", see CheckIn in  the Attendance diagram</li>
</ul>

<ul>
	<li>For "Paired With", see CommunicationsIdentifier diagram</li>
</ul>

<ul>
	<li>For "Is associated with" see IdentityDocument diagram</li>
</ul>

<ul>
	<li>For "Rental Of", see RentalAgreeement in the Agreements diagram</li>
</ul>

<ul>
	<li>For "Fulfilled By", see VehicleUsed in the Movement diagram</li>
</ul>

<ul>
	<li>For "Purchaser Of", see Trade diagram</li>
</ul>

### <a id="{32236FE8-78CF-4997-A848-3B877338E1E7}"></a>
Use with caution. In 99.99% of the occasions when you think you need this, you actually don't

### <a id="{21F150BC-4EBB-459f-880E-8433BDED9D12}"></a>
See main models:

### <a id="{3C8959FE-BDE5-427c-8250-7644B8CE146A}"></a>Entities : Communications Identifier
Communications Identifier

### <a id="{962E4B18-0F33-4a32-B823-D233EE16A2FB}"></a>Entities : Identity Document
Identity Document

### <a id="{A13E7FBB-91E9-4ff5-AEE6-2C8BD83482AA}"></a>Entities : Online
Entities : Online

### <a id="{14619905-B6F7-4994-A049-2D2FDBEA0248}"></a>Entities : Online
See also online likes

### <a id="{652F5D5D-7708-4443-821C-5C305EA0CD02}"></a>Events : Agreement
Events : Agreement

### <a id="{6CD3254D-F304-456e-A517-8F8A84EFD533}"></a>Events : Agreement
Agreement

### <a id="{C9C0DE32-05C8-4f9f-B379-A2624D5353E7}"></a>Events : Attendance
Attendance

### <a id="{DCC61F0C-7C68-4fb5-92AA-3E3416E2ADD0}"></a>Events : Communication
Events : Communication

### <a id="{2A750776-1EBA-485f-968D-E9A2725B8DE2}"></a>Events : Lifecycle
See main model: Lifecycle

### <a id="{2FD02E92-AA73-4419-BC79-CD23E17A2DF1}"></a>Events : Movement
Movement

### <a id="{5A30BDDE-ED08-44e4-8B46-B7C277646EF5}"></a>Events : Trade
Trade

### <a id="{6908DAEB-9557-4648-BA53-CB10E3DD86C8}"></a>Events :Disagreement and War
Events :Disagreement and War

### <a id="{65CA1E00-2890-4c74-AA97-46308E8D3AC5}"></a>IES v4 : Where and When
Where and When

## <a id="{5F2E9C9F-780E-4de3-8B3B-017023D6259C}"></a>All Elements


### <a id="{63409D9A-1779-444a-BF04-23C03B3B2F72}"></a>Accent
An Characteristic whose members are people who all share the same national or regional accent

### <a id="{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"></a>Account
An <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> that is the collection of all transactions between a provider and a customer

### <a id="{19E90CA4-F0EB-4245-826E-EDC278642B41}"></a>AccountAdminEvent
A <a href="#{94CEDBD1-8E3D-4cb4-8155-FBD621DA6A0D}"><font color="#0000ff"><u>BusinessEvent</u></font></a> that an <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a> participates in

### <a id="{7891E893-56DB-4d47-80B4-C78A667767F6}"></a>accountForCard
Relates a <a href="#{848A9E0F-F3B4-47c3-AA7E-2FF6BE92170C}"><font color="#0000ff"><u>BankCard</u></font></a> to the <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a> which the card is issued against.

### <a id="{C93379F2-6B01-4100-ABFA-BD26098AC1CB}"></a>AccountHolder
A <a href="#{38F8B795-0BCE-4945-8C69-8678ED935C1A}"><font color="#0000ff"><u>PersonState</u></font></a> when they hold an <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a>

### <a id="{942FBF46-A7EF-432b-99DD-1E0E3E874C21}"></a>AccountInCommunication
An <a href="#{0BCDB801-1F3B-4496-B04B-95EF545E9445}"><font color="#0000ff"><u>AccountState</u></font></a> (and an <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a>) when an <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a> is involved in communicating. 

### <a id="{A72F0FF1-88F2-4b36-A2C4-26B4B0698A2C}"></a>AccountNumber
The account number for the respective <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a>.

### <a id="{0F9244C3-B2F5-4b8a-AED2-54B7FDAB9578}"></a>accountProvider
The <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that provides the <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a>

### <a id="{0BCDB801-1F3B-4496-B04B-95EF545E9445}"></a>AccountState
A temporal state of an <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a>

### <a id="{A4D8A62A-DC98-410c-80D2-57C98C1E95C0}"></a>Accused
A <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a>'s role as the accused in a <a href="#{024133FE-9D0B-4e5d-A97D-A34B5EA01C41}"><font color="#0000ff"><u>Prosecution</u></font></a>

### <a id="{22D9054C-AE5C-4afe-99D9-3C9D65C86CB9}"></a>aCopyOf
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a Document is a copy of WorkOfDocumentation

Note: Document instances are individual physical documents whereas <a href="#{F0B48978-D4E4-45a4-8238-091A5B714D82}"><font color="#0000ff"><u>WorkOfDocumentation</u></font></a> is the general case of a document - e.g. "War and Peace" vs "my copy of <a href="$element://{D4F568F5-7BC4-489d-94BC-AE1305E5C0C2}"><font color="#0000ff"><u>War</u></font></a> and Peace"

### <a id="{3360DCC9-D39B-4280-8872-2FE122240407}"></a>ActiveEventParticipant
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where the participant is "actively" engaged in the <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a>.

Note: In BORO, EventParticipant would be "Involvement" and ActiveEventParticipant would be "Participation".

### <a id="{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B}"></a>Actor
An <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> that is capable of performing functions - i.e. actively participating in an Event.

### <a id="{7ED8BC7C-A85F-4ed5-AC6F-D640F2DF4B7B}"></a>ActorState
A temporal state of an <a href="#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B}"><font color="#0000ff"><u>Actor</u></font></a>

### <a id="{C90267B5-77A3-4b79-BD0D-7C50C3F4C333}"></a>Address
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> that can be specified by a postal address

### <a id="{3E452516-2523-4a86-974D-1D2251057E6E}"></a>addressRegion
An <a href="#{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate an <a href="#{C90267B5-77A3-4b79-BD0D-7C50C3F4C333}"><font color="#0000ff"><u>Address</u></font></a> is in a <a href="$element://{65D869DB-19EE-4886-98BA-E579C39C4A68}"><font color="#0000ff"><u>RegionOfCountry</u></font></a>

### <a id="{D779F547-C1FB-4d48-9BB8-CB37B9D2F82C}"></a>AdministeredAccount
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a> is administered

### <a id="{FA4DDF04-16DA-4b5c-AE9A-6AB8CD07DCDB}"></a>after
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking two Elements where one ends before the other starts

### <a id="{93F71FAF-AEF4-4e41-8CEB-FC6447B20428}"></a>AgreementExecution
An <a href="#{422B4F1C-DA90-400b-8FFD-43C90B4F10F4}"><font color="#0000ff"><u>AgreementStage</u></font></a> which includes all the ongoing activities that conform to the agreement reached

### <a id="{7A750064-E711-4871-AFC3-39057342FB9E}"></a>AgreementName
A <a href="#{7D7CC966-56EB-4220-A650-A993E598F2E2}"><font color="#0000ff"><u>Name</u></font></a> that is used to refer to an <a href="#{1B39630B-B00F-4def-9C65-48082C4AD2E0}"><font color="#0000ff"><u>EndToEndAgreement</u></font></a>.

### <a id="{422B4F1C-DA90-400b-8FFD-43C90B4F10F4}"></a>AgreementStage
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> which is part of an <a href="#{1B39630B-B00F-4def-9C65-48082C4AD2E0}"><font color="#0000ff"><u>EndToEndAgreement</u></font></a>

### <a id="{01A64A84-7A14-45a5-AAF2-F1AA614D5F30}"></a>Aircraft
A <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> that travels by air

### <a id="{82E3793F-D0D1-40ca-927C-7A6FEF913503}"></a>Airport
A <a href="#{57860A04-0128-4c7e-9BFD-83D3BA432F8C}"><font color="#0000ff"><u>Port</u></font></a> used for air travel

### <a id="{97E2E16A-5D4C-41bd-AF32-8DF2057A35BA}"></a>allAuthorisedAgainst
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking an <a href="#{057C04F9-EB8A-4e21-9CF8-2D98038570FB}"><font color="#0000ff"><u>AuthorisedEventClass</u></font></a> to an <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> to assert that all instances of the AuthorisedEventClass were Events acting upon the ExchangedItem.

Note: this is generally a law-enforcement concern where a warrant (EndToEndAuthorisation) is granted against people, devices, etc. (GrantOfAuthority).



### <a id="{81A1E70D-6ADB-4843-BCA6-C0A710E7716B}"></a>allHaveCharacteristic
An rdfs:subClassOf <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts that all instances of a ClassOfElement share a particular Characteristic or Measure

e.g. all London buses being red, all heavyweight boxers weighing more than 200lbs

### <a id="{6F8504E0-E03C-43fa-AA81-C3341CA551E3}"></a>allHaveDisposition
An rdfs:subClassOf <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts that all instances of a ClassOfElement share a disposition

e.g. all Eurofighters being cable of Mach 2

### <a id="{3D83E15F-ACA8-48e4-8C7B-84580807E06F}"></a>Alliance
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> made up of allies - these could be people or organisations, and the alliance may be quite loose.

### <a id="{7F818F57-2C3B-4629-8EEC-F5F8310AE655}"></a>alliedTo
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one is allied to the other.

### <a id="{518E9B39-58C0-4e89-831D-B6099C3B9892}"></a>allocatedSeatNumber
The seat number associated with the ticket

### <a id="{51B6F4C5-0DA3-437d-9507-38514BC2ABCD}"></a>Altitude
The Length that is the distance above (or below in the case of negative numbers) the surface of the WGS84 spheroid of the respective <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> 

### <a id="{0DF94DE5-68B7-45b4-A106-A11CE06C31B8}"></a>AmountOfMoney
A specific amount of a given currency

### <a id="{324D0329-1299-45cc-92A5-270134E66512}"></a>AmountOfSubstance
The Measure of the stoichiometric quantity of substance (usually measured in moles)

### <a id="{15388C46-262D-4f70-8F65-83758A5AEAF5}"></a>ancestorOf
A Relationship between two <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> Entities that indicates one is and ancestor of the other

Note: was called "relative of" in IES 3.x, but was really only about ancestry, so is changed here. 

### <a id="{1326576A-6240-47b0-AED7-5F3FC4E3884D}"></a>andGroup
The groups (if any) which the requesting user must be a member of in order to access the item. See the EDH specification for further details.

Allowable Values:

See EDH Standard

### <a id="{F8FABF60-63D3-42ae-BA6A-54CFD0C036BF}"></a>ArbitraryOverlap
An <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> whose extent is defined by being the shared overlap of two or more Elements

### <a id="{68BA678C-DCA8-453e-BFCC-D9FB48339D99}"></a>ArbitraryPeriod
A <a href="#{3FDFA898-C340-4279-8B3C-275359D5B02D}"><font color="#0000ff"><u>PeriodOfTime</u></font></a> for which is not delineated by a particular clock period - e.g. not a year, not a month, not a day, not an hour, etc. Instead it is one which is most clearly specified in terms of start and end that are <a href="#{2173F463-524C-457c-B106-51322F64F122}"><font color="#0000ff"><u>ParticularPeriods</u></font></a>.

### <a id="{C6BA7464-C00E-4ff6-AE7B-9CE9D4E08FDF}"></a>areaOfCoverage
The area over which the TravelCard is valid 

Examples:

London � Zone 1
London � All Zones

### <a id="{D8D7184C-2F7B-4a5d-AA8F-7EE7B5A04F94}"></a>Arrest
A <a href="#{3876B81C-E316-4e11-A6C4-8024E52F769B}"><font color="#0000ff"><u>LawEnforcement</u></font></a> <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> is arrested

### <a id="{B870A3B5-32FA-4aaf-86F1-7DB674585F3A}"></a>Arrested
A <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>'s role when arrested

### <a id="{5B3F41C3-91CC-442f-A4F8-615E77751734}"></a>ArrestingOfficer
A <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>'s role as arresting officer

### <a id="{F2C03DA3-B554-4bde-A0DE-EFB5BEE19C56}"></a>Arrival
A <a href="#{892345CD-9FA7-4982-978D-B6D3ABAE839C}"><font color="#0000ff"><u>BoundingState</u></font></a> that marks the end of a <a href="#{95B5ACC4-956A-4b29-AB9E-BDCD12EF319F}"><font color="#0000ff"><u>Movement</u></font></a> event

The date/time of the arrival can be specified using the <a href="#{2F08EF25-A5C8-48ad-85E3-903DB008AA19}"><font color="#0000ff"><i><u>inPeriod</u></i></font></a><i> </i>relationship. 

### <a id="{669E3CD0-CD9D-496c-A711-ECDE3F589012}"></a>assessed
An owl:objectProperty that links an AssesToBeTrue to the rdfs:Resource that is assessed to be true.

### <a id="{6A1C6C65-D671-4ea3-9184-044AE2A802CF}"></a>assessedToBeTheSameAs
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts two ExchangedItems that may have been previously judged to be different are in fact the same thing. 

WARNING:  by "the same" we mean they occupy the same space for the same period of time - i.e. not two different things in the same place at different times, and not the same physical item at two different periods of time. The <a href="#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E}"><font color="#0000ff"><u>Identifier</u></font></a> and <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> patterns should do most of what is needed here, and it is <i>extremely rare </i>that this would ever be needed. Do not use unless absolutely necessary. 

### <a id="{80F9B97D-2C7F-4978-83A3-BE934DD4E1FF}"></a>Assessor
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an Actor assesses something to be true.

### <a id="{7150208D-A02E-45ed-8279-44843F4DA897}"></a>AssessToBeTrue
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where a fact is assessed to be true by a Actor (i.e. a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> or Device)

An AssessToBeTrue shall have one and only one <a href="#{04F797E7-9B5C-48c5-A50D-A14CFF7725DE}"><font color="#0000ff"><u>hmlConfidence</u></font></a> attribute (i.e. this is mandatory)

### <a id="{40231334-5ACC-4dd4-A8C1-05012E2170E0}"></a>Asset
An <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> that is either man-made (or defined - see <a href="#{487778E0-4BD7-4d9a-B7F7-63731478E1A2}"><font color="#0000ff"><u>Rights</u></font></a>) or whose extent is defined in such a way as to specify ownership - e.g. a parcel of real estate

### <a id="{CA196722-9531-4eb4-A8CF-B9A5145CDCFD}"></a>AssetState
A temporal state of an <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a>

### <a id="{2E464C7F-FC0B-4dcc-9B1C-5DCA87B4CE3A}"></a>associatedCarrier
The Organisation that provides the transport specified on the <a href="#{0BC61540-2AFB-42e6-A845-79771EE0268D}"><font color="#0000ff"><u>Ticket</u></font></a>

### <a id="{022535DE-2100-420b-B4BC-10465DEEEC3C}"></a>associatedPersonName
The name of the Person which is associated with the Entity

This may be the name of an account holder, the name printed on ID, tickets, etc.

Note in 3.x, this was several different attributes:
accountHolderName on FinancialAccount
nameOnLicense, etc. on IdentityDocument
ticketHolderName on Ticket

### <a id="{73D38C0E-3291-4de9-8920-F37980CB3A9E}"></a>Attacker
Relates a <a href="#{8787BE51-8FE0-4d76-97B4-608311434F5B}"><font color="#0000ff"><u>MilitaryAttack</u></font></a> to the <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> conducting the attack

### <a id="{626D5F2C-9153-40f4-9F2A-393B6DB072D3}"></a>Attendance
A <a href="#{8404464D-3904-4c59-AE0E-B3FAFB46AC4E}"><font color="#0000ff"><u>Presence</u></font></a> where the <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> is present

Note - we may not know the identity of the person, so would just create only the <a href="#{626D5F2C-9153-40f4-9F2A-393B6DB072D3}"><font color="#0000ff"><u>Attendance</u></font></a> (<a href="$element://{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a>). This allows the <a href="$element://{98BDD06F-1BD7-42b8-B338-20A198BCF90A}"><font color="#0000ff"><u>model</u></font></a> to grow as more information is discovered without recourse to using sameAs relationships.

### <a id="{4A8E5877-32DF-428f-9A60-6AC3D083FFCA}"></a>attribute
A feature or property of an ExchangedItem

Note: In IES4 it is important to distinguish between names and attributes - attribute should never be used to identify or name something - for that, use Name or Identifier.

### <a id="{89953404-8A71-46ef-8F7B-90C12EE286FD}"></a>AtWar
An <a href="#{F12D45EA-66D5-4016-BDF7-E1CD8F48CCF5}"><font color="#0000ff"><u>InDisagreement</u></font></a> where the parties have declared war

### <a id="{8177A2FB-CA54-4dc5-9884-33FBA660B174}"></a>AuthorisationDocument
A <a href="#{F0B48978-D4E4-45a4-8238-091A5B714D82}"><font color="#0000ff"><u>WorkOfDocumentation</u></font></a> that provides permission

### <a id="{1D6BAE08-B8F1-4eee-928E-991B3B46EADF}"></a>AuthorisationRequest
An <a href="#{2D5069F2-FE77-477f-A607-FA6458E64173}"><font color="#0000ff"><u>AuthorisationStage</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> requests authorisation to act from another <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a>

### <a id="{81BF6EA6-996D-4148-8F5D-8B41156637F6}"></a>AuthorisationRequester
An <a href="#{3360DCC9-D39B-4280-8872-2FE122240407}"><font color="#0000ff"><u>ActiveEventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> requests authority to act 

### <a id="{8E4CC036-C4C5-4222-8532-9B6C53EEC56E}"></a>AuthorisationReviewer
An <a href="#{3360DCC9-D39B-4280-8872-2FE122240407}"><font color="#0000ff"><u>ActiveEventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> reviews an <a href="#{1D6BAE08-B8F1-4eee-928E-991B3B46EADF}"><font color="#0000ff"><u>AuthorisationRequest</u></font></a>

### <a id="{2D5069F2-FE77-477f-A607-FA6458E64173}"></a>AuthorisationStage
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> which is part of an <a href="#{D75F18D1-95D6-481b-84D5-F8D7F3A5A389}"><font color="#0000ff"><u>EndToEndAuthorisation</u></font></a>

### <a id="{F69279D2-BA11-4a31-8739-0D91EF5B9BEF}"></a>AuthorisedActor
An <a href="#{3360DCC9-D39B-4280-8872-2FE122240407}"><font color="#0000ff"><u>ActiveEventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> is granted authority to act in a <a href="#{F5EAAEEE-C0B2-469f-9048-3E0731ED8342}"><font color="#0000ff"><u>GrantOfAuthority</u></font></a> 

### <a id="{057C04F9-EB8A-4e21-9CF8-2D98038570FB}"></a>AuthorisedEventClass
A ClassOfEvent where the type activity described is either authorised or required to be authorised.

An instance of an AuthorisedEventClass will most often also be a TimeBoundedClass as it is rare to see requests or grants of authority with no time limit. 

An AuthorisedEventClass will usually be of the form of "Event type A against Entity X" = e.g. "Arrest of John Smith", "Surveillance of 23 Acacia Gardens". The link from this class to the entity involved is via the allAuthorisedAgainst relationship.

### <a id="{466DCDFB-B642-468b-A47A-E83291A86C6B}"></a>Authoriser
An <a href="#{3360DCC9-D39B-4280-8872-2FE122240407}"><font color="#0000ff"><u>ActiveEventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> acts as the authoriser (sign off) in a <a href="#{F5EAAEEE-C0B2-469f-9048-3E0731ED8342}"><font color="#0000ff"><u>GrantOfAuthority</u></font></a> 

### <a id="{A2DA918D-843C-43c9-A974-4795601E9D65}"></a>authorisesAccessTo
The Event for which the respective Ticket applies.

### <a id="{4E10343E-8350-4354-B3DB-A7F74B4535EF}"></a>Bank
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that holds a banking license and can conduct financial transactions on behalf of customers

### <a id="{02E3C3B8-8650-4867-8390-823E4B3360E6}"></a>BankBranch
An operating division of a <a href="#{4E10343E-8350-4354-B3DB-A7F74B4535EF}"><font color="#0000ff"><u>Bank</u></font></a>, usually a high street branch, but might also be the online arm of a Bank

### <a id="{848A9E0F-F3B4-47c3-AA7E-2FF6BE92170C}"></a>BankCard
A <a href="#{9882D901-1B22-4b89-81D1-031F840A20D0}"><font color="#0000ff"><u>PaymentArtefact</u></font></a> that is a physical card used for making financial transactions.

Note: when used online, the accompanying Fan

### <a id="{2C441F0A-635D-41ef-B8CC-96AA07958F8E}"></a>beginBoundOfClass
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking a <a href="#{E7A659A5-9059-4ea5-8FAB-8A29AFC47D9A}"><font color="#0000ff"><u>TimeBoundedClass</u></font></a> to the <a href="#{2173F463-524C-457c-B106-51322F64F122}"><font color="#0000ff"><u>ParticularPeriod</u></font></a> that marks the beginning bound date of its instances

### <a id="{4457E8AF-EDBD-4ef1-B62B-59037829B961}"></a>BirthCertificate
An <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a> issued to prove the data and place of birth of a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>

### <a id="{CFE53096-32FC-47c8-98BA-950EE6F988CB}"></a>BirthState
A <a href="#{892345CD-9FA7-4982-978D-B6D3ABAE839C}"><font color="#0000ff"><u>BoundingState</u></font></a> that marks the beginning of a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>'s life.

The location of the birth can be specified using <a href="#{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><i><u>inLocation</u></i></font></a>

The date/time of the birth can be specified using the <a href="$element://{2F08EF25-A5C8-48ad-85E3-903DB008AA19}"><font color="#0000ff"><i><u>inPeriod</u></i></font></a><i> </i>relationship. 

### <a id="{683E5B90-2514-4342-AE34-894D2DAC2AF0}"></a>BoardingCardNumber
The number of the boarding card issued to the Passenger. 

### <a id="{22AB6EA2-B088-4ef6-AE3A-5843FBA5C8AE}"></a>Book
A <a href="#{F0B48978-D4E4-45a4-8238-091A5B714D82}"><font color="#0000ff"><u>WorkOfDocumentation</u></font></a> that is a published book

### <a id="{53C6BCA9-4D66-4bac-B946-0A8541CF510A}"></a>BookedPassenger
A <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>'s involvement as a booked traveller in a <a href="#{76DC9A0C-F6E8-4ff4-ADD6-072DC1EBE3AB}"><font color="#0000ff"><u>TravelBooking</u></font></a>

### <a id="{0AF87601-5B3E-4c5e-8149-D0D3C0073C42}"></a>BookingAgent
A <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a>'s involvement as the facilitator of a <a href="#{76DC9A0C-F6E8-4ff4-ADD6-072DC1EBE3AB}"><font color="#0000ff"><u>TravelBooking</u></font></a>

### <a id="{61BDEBA6-BE87-44e3-A1C7-246D0CE60ADC}"></a>BookingPayment
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8}"><font color="#0000ff"><u>AmountOfMoney</u></font></a> in cash is used as payment in a <a href="#{76DC9A0C-F6E8-4ff4-ADD6-072DC1EBE3AB}"><font color="#0000ff"><u>TravelBooking</u></font></a>.

When neither card nor cash is used, there will be an accompanying <a href="$element://{D94ED70F-8CCA-4c6e-8AE5-65450BBA62D7}"><font color="#0000ff"><u>MoneyTransfer</u></font></a>

### <a id="{D31E959A-6354-40e7-8370-1FE5246624AD}"></a>BookingReference
An <a href="#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E}"><font color="#0000ff"><u>Identifier</u></font></a> that is  notionally unique number that is allocated to a <a href="#{76DC9A0C-F6E8-4ff4-ADD6-072DC1EBE3AB}"><font color="#0000ff"><u>TravelBooking</u></font></a>.

Note that Booking Reference Numbers are recycled and so are not unique in their own right. When combined with the BookingDate it is potentially possible to identify a specific booking.

### <a id="{C52879E4-919A-4dee-82EB-3CB11DD69E56}"></a>bookingType
Relates a <a href="#{76DC9A0C-F6E8-4ff4-ADD6-072DC1EBE3AB}"><font color="#0000ff"><u>TravelBooking</u></font></a> to a <a href="#{44D4DD7C-201A-447d-8BCE-C8B3E3E6A890}"><font color="#0000ff"><u>ClassOfTravelBooking</u></font></a> to indicate the method of booking

### <a id="{892345CD-9FA7-4982-978D-B6D3ABAE839C}"></a>BoundingState
A <a href="#{6E5AF4BB-BB7F-4387-A7BB-476B81FEC103}"><font color="#0000ff"><u>ContinuousState</u></font></a> that occurs at the beginning or end of an <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> 

The date/time of the state can be specified using the <a href="#{2F08EF25-A5C8-48ad-85E3-903DB008AA19}"><font color="#0000ff"><i><u>inPeriod</u></i></font></a><i> </i>relationship. 

### <a id="{012F7F29-4F8E-4263-8224-126050EE175F}"></a>BranchCode
In identifier for a <a href="#{02E3C3B8-8650-4867-8390-823E4B3360E6}"><font color="#0000ff"><u>BankBranch</u></font></a> - In the UK this is often referred to as the Sort Code.

### <a id="{62675B63-9169-4f05-9993-E1B17540A6C1}"></a>branding
A brand or logo that is represented on an Entity

e.g. some bank cards are branded by a car manufacturer, etc. but actually operated by a bank

### <a id="{94CEDBD1-8E3D-4cb4-8155-FBD621DA6A0D}"></a>BusinessEvent
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> that is commercial or administrative in nature

### <a id="{F50BAD6D-EBE0-4fd8-B54C-3E24A62491A6}"></a>Callee
An <a href="#{A5713B2C-E098-4dd2-BD46-42DA51899FEA}"><font color="#0000ff"><u>PartyInCommunication</u></font></a> where the communicating party is called in an <a href="#{6D5E11EE-C61A-4e38-913F-BBAF2A34A288}"><font color="#0000ff"><u>InteractiveCommunication</u></font></a>

### <a id="{03DDC2F5-F961-47c2-B8F8-B27A752AEC34}"></a>Caller
An <a href="#{A5713B2C-E098-4dd2-BD46-42DA51899FEA}"><font color="#0000ff"><u>PartyInCommunication</u></font></a> where the communicating party is the caller in an <a href="#{6D5E11EE-C61A-4e38-913F-BBAF2A34A288}"><font color="#0000ff"><u>InteractiveCommunication</u></font></a>

### <a id="{25F4F685-3931-4cdc-AF43-1A9194BBE15D}"></a>Callsign
In broadcasting and radio communications, a call sign (also known as a call name or call letters � and historically as a call signal) is a unique designation for a transmitting station.

### <a id="{91D62F08-ED05-4558-9321-368712A34A30}"></a>Capability
A DispositionalClass where all the instances share the same capability

Example: Vehicles capable of Mach 2

### <a id="{087F3453-B1D7-41e6-B79F-31B123ED0D68}"></a>CardNumber
An <a href="#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E}"><font color="#0000ff"><u>Identifier</u></font></a> that is the long number on the face of the card (<a href="#{9882D901-1B22-4b89-81D1-031F840A20D0}"><font color="#0000ff"><u>PaymentArtefact</u></font></a>)

### <a id="{CF6B72ED-DF58-42e1-A72A-1F047287B80D}"></a>cardType
The type of a <a href="#{9882D901-1B22-4b89-81D1-031F840A20D0}"><font color="#0000ff"><u>PaymentArtefact</u></font></a>

### <a id="{1B9C8EB0-69A7-4fe7-8358-0F6067439C42}"></a>CardUsed
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{9882D901-1B22-4b89-81D1-031F840A20D0}"><font color="#0000ff"><u>PaymentArtefact</u></font></a> is participant in a <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a>

### <a id="{91DC18F6-3E35-411c-814D-5ACEE83BE316}"></a>Carrier
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> participates in a <a href="#{F428ADA5-2349-4cd0-815F-8F768B08C6E6}"><font color="#0000ff"><u>Delivery</u></font></a> as a carrier

### <a id="{76C31798-780C-41b0-A985-0AE3B1C3A478}"></a>carrierService
The Organisation that provides the transport specified on the <a href="#{0BC61540-2AFB-42e6-A845-79771EE0268D}"><font color="#0000ff"><u>Ticket</u></font></a>

### <a id="{F5E2BCD3-4529-42f2-9ED9-95801B42ED3F}"></a>CarTravel
A <a href="#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74}"><font color="#0000ff"><u>TravelService</u></font></a> by car

### <a id="{62A9AA44-6C36-448b-805F-E13203CFB4FC}"></a>CashPayment
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8}"><font color="#0000ff"><u>AmountOfMoney</u></font></a> in cash is used as payment in a <a href="#{0A9A9F7D-A6F1-4629-BD2B-7990D2D36493}"><font color="#0000ff"><u>Purchase</u></font></a>.

When neither card nor cash is used, there will be an accompanying <a href="$element://{D94ED70F-8CCA-4c6e-8AE5-65450BBA62D7}"><font color="#0000ff"><u>MoneyTransfer</u></font></a>

### <a id="{61D00F47-977E-43f6-BD30-77CBAAA74CC1}"></a>Casualty
Relates a <a href="#{8787BE51-8FE0-4d76-97B4-608311434F5B}"><font color="#0000ff"><u>MilitaryAttack</u></font></a> to a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> who was injured or killed in the attack

### <a id="{18EB7B22-5927-4b0e-98A8-638D28BDCF87}"></a>CBRadioHandset
A <a href="#{18EB7B22-5927-4b0e-98A8-638D28BDCF87}"><font color="#0000ff"><u>CommunicationsDevice</u></font></a> used to hold radio conversations on frequencies allocated as "Citizen Band"

### <a id="{9D4A1395-8687-4f0b-BC5D-61A756210B4D}"></a>CellularBaseStation
A <a href="#{F02CFF55-12A7-4308-9A60-E2353DE5BE58}"><font color="#0000ff"><u>RadioMast</u></font></a> that is used for cellular communication



### <a id="{7FA15F56-86C4-47f4-9032-999C17703368}"></a>ChangeOfGovernment
A <a href="#{3A0E6FDD-5B3B-4092-9549-C05E8A5FED41}"><font color="#0000ff"><u>PoliticalEvent</u></font></a> where one <a href="#{D62DDBB8-53FC-405a-BC43-89CA337563A0}"><font color="#0000ff"><u>Government</u></font></a> is replaced by another.

### <a id="{A7F266E8-B1CB-4b9b-8AF1-1EF2A7D8F5EE}"></a>Characteristic
A ClassOfElement whose instances all share a common property - e.g. they are all the same colour, mass, etc. 

### <a id="{48223A62-12E6-4953-8F80-8C7A48151825}"></a>charters
A Relationship between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and the <a href="#{7693D2C9-0F06-4005-BB8D-B5B572B2281A}"><font color="#0000ff"><u>Transit</u></font></a> they have chartered.

### <a id="{87308A03-5C79-4d94-99E1-660042AC7929}"></a>CheckIn
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> checks in to a hotel or <a href="#{7693D2C9-0F06-4005-BB8D-B5B572B2281A}"><font color="#0000ff"><u>Transit</u></font></a>. This also includes swiping tickets to use public transport

The location of the <a href="$element://{87308A03-5C79-4d94-99E1-660042AC7929}"><font color="#0000ff"><u>CheckIn</u></font></a> is specified using a <a href="$element://{60A37745-8DD5-4e4c-9A4C-6957F71AD971}"><font color="#0000ff"><u>happensIn</u></font></a> relationship.

The CheckIn may be part of another Event - e.g. an <a href="$element://{78C33499-CD14-43cb-82AE-93A0F8CF022B}"><font color="#0000ff"><u>EntertainmentEvent</u></font></a> or <a href="$element://{7693D2C9-0F06-4005-BB8D-B5B572B2281A}"><font color="#0000ff"><u>Transit</u></font></a> event. Simply use the <a href="$element://{CD85D7F7-783B-4d06-B023-56DBBDDC02DC}"><font color="#0000ff"><u>isPartOf</u></font></a> <a href="$element://{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to specify this.

### <a id="{7E0C25C9-DD3A-463e-A481-7CA4EA4AC8C5}"></a>CinemaTicket
An <a href="#{96989C30-99CC-4606-A8D4-DFD9421F0E34}"><font color="#0000ff"><u>EntertainmentTicket</u></font></a> that permits attendance at a cinema

### <a id="{0077DA88-19EF-4c4c-B6C0-D418D5D77256}"></a>ClassOfAccount
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a>

### <a id="{E5C27DA8-7DF1-49ea-A9EC-ABE17AFD2047}"></a>ClassOfAmountOfMoney
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8}"><font color="#0000ff"><u>AmountOfMoney</u></font></a>

### <a id="{F999F59A-7C7B-40f3-8F86-5B2592889E95}"></a>ClassOfAsset
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a>- i.e. a <a href="#{D1B2FB30-36CA-4012-B85F-514E270BF541}"><font color="#0000ff"><u>ClassOfEntity</u></font></a> whose instances are classes of Asset

Examples:

* Vauxhall Insignia, VW Golf
* Smartphone
* Apple iPhone 6S

### <a id="{85305668-DE1A-454a-87EE-346A221E846C}"></a>ClassOfClassOfElement
An <a href="#{58C6DE35-5E57-4009-A6CE-69C889B31D82}"><font color="#0000ff"><u>rdfs:Class</u></font></a> and an <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> whose instances are classes of classes of <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a>

### <a id="{1F9AC8FE-3862-48d6-A3DC-E429B08D2B26}"></a>ClassOfClassOfEntity
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{D1B2FB30-36CA-4012-B85F-514E270BF541}"><font color="#0000ff"><u>ClassOfEntity</u></font></a>

### <a id="{69868D83-C3BD-4877-AB5C-374B4C6F4A7E}"></a>ClassOfCriminalActivity
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{43E58528-16E4-48b3-8F13-10500879EA83}"><font color="#0000ff"><u>CriminalActivity</u></font></a>

Example instances:

* Burglary
* Fraud
* Murder
* Driving sheep across London Bridge if not a freeman of the City
* Being Welsh inside the walls of Chester outside daylight hours

### <a id="{09F9136C-9069-47ec-A58E-FC26CF9BA55E}"></a>ClassOfDevice
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a>- i.e. a <a href="#{D1B2FB30-36CA-4012-B85F-514E270BF541}"><font color="#0000ff"><u>ClassOfEntity</u></font></a> whose instances are classes of Device

Examples:

* Smartphone
* Apple iPhone 6S

### <a id="{3C13E07D-5796-4d03-9EBC-C75277E87CA4}"></a>ClassOfElement
An <a href="#{58C6DE35-5E57-4009-A6CE-69C889B31D82}"><font color="#0000ff"><u>rdfs:Class</u></font></a> and an <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> whose instances are classes of <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a>

Examples:

<ul>
	<li>Human groupings (e.g. Nigerian Women, British Men, Righthanded people, English Speakers);</li>
	<li>Political Ideologies</li>
	<li>Weapons</li>
	<li>Days of the week</li>
	<li>Standard procedures</li>
	<li>etc.</li>
</ul>

### <a id="{D1B2FB30-36CA-4012-B85F-514E270BF541}"></a>ClassOfEntity
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Entity</u></font></a> - i.e. a <a href="#{3C13E07D-5796-4d03-9EBC-C75277E87CA4}"><font color="#0000ff"><u>ClassOfElement</u></font></a> whose instances are classes of Entity

Examples:

� Human groupings (e.g. Nigerian Women, British Men, Righthanded people, English Speakers);
� Weapons
� Etc.

### <a id="{4EA194C6-BBF9-45ab-85DE-5802D8C3A531}"></a>ClassOfEvent
An <a href="#{3C13E07D-5796-4d03-9EBC-C75277E87CA4}"><font color="#0000ff"><u>ClassOfElement</u></font></a> whose instances are classes of <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a>. This is the <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of Event.

Examples:

* Conference
* Football Match
* Annual General <a href="$element://{6445E51F-3DDF-4dcf-ABDF-3ED123D53188}"><font color="#0000ff"><u>Meeting</u></font></a>

### <a id="{901334E9-238C-4d05-8F85-FE9A8E537BA1}"></a>ClassOfFinancialAccount
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a>

Examples:

* Savings Account
* Current Account
* Credit Card <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a>

### <a id="{CCC8FA06-CDA8-491d-BFFC-0A88D6A565B1}"></a>ClassOfIndividualDocument
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{0F327324-6B4E-40b1-B96B-97A334BA5E4A}"><font color="#0000ff"><u>IndividualDocument</u></font></a>

### <a id="{4520A91C-D956-46c1-9A81-93C4C0B12880}"></a>ClassOfMeasureValue
A ClassOfRepresentation that is the powertype of MeasureValue

### <a id="{F1AACA77-BA24-41cb-9AB8-7AF9C1B9971D}"></a>ClassOfMoneyTransfer
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{D94ED70F-8CCA-4c6e-8AE5-65450BBA62D7}"><font color="#0000ff"><u>MoneyTransfer</u></font></a>

Examples:

* BACS
* CHAPS
* Paypal payment

### <a id="{FBE0CFC1-43C4-47e2-9EFE-20E291A1697C}"></a>ClassOfOnlineService
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{27BEFD0A-B30B-47db-B863-13E48D1172F9}"><font color="#0000ff"><u>OnlineService</u></font></a>

### <a id="{64CE6FEA-7B05-4813-BD55-D56C02A54486}"></a>ClassOfOperationalEvent
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{59121C21-38E4-4224-8C2D-4D3E94A3A0D9}"><font color="#0000ff"><u>OperationalEvent</u></font></a>

Examples:

* Counter-Narcotics Operation
* Murder Investigation


### <a id="{5B21F148-72C1-45e6-A3E3-F2D8B33729D3}"></a>ClassOfOrganisation
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a>

Note: care should be exercised when using ClassOfOrganisation - it should only be used for classifications that apply to the whole life of the organisation.

### <a id="{46144D4F-5A9F-432b-B533-26C0399DBB34}"></a>ClassOfPaymentArtefact
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{9882D901-1B22-4b89-81D1-031F840A20D0}"><font color="#0000ff"><u>PaymentArtefact</u></font></a>

Examples:

* Visa
* Oyster
* Selfridges Store Card

### <a id="{2A62C672-1757-4a2d-874B-C099C9DEC416}"></a>ClassOfPerson
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>

### <a id="{92CDC810-9DFA-476b-A2E7-33121F65905B}"></a>ClassOfPersonState
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{38F8B795-0BCE-4945-8C69-8678ED935C1A}"><font color="#0000ff"><u>PersonState</u></font></a>

### <a id="{4FFEB84D-B823-4829-9A3A-ADE51EF0F0F5}"></a>ClassOfRepresentation
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a>

### <a id="{9FC2431D-63A4-4e1b-8D31-2BCD125853D9}"></a>ClassOfResponsibleActor
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> 

### <a id="{9CEF4F29-5619-4d8f-A9DE-8CB43270C7F5}"></a>ClassOfResponsibleActorState
A <a href="#{0358DDAB-D22C-4ee5-8F9A-CF18F3E432BD}"><font color="#0000ff"><u>ClassOfState</u></font></a> that is the <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> 

### <a id="{0358DDAB-D22C-4ee5-8F9A-CF18F3E432BD}"></a>ClassOfState
A <a href="#{3C13E07D-5796-4d03-9EBC-C75277E87CA4}"><font color="#0000ff"><u>ClassOfElement</u></font></a> whose instances are classes of States. This is the <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of State.

Examples:

* Roles

### <a id="{44D4DD7C-201A-447d-8BCE-C8B3E3E6A890}"></a>ClassOfTravelBooking
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{76DC9A0C-F6E8-4ff4-ADD6-072DC1EBE3AB}"><font color="#0000ff"><u>TravelBooking</u></font></a>

Examples:

INTERNET Booking
TELEPHONE Booking

### <a id="{2BADCB50-7A19-4d7b-A46E-8369F8B00D57}"></a>ClassOfTravelVisa
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{C066EEB4-91AF-4ee6-BB02-44A49087946B}"><font color="#0000ff"><u>TravelVisa</u></font></a>

### <a id="{B1AAE4CA-CAB0-475f-B7D3-8CED404B1FC6}"></a>ClassOfWebResource
The <a href="#{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"><font color="#0000ff"><u>powertype</u></font></a> of <a href="#{46D508B4-F1CC-45d7-9E4B-BA8A3C88D82A}"><font color="#0000ff"><u>WebResource</u></font></a>

### <a id="{2A5450A7-5B26-4605-A109-5CB26DD9A70F}"></a>CloseAccount
An <a href="#{19E90CA4-F0EB-4245-826E-EDC278642B41}"><font color="#0000ff"><u>AccountAdminEvent</u></font></a> where an <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a> is shut down.

### <a id="{9E413787-42C8-4cd4-B7B1-63E38F6A02D9}"></a>coercedBy
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one (range) coerces the other (domain).

### <a id="{3524D10D-D9B0-416d-ADED-D5AAEB99DD09}"></a>CoLocation
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where the activity is uncertain, but it is known that some Entities were present

Note: whilst colocation can be easily inferred from data, sometimes it's important to call out specific instances where entities of interest were in the same place at the same time.

### <a id="{B10D22FB-1D6A-47c9-B1C0-E870D43A5C52}"></a>Colour
An Characteristic whose members all have the same colour

### <a id="{1456439C-65C9-4a39-A743-09A7D0FBF248}"></a>CommercialOrganisation
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that is run for profit

### <a id="{6698805F-F492-4f1f-954C-E1EB3C53E148}"></a>Communication
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where two or more parties interact and exchange information

### <a id="{8300451C-1DF9-4545-9174-D8AA69C58CCD}"></a>CommunicationsAccount
An <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a> of the communications transactions provided to a customer

### <a id="{20BB42F0-3F2D-4bb7-88DD-F4D05377D59B}"></a>CommunicationsAccountState
A temporal state of a <a href="#{8300451C-1DF9-4545-9174-D8AA69C58CCD}"><font color="#0000ff"><u>CommunicationsAccount</u></font></a>

### <a id="{32EB46A5-0FA4-44e9-A9E9-9424E80BDE91}"></a>CommunicationsDevice
A <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a> that provides an endpoint for communications � e.g. mobile telephone, landline, satellite phone, CB Radio, etc.

### <a id="{A82378B9-9774-46b9-9845-CC75BE882F06}"></a>CommunicationsIdentifier
An <a href="#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E}"><font color="#0000ff"><u>Identifier</u></font></a> for the end-point of a communication 

### <a id="{DF388418-F296-46a5-A2A3-4297F084DD07}"></a>CommunicationsIdentifierRange
A specified range of identifiers for the end-points of a communication.

### <a id="{98421510-0A8A-4942-9743-191EA0DCA9E6}"></a>Competition
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where the participants are competing with each other

### <a id="{763C82F1-5CE0-4652-8A93-D56D93DE1544}"></a>Competitor
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> is in competition

### <a id="{8FF9DE7F-137B-4a03-AB24-7D84FCFB99C0}"></a>ConcertTicket
An <a href="#{96989C30-99CC-4606-A8D4-DFD9421F0E34}"><font color="#0000ff"><u>EntertainmentTicket</u></font></a> where the <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> is a concert

### <a id="{B59AB165-6D9C-423f-9CB2-85B4E1B37D93}"></a>ConferenceHost
A <a href="#{5C76FE3F-FE06-4abc-B495-0D4F35FB5252}"><font color="#0000ff"><u>ConferenceParticipant</u></font></a> that is in the role of host

### <a id="{5C76FE3F-FE06-4abc-B495-0D4F35FB5252}"></a>ConferenceParticipant
An <a href="#{A5713B2C-E098-4dd2-BD46-42DA51899FEA}"><font color="#0000ff"><u>PartyInCommunication</u></font></a> that is a participant in a <a href="#{6EAC8930-3D16-4e44-9706-989BDF6564A5}"><font color="#0000ff"><u>TeleConference</u></font></a>

### <a id="{45FE24B3-B146-4199-B760-C1150CEF9AB2}"></a>confidence
A qualitative or quantitative indication of the confidence of an AssessToBeTrue 

### <a id="{B54BB629-E007-4099-BC01-B512894F1E89}"></a>contactDetailsOnBooking
The contact details of the Person making the booking as recorded on the actual Travel Booking.

Note that if these details can be parsed to identify the contact telephone number, contact email address etc. then they should be mapped as instances of <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to the respective <a href="#{A82378B9-9774-46b9-9845-CC75BE882F06}"><font color="#0000ff"><u>CommunicationsIdentifier</u></font></a> (TelephoneNumber, EmailAddress, etc.).

### <a id="{8CA5551A-EAEB-4145-A75F-2E7D7DAD5A57}"></a>ContentCategory
An <a href="#{1F9AC8FE-3862-48d6-A3DC-E429B08D2B26}"><font color="#0000ff"><u>ClassOfClassOfEntity</u></font></a> whose instances collect together all Representations that have similar content.

Examples:

* Fiction
* Non-Fiction
* Financial Information
* Extremist Media

### <a id="{6E5AF4BB-BB7F-4387-A7BB-476B81FEC103}"></a>ContinuousState
A <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> that is temporally continuous - i.e. it is not a <a href="#{52DB371E-71AC-4812-B3CF-0FD7D73F1BB0}"><font color="#0000ff"><u>DiscontinuousState</u></font></a>

### <a id="{0876AE1F-7202-41d9-A00F-208B118BBF79}"></a>contractedTo
A <a href="#{181AAC84-26CE-4531-AC32-A73B8FD8B858}"><font color="#0000ff"><u>worksFor</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (domain) is contracted to another ResponsibleActor (range).

### <a id="{C81B6EAD-8494-45ca-928C-21CB6D395C39}"></a>Cookie
An <a href="#{54500458-51CF-46b5-A5A3-14B1D5C7F755}"><font color="#0000ff"><u>OnlineArtefact</u></font></a> that is stored on a <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a> to enable continuity of session, log-in, or simply to track activity online.

Cookies tend to be ephemeral, an unique to a device, so no states are required. Simply use <a href="#{76D8EA41-E338-4db5-BB30-D642CF0F90EB}"><font color="#0000ff"><u>cookieOnDevice</u></font></a> <a href="$element://{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> mark the stand and end BoundingStates of the Cookie. 

### <a id="{76D8EA41-E338-4db5-BB30-D642CF0F90EB}"></a>cookieOnDevice
Relates a <a href="#{C81B6EAD-8494-45ca-928C-21CB6D395C39}"><font color="#0000ff"><u>Cookie</u></font></a> to the <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a> it is installed on.

Note: there is usually no need for states here as the Cookie itself has begin and end times.

### <a id="{24E8B958-284F-4be2-AACD-A7B2A94B97D4}"></a>cookieOriginSite
Relates a <a href="#{C81B6EAD-8494-45ca-928C-21CB6D395C39}"><font color="#0000ff"><u>Cookie</u></font></a> to the <a href="#{79098C74-E063-4c45-886D-D0B88A48E954}"><font color="#0000ff"><u>Webpage</u></font></a> from which it originated.

### <a id="{F650B9E3-2669-455e-B20C-92737CFD9A08}"></a>Cooperation
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where the participants are cooperating with each other

### <a id="{2B96182A-9363-4c6a-BE62-132B072A7520}"></a>Cooperator
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> is in <a href="#{F650B9E3-2669-455e-B20C-92737CFD9A08}"><font color="#0000ff"><u>Cooperation</u></font></a>

### <a id="{92EBA9B9-48C2-4082-9FE5-603977BD6846}"></a>Country
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> whose land extent / borders are recognised as a <a href="#{92EBA9B9-48C2-4082-9FE5-603977BD6846}"><font color="#0000ff"><u>Country</u></font></a> by the International Standards <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> (ISO)

Note: this is simply the land, any buildings on it, and the airspace and ground beneath as recognised by the ISO definition. It does not include the nationals of the Country, its Government, etc. 

### <a id="{D33498ED-B6A0-41ea-864F-CE95E2B1E010}"></a>countryOfRegistration
The Country in which the respective <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is registered / recognised.

### <a id="{8C3F2C71-C7A2-414a-85C2-DFCD2D91D8E5}"></a>countryUsingDialCode
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{79C84EC1-83EC-45a8-A3CE-F88CFFBF9434}"><font color="#0000ff"><u>TelephoneCountryCode</u></font></a> and a <a href="#{92EBA9B9-48C2-4082-9FE5-603977BD6846}"><font color="#0000ff"><u>Country</u></font></a> that uses that code.

Note:  more than one Country may use the same code, and in rare cases a given Country may have more than one code.

### <a id="{32A625FA-3159-4b36-B551-3742BA11C7A8}"></a>cousinOf
A Relationship between two <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> Entities that indicates one is the cousin of the other

### <a id="{AF60517B-E4EF-48ca-BE0F-56E0A89660FD}"></a>Create
A <a href="#{FA07AB7A-0EE8-4258-BE8B-260F9A1192A7}"><font color="#0000ff"><u>LifecycleEvent</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is brought into existence.

### <a id="{46DE5D1F-B3CE-4858-A6D1-64A0B891A00F}"></a>Created
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is created

The date/time of the creation can be specified using the <i>inPeriod </i>relationship. 

### <a id="{1EBC6375-B26C-4506-B4DE-85B74E476362}"></a>CreatedContent
A <a href="#{AF60517B-E4EF-48ca-BE0F-56E0A89660FD}"><font color="#0000ff"><u>Create</u></font></a> <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where online content is created

### <a id="{850DB6D5-C8E8-4aa8-87A0-4E7680FF854A}"></a>Creator
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> participates in a <a href="#{AF60517B-E4EF-48ca-BE0F-56E0A89660FD}"><font color="#0000ff"><u>Create</u></font></a> event as a creator

### <a id="{C2174205-C96F-4427-A401-19C1DEF0E4AF}"></a>CreditCard
A <a href="#{848A9E0F-F3B4-47c3-AA7E-2FF6BE92170C}"><font color="#0000ff"><u>BankCard</u></font></a> that allows the customer to carry a line of credit

### <a id="{43E58528-16E4-48b3-8F13-10500879EA83}"></a>CriminalActivity
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> which is illegal within the laws of the jurisdiction in which it takes place.

Note: If the <a href="#{43E58528-16E4-48b3-8F13-10500879EA83}"><font color="#0000ff"><u>CriminalActivity</u></font></a> falls into one of the Home Office Offence Classification Index codes, then this should be provided using the offenceCode attribute.

### <a id="{3CEFB37C-D5EE-4c9d-848D-C8E2DB206482}"></a>CriminalOrganisation
An <a href="#{F3DB6A59-B2DE-4743-A9A8-7DA9CCC68638}"><font color="#0000ff"><u>OrganisationState</u></font></a> that is assessed to be breaking the law in an organised manner

### <a id="{B85F065A-6A18-433e-9195-7B6BCBB91C7C}"></a>Crossing
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> and an <a href="#{F8FABF60-63D3-42ae-BA6A-54CFD0C036BF}"><font color="#0000ff"><u>ArbitraryOverlap</u></font></a> whose extent is defined by the shared overlap of two or more Locations

### <a id="{5A0E8F10-EE46-49bd-8E25-A67040D4A40B}"></a>crossingOf
A partOf <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> (range) has a <a href="#{B85F065A-6A18-433e-9195-7B6BCBB91C7C}"><font color="#0000ff"><u>Crossing</u></font></a> (domain)

### <a id="{A06EE74F-9A66-4b63-8DC3-3B1C2B362862}"></a>Currency
A <a href="#{E5C27DA8-7DF1-49ea-A9EC-ABE17AFD2047}"><font color="#0000ff"><u>ClassOfAmountOfMoney</u></font></a> that is the denomination as currency.

The identifier should be specified as an ISO4217 three-letter code (e.g. USD, GBP, EUR, etc.)

### <a id="{C53F62D0-0817-404b-9624-95A89D94F9A2}"></a>currencyAmount
A number that represents the amount of currency. 

Note: sometimes the number and/or the currency may be unknown and therefore not instantiated

### <a id="{AE8A5533-9C08-46e7-8131-E3D119F6AAE3}"></a>currencyDenomination
The currency in which the <a href="#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8}"><font color="#0000ff"><u>AmountOfMoney</u></font></a> is denominated

### <a id="{76689446-5969-49d3-8E7E-A92C86C244D5}"></a>Customer
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> is the customer for the <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> - i.e. the Event has been conducted as a service to them, or in production of goods for them.

### <a id="{43560C95-66A3-4d69-A743-F0A166DE51FC}"></a>CustomerIdentifier
The customer identifier associated with the Financial Account.

A single <a href="#{76689446-5969-49d3-8E7E-A92C86C244D5}"><font color="#0000ff"><u>Customer</u></font></a> Identity could be associated with more than one Financial <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a> managed by the same provider.

### <a id="{8CF52FB7-69F2-4ef2-8074-FB90EE924139}"></a>CyberStalking
A form of <a href="#{9B232210-27A3-410a-A713-EFDE7922C61C}"><font color="#0000ff"><u>Stalking</u></font></a> which takes place online.

### <a id="{3099B032-4B0A-4aec-ABCD-3E862C4C1979}"></a>Database
A <a href="#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2}"><font color="#0000ff"><u>DataObject</u></font></a> that is the contents of an entire database (note this is still a class, as there may be many copies of the database)

### <a id="{73F8D96C-A9EC-4301-9968-0F7BF9826C45}"></a>DatabaseItem
A <a href="#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2}"><font color="#0000ff"><u>DataObject</u></font></a> that is part of the data in a Database

Examples:

* A table, row, column in RDBMS
* A document in a document db
* a key-value pair in KVDB
* named graph in a graph db

### <a id="{1F23EB62-323B-402d-84BD-B4D417ED1A73}"></a>DatabaseRow
A <a href="#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2}"><font color="#0000ff"><u>DataObject</u></font></a> that is an entire row of a table in a database (note this is still a class, as there may be many copies of the database)

### <a id="{D9E56CAA-4668-4248-B087-C041363816DD}"></a>DatabaseTable
A <a href="#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2}"><font color="#0000ff"><u>DataObject</u></font></a> that is the entire contents of a table in a database (note this is still a class, as there may be many copies of the database)

### <a id="{2D88DE83-F87F-48ad-A485-9FFA79ED90D8}"></a>DataKey
A unique key (usually only unique within a Database, though it could be a GUID) that identifies a <a href="#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2}"><font color="#0000ff"><u>DataObject</u></font></a>

### <a id="{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2}"></a>DataObject
A <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> which might contain internal structure that can be exploited using bespoke tools and/or applications. Data objects might be geoobjects, video files, audio files, etc.

### <a id="{F6173D27-D86D-40f8-A5B0-36DCCF85D396}"></a>DeathState
A <a href="#{892345CD-9FA7-4982-978D-B6D3ABAE839C}"><font color="#0000ff"><u>BoundingState</u></font></a> that marks the end of a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>'s life

The location of the death can be specified using inLocation

The date/time of the death can be specified using the <i>inPeriod </i>relationship. 

### <a id="{F0C846E7-76B9-4ab6-988E-3694C95818E7}"></a>DebitCard
A <a href="#{848A9E0F-F3B4-47c3-AA7E-2FF6BE92170C}"><font color="#0000ff"><u>BankCard</u></font></a> where transactions debit from a bank account

### <a id="{5E25DC95-E376-420f-9991-F5175476B386}"></a>DeclarationOfWar
A <a href="#{53D5957B-E4B6-4cbb-8CE9-887F7152820F}"><font color="#0000ff"><u>PoliticalAnnouncement</u></font></a> marking the start of a <a href="#{D4F568F5-7BC4-489d-94BC-AE1305E5C0C2}"><font color="#0000ff"><u>War</u></font></a>

### <a id="{19B808BB-348E-4ea3-B62E-ED6356F7D4A0}"></a>DeclaredTarget
The <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> against which <a href="#{D4F568F5-7BC4-489d-94BC-AE1305E5C0C2}"><font color="#0000ff"><u>War</u></font></a> has been declared

### <a id="{82139547-0CA1-448d-997F-3386EFDF049C}"></a>DeclaringParty
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> makes an Announcement

Note: this also covers GoverningParty from IES 3.2

### <a id="{F428ADA5-2349-4cd0-815F-8F768B08C6E6}"></a>Delivery
A <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> where one or more Entities are delivered to the receiving party

### <a id="{096F83D3-F25E-4d48-96E8-566731C06DB1}"></a>DeliveryAddress
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{C90267B5-77A3-4b79-BD0D-7C50C3F4C333}"><font color="#0000ff"><u>Address</u></font></a> participates in a <a href="#{F428ADA5-2349-4cd0-815F-8F768B08C6E6}"><font color="#0000ff"><u>Delivery</u></font></a> as a the location to which the delivery is made

### <a id="{63289363-A4D6-4abf-BE19-6DCDDCF9B28F}"></a>DeliveryRecipient
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> participates in a <a href="#{F428ADA5-2349-4cd0-815F-8F768B08C6E6}"><font color="#0000ff"><u>Delivery</u></font></a> as a recipient

### <a id="{33C68A39-AF9C-4f37-97EA-1DE4BAC4F7FB}"></a>DemocraticChangeOfGovernment
A <a href="#{7FA15F56-86C4-47f4-9032-999C17703368}"><font color="#0000ff"><u>ChangeOfGovernment</u></font></a> that comes about by democratic means

### <a id="{6C7891C7-E095-41f4-A894-AA0C6A22F5D2}"></a>Department
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that is part of another Organisation - usually part of a <a href="#{1456439C-65C9-4a39-A743-09A7D0FBF248}"><font color="#0000ff"><u>CommercialOrganisation</u></font></a>, though other Organisations have departments

### <a id="{0FCBDA68-1B1C-40e1-9C5B-0E225CA827DB}"></a>Departure
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> and a <a href="#{892345CD-9FA7-4982-978D-B6D3ABAE839C}"><font color="#0000ff"><u>BoundingState</u></font></a> that marks the start of a Travel event

The date/time of the departure can be specified using the <i>inPeriod </i>relationship. 

### <a id="{27000BBA-F3F9-4355-B466-92CE04477C9B}"></a>Destroy
A <a href="#{FA07AB7A-0EE8-4258-BE8B-260F9A1192A7}"><font color="#0000ff"><u>LifecycleEvent</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is destroyed

### <a id="{E70CA8CD-51DC-4f77-982C-C233F9493FF9}"></a>Destroyed
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is destroyed

### <a id="{C029299D-5946-48dd-94CB-80EC23A56300}"></a>Destroyer
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> participates in a <a href="#{27000BBA-F3F9-4355-B466-92CE04477C9B}"><font color="#0000ff"><u>Destroy</u></font></a> event as a destroyer

### <a id="{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"></a>Device
An <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a> that is man-made and performs one or more functions - i.e. it is also an <a href="#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B}"><font color="#0000ff"><u>Actor</u></font></a>

### <a id="{0073BD83-64CB-433c-BF4D-A6BB01862F14}"></a>DeviceInCommunication
A <a href="#{6107EEA5-1A13-46e4-83FB-14740437B814}"><font color="#0000ff"><u><a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a>State</u></font></a> (and an EventParticipant) when a Device is communicating. 

### <a id="{700BC564-35E1-4921-8759-5DAFA51B4E83}"></a>DeviceOnline
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a> participates in an <a href="#{24499751-7D9B-4f2e-B880-8D5BC4FCEF30}"><font color="#0000ff"><u>OnlineEvent</u></font></a>

### <a id="{6107EEA5-1A13-46e4-83FB-14740437B814}"></a>DeviceState
A temporalState of a <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a>

### <a id="{73F2438B-77F5-49ee-B70D-84D5D50B378F}"></a>dialInNumber
The number dialed to take part in the <a href="#{6EAC8930-3D16-4e44-9706-989BDF6564A5}"><font color="#0000ff"><u>TeleConference</u></font></a>

### <a id="{E73C74A9-B356-40a4-BDBB-40567592BBD0}"></a>Disagreement
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> that covers the end-to-end disagreement between parties

### <a id="{52DB371E-71AC-4812-B3CF-0FD7D73F1BB0}"></a>DiscontinuousState
A <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> that is temporally dissected - i.e. it is not a continuous state, but in fact a fusion of states (which may or may not be specified)

This is used for managing situations where something happens from time to time, and we don't always know when it happens. For example, if a vehicle is usually parked in a street, we would use a <a href="#{52DB371E-71AC-4812-B3CF-0FD7D73F1BB0}"><font color="#0000ff"><u>DiscontinuousState</u></font></a> of the vehicle that would be inLocation.

### <a id="{30A0F2DA-DB31-40fd-8723-88A24B2F8448}"></a>Dislikes
A <a href="#{B1D011F9-9585-49eb-97C4-86E82D6F0BCF}"><font color="#0000ff"><u>Interested</u></font></a> state where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> dislikes something

### <a id="{2855AF50-EEE4-4ced-B499-AE42423A4DE3}"></a>DispositionalClass
A ClassOfElement whose instances all share the same disposition - e.g. capability or tendency

Example: Vehicles capable of Mach 2

### <a id="{369D2CA7-BFFD-4bc3-941F-47262C3DBF1F}"></a>disrespectfulOf
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one is disrespectful of the other.

Note: this should not be considered a bi-directional relationship. Just because one person disrespects another person does not necessarily mean the feeling is reciprocated. 

### <a id="{3499FB8A-AA42-4367-BBBC-79A69338BD70}"></a>distrusts
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one <a href="#{3499FB8A-AA42-4367-BBBC-79A69338BD70}"><font color="#0000ff"><u>distrusts</u></font></a> the other.

Note: this should not be considered a bi-directional relationship. Just because one person distrusts another person does not necessarily mean the feeling is reciprocated. 

### <a id="{AC7C948A-F19C-4296-AC38-0FEE6A4C5E90}"></a>documentedBy
An <a href="#{D106A0A9-55C4-454f-9E20-35BA54114036}"><font color="#0000ff"><u>isRepresentedAs</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{F0B48978-D4E4-45a4-8238-091A5B714D82}"><font color="#0000ff"><u>WorkOfDocumentation</u></font></a> is about an <a href="$element://{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a>

### <a id="{ACB44E46-7A30-4911-A9F0-3D5412FB3725}"></a>DocumentFormat
A <a href="#{CCC8FA06-CDA8-491d-BFFC-0A88D6A565B1}"><font color="#0000ff"><u>ClassOfIndividualDocument</u></font></a> whose members are all of the same document <a href="#{EF2C13D4-7106-4799-BB72-7CD47714F257}"><font color="#0000ff"><u>format</u></font></a> - e.g.

PDF
MS Word

### <a id="{2F8738A6-5EBA-4d80-980B-AA9E6F28B81A}"></a>documentIdentifies
Links an <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a> to the <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> it identifies.

Note: was "Is associated with" in IES3

### <a id="{19FE20BA-D898-46d4-8916-3E73BC059D54}"></a>DocumentSection
A <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> that is a section/chapter/paragraph in a <a href="#{F0B48978-D4E4-45a4-8238-091A5B714D82}"><font color="#0000ff"><u>WorkOfDocumentation</u></font></a>

Note: inRepresentation should be used to associate the DocumentSection with the WorkOfDocumentation or other DocumentSection it is part of.

### <a id="{42FFB9AC-2D28-453a-80A0-2A271DA32EB5}"></a>DomainName
A <a href="#{DF388418-F296-46a5-A2A3-4297F084DD07}"><font color="#0000ff"><u>CommunicationsIdentifierRange</u></font></a> that defines a realm of administrative autonomy, authority or control within the internet.  [from wikipedia]

### <a id="{44C1DD59-354B-405a-9755-417240802DE4}"></a>DrivingLicence
An <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a> that permits a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> to drive a <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> in the <a href="$element://{92EBA9B9-48C2-4082-9FE5-603977BD6846}"><font color="#0000ff"><u>Country</u></font></a> of issue. 

### <a id="{7852A5E5-8684-49f2-82AE-3368032163B1}"></a>Duration
The Measure of an Element's temporal extent

### <a id="{A4502460-54B7-446b-A9AA-003B49F9682B}"></a>Easting
The GeoIdentity that is a representation of the eastward componrnent of cartesian point on a map - i.e. on a 2D projection of the globe such as a mercator projection.

### <a id="{F30D350C-848D-4b02-AEA5-86575CEEEFB3}"></a>EducationalOrganisation
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that provides education

### <a id="{7D9E328D-345E-43f5-8163-9657E4D016BD}"></a>Election
A <a href="#{3A0E6FDD-5B3B-4092-9549-C05E8A5FED41}"><font color="#0000ff"><u>PoliticalEvent</u></font></a> where the population vote for their preferred <a href="#{E035D766-CB68-49c3-AC69-A56F3487C625}"><font color="#0000ff"><u>ElectoralCandidate</u></font></a> to become their representative. 

### <a id="{E035D766-CB68-49c3-AC69-A56F3487C625}"></a>ElectoralCandidate
A <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> standing for elected office

### <a id="{515468C2-B4D9-449d-8AC4-575973EFBF6B}"></a>ElectoralRegion
The <a href="#{FC55D479-07C4-4d98-B48C-5032190E493D}"><font color="#0000ff"><u>RegionalConstituency</u></font></a> being decided in an <a href="#{7D9E328D-345E-43f5-8163-9657E4D016BD}"><font color="#0000ff"><u>Election</u></font></a>

### <a id="{9442C4E6-A52B-4c93-B942-8B93D90B3B14}"></a>ElectricCurrent
The Measure of the flow of electric charge

Note: whilst this is a tricky Measure in a 4D ontology, it should be used in a niaive manner - i.e. a measure of a State of an Entity when the current is flowing through it.

### <a id="{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"></a>Element
An <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> that has a spatial extent and can have start and end dates

### <a id="{FCBB35B9-704B-46c1-8054-10B7DA7EB8F8}"></a>EmailAccount
A <a href="#{8300451C-1DF9-4545-9174-D8AA69C58CCD}"><font color="#0000ff"><u>CommunicationsAccount</u></font></a> that is used to administer the use of one or more e-mail addresses.

### <a id="{36F61EDF-6E6E-4d8d-9E75-275A820F6D96}"></a>EmailAddress
A <a href="#{A82378B9-9774-46b9-9845-CC75BE882F06}"><font color="#0000ff"><u>CommunicationsIdentifier</u></font></a> that uniquely identifiers an email account.

Format: local-part@domain

### <a id="{74721DF1-18D6-4c1b-93CC-71C888C6D405}"></a>employedBy
A <a href="#{181AAC84-26CE-4531-AC32-A73B8FD8B858}"><font color="#0000ff"><u>worksFor</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> where the worker is employed.

### <a id="{8AF1DB0B-9BEB-4a33-A459-7EF2BE309E81}"></a>EncodedData
A <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> which is external data according to a data format that is not in IES format. 

### <a id="{F8109922-1CB1-490d-BBB5-FD5B76E19FD1}"></a>endBoundOfClass
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking a <a href="#{E7A659A5-9059-4ea5-8FAB-8A29AFC47D9A}"><font color="#0000ff"><u>TimeBoundedClass</u></font></a> to the <a href="#{2173F463-524C-457c-B106-51322F64F122}"><font color="#0000ff"><u>ParticularPeriod</u></font></a> that marks the end bound date of its instances

### <a id="{6767DFCD-3FCB-42cc-BEE3-9FA9A324DF0B}"></a>endsIn
An xsd:DateTime for the end of the period

### <a id="{A88ABE99-1D6C-4843-A2E4-7531626D3859}"></a>EndToEndActivity
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> (usually of long duration) that is composed of a number of other Events.

### <a id="{1B39630B-B00F-4def-9C65-48082C4AD2E0}"></a>EndToEndAgreement
An <a href="#{A88ABE99-1D6C-4843-A2E4-7531626D3859}"><font color="#0000ff"><u>EndToEndActivity</u></font></a> which is the overall process of agreeing something, including all the events that take place under that agreement, such as the negotiation, signing, delivery of service, etc.

### <a id="{D75F18D1-95D6-481b-84D5-F8D7F3A5A389}"></a>EndToEndAuthorisation
An <a href="#{A88ABE99-1D6C-4843-A2E4-7531626D3859}"><font color="#0000ff"><u>EndToEndActivity</u></font></a> which is the overall process of requesting, receiving authority to act, and the conduct of activities under that authorisation until the period of authorisation ends. 

### <a id="{911EB3DE-A001-493d-850D-3CF5A848791D}"></a>EndToEndTransaction
An <a href="#{A88ABE99-1D6C-4843-A2E4-7531626D3859}"><font color="#0000ff"><u>EndToEndActivity</u></font></a> covering the lifecycle of the trade

### <a id="{7F1A6A06-5223-4bf9-B903-1061A127D62C}"></a>enemyOf
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one is the enemy of the other.

Note: this should not be considered a bi-directional relationship. Just because one person considers another person their enemy does not necessarily mean the feeling is reciprocated. 

### <a id="{78C33499-CD14-43cb-82AE-93A0F8CF022B}"></a>EntertainmentEvent
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where entertainment (sporting, music, theatre, etc.) is provided

### <a id="{96989C30-99CC-4606-A8D4-DFD9421F0E34}"></a>EntertainmentTicket
A <a href="#{0BC61540-2AFB-42e6-A845-79771EE0268D}"><font color="#0000ff"><u>Ticket</u></font></a> to an <a href="#{78C33499-CD14-43cb-82AE-93A0F8CF022B}"><font color="#0000ff"><u>EntertainmentEvent</u></font></a>

### <a id="{F4EDE167-6F5A-417d-9984-0221CCDF752C}"></a>Entity
An <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> typically represents a tangible thing like a Person, a Communications Device, or a Location.

### <a id="{74169219-A47C-48ce-A25F-3948E7E873B6}"></a>EntityInTransit
A <a href="#{55384377-146A-47c9-8706-18A1343A219C}"><font color="#0000ff"><u>TravelLeg</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is moving in <a href="#{7693D2C9-0F06-4005-BB8D-B5B572B2281A}"><font color="#0000ff"><u>Transit</u></font></a>

### <a id="{8AC946A4-4C03-463c-9F32-37EA8593988A}"></a>Ethnicity
A <a href="#{2A62C672-1757-4a2d-874B-C099C9DEC416}"><font color="#0000ff"><u>ClassOfPerson</u></font></a> whose members all share the same ethnicity

### <a id="{B376370E-F5E8-4287-A3EC-AC35532919B1}"></a>Event
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> represents an activity or incident, involving one or more participating entities, that occurred/started at a specific point in time � e.g. a meeting, or a telephone call.

### <a id="{07DCD4FC-938C-438d-ABE6-F7F64E66A255}"></a>eventDateTime
The date/time of the performance to which the ticket is valid.

### <a id="{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"></a>EventParticipant
A <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> which is the participating role of an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> in an Event.

Note: this includes inactive participation (e.g. something that is being repaired). If the participation is known to be active then ActiveEventPartipant (or one of its subtypes) should be used. In BORO, EventParticipant would be "Involvement" and ActiveEventParticipant would be "Participation".

### <a id="{FE668C24-D25C-4273-872A-EB77CB09341D}"></a>EventState
A temporal state of an <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a>

Note: care must be taken with using this in a 4D, extensional model such as IES. States such as "Ended" would not be appropriate, for example - in such a case, the temporal extent of the Event or the presence of a BoundingState to end it would be correct. 

### <a id="{AFFFF30F-B274-4466-B0F2-D2A6A78E1832}"></a>EvidentialPhotograph
Relates a <a href="#{AD0F575E-5C28-4594-B346-50E9F22C2A8E}"><font color="#0000ff"><u>Surveillance</u></font></a> <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> to a Document that is the evidence resulting from the Surveillance

### <a id="{485CBF1A-04FF-4741-8471-46A03D28C406}"></a>ExchangedItem
An <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> is a real world �thing� about which a sender might retain specific knowledge, some or all of which is needed to be shared (exchanged) with one or more recipients.

### <a id="{749B002E-37B1-4754-B3B2-96642B3CF4A7}"></a>ExchangePayload
A marker object that shall be present in all IES exchange files. This object is the domain for all meta-data about the file.

Wherever possible, Dublin-Core meta-data tags should be used on an ExchangePayload. If locally defined properties are needed, then these may also be defined and included in the exchange file. 

### <a id="{883B5479-62DD-47a4-BC14-9A11835D820B}"></a>excludedFrom
A Relationship between a <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> and a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> they are not allowed to enter.

Note: any additional information about how or why the exclusion is in place should be added to the state

### <a id="{9CD2C1B1-85B1-4579-9376-07827AD68461}"></a>Facility
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> that is man-made, but is typically larger than an <a href="#{C90267B5-77A3-4b79-BD0D-7C50C3F4C333}"><font color="#0000ff"><u>Address</u></font></a> (i.e. it may have more than one postal address)

Examples:

Military camps, factories, sports facilities, airports, etc.

### <a id="{3AA26AC6-206D-4b6d-BDEC-C9E2B4814BE7}"></a>familiallyRelatedTo
A Relationship between <a href="#{38F8B795-0BCE-4945-8C69-8678ED935C1A}"><font color="#0000ff"><u>PersonState</u></font></a> (which may be a Person, or just a temporal state of Person) and another <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> to indicate they have a familial relationship.

Note:  some relationships will be temporal (e.g. spouseOf) and therefore related a state to a Person. Others will be for life (i.e. from the birth of the youngest until one of them dies) and therefore between two whole-life Person entities.

### <a id="{A589F81D-DC15-4b71-80B5-BA4CD46B2E41}"></a>fearfulOf
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one is fearful of the other.

Note: this should not be considered a bi-directional relationship. Just because one person considers another person a threat does not necessarily mean the feeling is reciprocated. 

### <a id="{B2ED961F-245E-4e74-A32F-6B9CF1BBDF2B}"></a>FerryTicket
A <a href="#{0BC61540-2AFB-42e6-A845-79771EE0268D}"><font color="#0000ff"><u>Ticket</u></font></a> that is used to travel by sea

### <a id="{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"></a>FinancialAccount
An <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a> held for financial management purposes.

### <a id="{94BC4F7F-3DC3-4e26-8E2B-26E7D9B1A760}"></a>financialAccountType
Relates a <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a> to its type. Note, that a given FinancialAccount may have more than one <a href="#{901334E9-238C-4d05-8F85-FE9A8E537BA1}"><font color="#0000ff"><u>ClassOfFinancialAccount</u></font></a> - e.g. a Business <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a> that is also a Current Account

### <a id="{8B6DD87E-3D76-4836-9201-1244B80CDC69}"></a>FirstLineOfAddress
The first line of the Address including the number of the dwelling and the street name.

### <a id="{375B0887-712F-43f0-BBF4-5C544D75AC39}"></a>Flight
A <a href="#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74}"><font color="#0000ff"><u>TravelService</u></font></a> by air

### <a id="{3A9A1BA9-465F-4f6d-BD55-9F3F8AE40AE0}"></a>FlightTicket
A <a href="#{0BC61540-2AFB-42e6-A845-79771EE0268D}"><font color="#0000ff"><u>Ticket</u></font></a> that is used to travel by air

### <a id="{DA626F73-5748-47db-813F-E1813577F41B}"></a>FootballMatchTicket
An EntertainmentTicket for a football match

### <a id="{78686D99-2AAC-4f5b-8EE0-456BDCC6F99E}"></a>Forgery
A <a href="#{43E58528-16E4-48b3-8F13-10500879EA83}"><font color="#0000ff"><u>CriminalActivity</u></font></a> that is the creation of fake items

(also a subclass of Create). 

### <a id="{EF2C13D4-7106-4799-BB72-7CD47714F257}"></a>format
The <a href="#{EF2C13D4-7106-4799-BB72-7CD47714F257}"><font color="#0000ff"><u>format</u></font></a> of the respective WorkOfDocumentation.

Examples:

PDF
MS Word

### <a id="{F1F94713-6D95-4928-B537-4FBA55D09E34}"></a>formatOfIndividualDocument
The <a href="#{EF2C13D4-7106-4799-BB72-7CD47714F257}"><font color="#0000ff"><u>format</u></font></a> of the respective IndividualDocument.

Examples:

PDF
Printed

### <a id="{5054AFA3-8FC7-449d-93EE-C69B9D2AE118}"></a>FoundOrganisation
A Create Event where an Organisation is founded

### <a id="{13EB3439-497F-49ad-A7F4-DEF8A600F640}"></a>friendOf
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one is the friend of the other.

Note: this should not be considered a bi-directional relationship. Just because one person considers another person their friend does not necessarily mean the feeling is reciprocated. Not that I'm bitter or anything. See also <a href="#{9B232210-27A3-410a-A713-EFDE7922C61C}"><font color="#0000ff"><u>Stalking</u></font></a> if you must. 

### <a id="{8B4DB18E-DF46-4419-B0ED-0159A25F2319}"></a>Gender
A ClassOfPerson whose members all share the same gender

### <a id="{7EEE1EF7-C814-4eee-85B3-F48698FD52B6}"></a>GeographicFeature
A Location that is a naturally occurring feature on the earth.

### <a id="{87251DA1-7293-445e-987F-F13E331B6BDF}"></a>GeoIdentity
A unique Identifier attributed to the respective Location

### <a id="{417C1F4E-6A5D-4631-B275-8E982252791A}"></a>GeoJSON
<a href="#{417C1F4E-6A5D-4631-B275-8E982252791A}"><font color="#0000ff"><u>GeoJSON</u></font></a> is an open standard <a href="#{EF2C13D4-7106-4799-BB72-7CD47714F257}"><font color="#0000ff"><u>format</u></font></a> designed for representing simple geographical features, along with their non-spatial attributes. It is based on JSON, the JavaScript Object Notation.

GeoJSON mandates use of WGS 84 coordinate system - see IETF RFC 7946

### <a id="{EA165884-8DF6-4aa6-848C-C682F6969D9F}"></a>GeoObject
A DataObject and a GeoRepresentation that contains geographical information

### <a id="{9A9467C3-D5FC-4964-8943-FE63ADF38914}"></a>GeoPoint
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> that is a point (mathematically speaking, of vanishing volume) on, below or above the surface of the WGS84 spheroid. The distance from the spheroid surface is given by the altitudeInMetres attribute.

### <a id="{A8C07233-5D62-4ad4-B405-2D15CFC37497}"></a>GeoRepresentation
A <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> for a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> - e.g. a point, a polyline, etc.

### <a id="{A01A5045-B09C-4bea-8C96-881C29F2EE60}"></a>GivenName
A PersonName that is one of the given names of a Person

Note:
A GivenName will often be applied to a <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> of the Person, as names tend to change over time

### <a id="{AE59CB88-3178-4bad-9F43-1276337C7944}"></a>GML
The Geography-Markup-Language (GML) is the XML grammar defined by the Open Geospatial Consortium (OGC) to express geographical features. <a href="#{AE59CB88-3178-4bad-9F43-1276337C7944}"><font color="#0000ff"><u>GML</u></font></a> serves as a modeling language for geographic systems as well as an open interchange <a href="#{EF2C13D4-7106-4799-BB72-7CD47714F257}"><font color="#0000ff"><u>format</u></font></a> for geographic transactions on the Internet. 

Key to GML's utility is its ability to integrate all forms of geographic information, including not only conventional "vector" or discrete objects, but coverages (see also GMLJP2) and sensor data.

### <a id="{917C549C-259F-4850-9CFD-35E05485BF63}"></a>governedPopulation
Relates a <a href="#{D62DDBB8-53FC-405a-BC43-89CA337563A0}"><font color="#0000ff"><u>Government</u></font></a> to the RegionalPopulation that it governs. 

### <a id="{72DC3E90-53CE-434d-A5F3-89BDCE08A201}"></a>governedRegion
The <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> which the respective <a href="#{D62DDBB8-53FC-405a-BC43-89CA337563A0}"><font color="#0000ff"><u>Government</u></font></a> is in charge of.

See also goverenedPopulation - sometimes Locations have no people, and sometimes people reside outside the region in which they are legally citizens.

Note: A Government instance has a start and end date corresponding to its time in power. 

### <a id="{D62DDBB8-53FC-405a-BC43-89CA337563A0}"></a>Government
An Organisation that is (usually) elected to run a governedRegion

### <a id="{0D042066-06C8-48d6-8387-500CF8EE2592}"></a>GovernmentOrganisation
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that is part of, or controlled by a national or local Government

### <a id="{289608A2-3F9D-413a-98AB-25579C370924}"></a>grantedActivityType
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking an <a href="#{F5EAAEEE-C0B2-469f-9048-3E0731ED8342}"><font color="#0000ff"><u>GrantOfAuthority</u></font></a> to a <a href="#{057C04F9-EB8A-4e21-9CF8-2D98038570FB}"><font color="#0000ff"><u>AuthorisedEventClass</u></font></a> that the authorisation grants.

For example,  granting authorisation to travel



### <a id="{F5EAAEEE-C0B2-469f-9048-3E0731ED8342}"></a>GrantOfAuthority
An <a href="#{2D5069F2-FE77-477f-A607-FA6458E64173}"><font color="#0000ff"><u>AuthorisationStage</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> grants another <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> authority to act.

### <a id="{2F618A01-5D5F-483c-8652-8B81196AA086}"></a>groupDescription
A simple text description of a GroupOfItems

### <a id="{42463865-450C-4a9a-9EF0-5322222C2B97}"></a>groupName
A name given to a GroupOfItems

### <a id="{04C2111A-D958-4a95-9271-7208B849DDD8}"></a>GroupOfItems
A collection of <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> that have been gathered together for a purpose. 

Note: The same ExchangedItem can be in more than one <a href="#{04C2111A-D958-4a95-9271-7208B849DDD8}"><font color="#0000ff"><u>GroupOfItems</u></font></a>

### <a id="{2AC7FDAB-7BB8-41ee-B558-AEBFE01274F2}"></a>Hacking
A <a href="#{43E58528-16E4-48b3-8F13-10500879EA83}"><font color="#0000ff"><u>CriminalActivity</u></font></a> where computer equipment is interfered with without the owners permission

### <a id="{1C02B06E-3159-48f6-9575-64B62765498B}"></a>handlingCaveat
A textual description of any handling caveats that must be adhered to.

### <a id="{60A37745-8DD5-4e4c-9A4C-6957F71AD971}"></a>happensIn
A partOf <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate an <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> takes place within a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a>

### <a id="{CB7F872F-7999-4bfd-8274-2C0E0AFE22AB}"></a>hasAccessTo
A Relationship between a <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> and an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> they have access to - e.g. a FinancialAccount, CommunicationsDevice, etc.

### <a id="{9464D864-E76F-4e09-89E1-D3B2D3E63F3B}"></a>hasAuthor
The author of the respective document.

### <a id="{720D0AA3-81F7-4220-A7A5-34304E33B72F}"></a>hasCharacteristic
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts an Element has a Characteristic or Measure

### <a id="{E7500475-8C4F-47a3-8AAB-C5679621FAE8}"></a>hasCountryOfIssue
The country in which the respective <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a> or <a href="#{9882D901-1B22-4b89-81D1-031F840A20D0}"><font color="#0000ff"><u>PaymentArtefact</u></font></a> was issued.

### <a id="{0AAF6757-AAC9-43c4-8B43-CB3358EADCA4}"></a>hasEmergencyContactAddress
The address of an emergency contact as printed on the <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a>

### <a id="{BC3185CE-53F4-45de-A6D4-DAC8343B4D1C}"></a>hasEthnicity
The ethnic group that the respective <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> belongs to.

The Metropolitan Police standard shall be used as the reference data standard.

### <a id="{8914E7DF-443B-4a3a-A945-AAD11B82A86A}"></a>hasGeneticGender
The gender the <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> was born with (sex) and which would result from a DNA test.

### <a id="{7640DBFC-B520-458c-A7C1-16651DDF217F}"></a>hasIdentifiedGender
The gender the <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> chooses to identify as

### <a id="{2065B9A0-DCAD-45be-9F0D-BD4398261A7F}"></a>hasLanguageProficiency
A language spoken by the respective <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> at a stage (PersonState) in their life

### <a id="{C3A36E36-0C73-4af7-88E3-81C9243CE456}"></a>hasName
An <a href="#{D106A0A9-55C4-454f-9E20-35BA54114036}"><font color="#0000ff"><u>isRepresentedAs</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts an <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> is identified (albeit loosely) by a <a href="$element://{7D7CC966-56EB-4220-A650-A993E598F2E2}"><font color="#0000ff"><u>Name</u></font></a>

### <a id="{07FD1DF6-BA77-4657-B3D3-D6D579FD4608}"></a>hasPublisher
The publisher of the document.

### <a id="{E076AFB8-F6F8-4b06-82B3-7ED568D1EE73}"></a>hasRegisteredCommsID
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{A82378B9-9774-46b9-9845-CC75BE882F06}"><font color="#0000ff"><u>CommunicationsIdentifier</u></font></a> and the <a href="#{20BB42F0-3F2D-4bb7-88DD-F4D05377D59B}"><font color="#0000ff"><u>CommunicationsAccountState</u></font></a> of the account to which the identifier is registered

### <a id="{6D1839A4-342A-4e34-823C-BDB392483048}"></a>hasReligion
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> where a <a href="#{38F8B795-0BCE-4945-8C69-8678ED935C1A}"><font color="#0000ff"><u>PersonState</u></font></a> holds or follows a <a href="#{BD538820-CE91-4b9a-ADB8-C105FE0F2E7B}"><font color="#0000ff"><u>Religion</u></font></a>

### <a id="{5C76592F-C47D-40ee-8D82-497962686D34}"></a>hasRole
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> has a Role

Example - Fred's time in Acme as a manager

### <a id="{16480E86-9FE4-4b37-ACFB-9E410F190664}"></a>hasSourceReference
A <a href="#{D106A0A9-55C4-454f-9E20-35BA54114036}"><font color="#0000ff"><u>isRepresentedAs</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> is the source (information provenance) for an <a href="$element://{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a>

### <a id="{0451B5D4-99CB-47a7-BB93-DF4DF6625837}"></a>hasStatedAddress
The address of the owner/user as recorded on the respective <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a> or PaymentArtefact.

### <a id="{9A4EB722-0BDA-4ba7-B895-7A4E273865C9}"></a>hasStatedCountryOfResidence
The country of residence as printed on the respective <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a> 

### <a id="{C8AB9A91-97ED-4868-8167-44E71F40AFE7}"></a>hasStatedNationality
The <a href="#{45CDA5C1-624D-4f2f-81F6-EF19300820A9}"><font color="#0000ff"><u>nationality</u></font></a> of the identity holder as specified on the IdentityDocument.

### <a id="{F95710A9-B0A7-4f7b-ADAA-08A2DCBD9C35}"></a>hasStatedPlaceOfBirth
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to the place of birth as recorded on the respective <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a>

### <a id="{644B75E8-92A0-4f16-861E-3B4FDFDF572E}"></a>hasStatedPlaceOfIssue
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to the place of issue as specified on the <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a>

### <a id="{654CB83B-75CF-4940-A2CF-C7820141C5AE}"></a>hasTheme
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking an <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> (e.g. Communication, <a href="#{6445E51F-3DDF-4dcf-ABDF-3ED123D53188}"><font color="#0000ff"><u>Meeting</u></font></a> or Investigation) to an <a href="$element://{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> that is a theme (or topic)

Examples:

* A Event being investigated <a href="$element://{FA4DDF04-16DA-4b5c-AE9A-6AB8CD07DCDB}"><font color="#0000ff"><u>after</u></font></a> it occurred
* A general investigation into a Location
* A Meeting discussing a new project
* A <a href="$element://{F186E39F-A251-4b84-85E9-577C7290F6D9}"><font color="#0000ff"><u>VoiceCall</u></font></a> about a <a href="$element://{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a>

### <a id="{8FD84185-A7CE-4d5d-974B-55F693C4376D}"></a>hasValue
An <a href="#{D106A0A9-55C4-454f-9E20-35BA54114036}"><font color="#0000ff"><u>isRepresentedAs</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a Measure has a MeasureValue

Note: a given Measure may have more than one value (e.g. 1kg or 2.2lbs) in different units of measure

### <a id="{6939AE2F-D74D-4446-8A88-5C26669689BA}"></a>Hates
An <a href="#{B1D011F9-9585-49eb-97C4-86E82D6F0BCF}"><font color="#0000ff"><u>Interested</u></font></a> state where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> hates something

### <a id="{FBCCD717-E163-4129-B270-966F5D404260}"></a>HealthServiceIdentifier
A NationalIdentityNumber used for managing a citizen's through-life healthcare

In UK, this would be an NHS number, apart from Scotland where it is called a CHI number

### <a id="{04F797E7-9B5C-48c5-A50D-A14CFF7725DE}"></a>hmlConfidence
A confidence whose value must be one of "HIGH", "MEDIUM", or "LOW"

This is a mandatory attribute for AssessToBeTrue

### <a id="{6314A9B0-4578-42a8-A553-1FDDF35AC7F1}"></a>holdsAccount
Relates an <a href="#{C93379F2-6B01-4100-ABFA-BD26098AC1CB}"><font color="#0000ff"><u>AccountHolder</u></font></a> (PersonState) to the <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a> they hold

### <a id="{F5C27E55-623E-4fa7-95C3-DD0A722D1035}"></a>hostedOn
Relates a <a href="#{3BE61CCF-DCD0-411d-9D43-5DEABF8381F2}"><font color="#0000ff"><u>WebResourceState</u></font></a> to the <a href="#{27BEFD0A-B30B-47db-B863-13E48D1172F9}"><font color="#0000ff"><u>OnlineService</u></font></a> that hosts it

### <a id="{AA530BCE-02F2-4195-A431-573D13A5B41C}"></a>IATACode
A GeoIdentity that is administered by the International Air Transport Associate for airport identification

### <a id="{40E59970-04CE-4961-83FC-179739C4DEC3}"></a>IBAN
An Identifier that is an International <a href="#{4E10343E-8350-4354-B3DB-A7F74B4535EF}"><font color="#0000ff"><u>Bank</u></font></a> <a href="#{31BFE794-924E-44e3-942E-ADC9ED19FBA1}"><font color="#0000ff"><u>Account</u></font></a> Number

See ISO 13616:2007

### <a id="{239A3A0C-183C-432f-9147-7259C9573AA2}"></a>ICAOCode
A GeoIdentity that is administered by the International Civil Aviation Organisation for identifying airports

### <a id="{1185F43F-7EBB-4e38-A1B3-FF1421F3416D}"></a>idAuthenticity
Provides an indication of the believed authenticity of the IdentityDocument


Genuine
Fake
Unknown

### <a id="{9E77B9DE-E76A-454d-B4B5-52496358FC65}"></a>idDateOfBirth
The Date of Birth as specified on the respective IdentityDocument.

### <a id="{ACAC12AD-16C3-480d-8149-C026F8BE9F81}"></a>idDateOfIssue
The date that the respective Identity Document was actually issued � this is different from the ValidFromDate on EphemeralIdDocuments.

### <a id="{96B7C774-1FE0-4307-BB62-B5899F953FF2}"></a>idEmergencyContactName
The name of an emergency contact as printed on the <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a>

### <a id="{0198C1BE-43A0-4841-925E-FA5C47991AC3}"></a>idEmergencyContactTelNo
The telephone number of an emergency contact as printed on the <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a>

### <a id="{315E6AD3-F2DA-4f69-864F-DA2B95121E2E}"></a>Identifier
A <a href="#{7D7CC966-56EB-4220-A650-A993E598F2E2}"><font color="#0000ff"><u>Name</u></font></a> that is unique within the specified context

### <a id="{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"></a>IdentityDocument
An IndividualDocument used to confirm the identity of the bearer (and often enables a particular activity � e.g. a passport enables the bearer to travel across international borders).

### <a id="{CCD1F7FE-C42A-4503-BF24-00E8805BD5DD}"></a>idFamilyName
The family name as printed on the <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a>

### <a id="{D5B27630-C222-45be-87C2-5C4F8592487B}"></a>idGender
The gender as recorded on the respective <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a>

### <a id="{77CA0C8D-71F0-4cb9-8621-407396FAC5A1}"></a>idGivenNames
The given names as printed on the <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a>

### <a id="{6C79CE89-8E17-4ee7-ABA8-DDA5D4AFC78B}"></a>idLowerRange
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{DF388418-F296-46a5-A2A3-4297F084DD07}"><font color="#0000ff"><u>CommunicationsIdentifierRange</u></font></a> and the <a href="#{A82378B9-9774-46b9-9845-CC75BE882F06}"><font color="#0000ff"><u>CommunicationsIdentifier</u></font></a> that is the lower limit of the identifier range 

### <a id="{92D9B068-F8D4-4cbc-AD57-1DA39D5CC1C7}"></a>idOnCard
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{F2CF8705-DA4A-4131-AB60-CF1AC33BED95}"><font color="#0000ff"><u>NationalIdentityNumber</u></font></a> (which identifies a person) is featured on a <a href="#{843EDE77-78C4-4a09-9866-DBCC726AD5E6}"><font color="#0000ff"><u>NationalIdentityCard</u></font></a>

### <a id="{7615FB07-E0C5-4734-AFC8-FD52688DD2CC}"></a>idUpperRange
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{DF388418-F296-46a5-A2A3-4297F084DD07}"><font color="#0000ff"><u>CommunicationsIdentifierRange</u></font></a> and the <a href="#{A82378B9-9774-46b9-9845-CC75BE882F06}"><font color="#0000ff"><u>CommunicationsIdentifier</u></font></a> that is the upper limit of the identifier range 

### <a id="{F481C966-058B-4caf-A427-9E492CAD0D63}"></a>IdUsedInCheckIn
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a> is used in a <a href="#{87308A03-5C79-4d94-99E1-660042AC7929}"><font color="#0000ff"><u>CheckIn</u></font></a> event

### <a id="{471CF113-1728-47fd-A763-D1FA69226FC4}"></a>ilrProficiency
The Proficiency qualifier is specified using the Interagency <a href="#{82652FF5-258F-459c-BC7F-6DAC65E1ECA1}"><font color="#0000ff"><u>Language</u></font></a> Roundtable (ILR) scale [E].

(a) ILR Level 0 � No proficiency
(b) ILR Level 1 � Elementary Proficiency
(c) ILR Level 2 � Limited Working Proficiency
(d) ILR Level 3 � Professional Working Proficiency
(e) ILR Level 4 � Full Professional Proficiency
(f) ILR Level 5 � Native or Bilingual Proficiency

### <a id="{3987794E-6E2E-4457-8BF7-47813B51B139}"></a>IMEI
The International Mobile Equipment Identity used to identify GSM, WCDMA and iDEN mobile phone handsets, as well as some satellite phones.

Usually a 15-digit number (14 digits plus a check digit)

Example Value:

123456789012345

### <a id="{C817C1ED-863B-41f0-B5C1-14117E926A94}"></a>IMSI
The International Mobile Subscriber Number
Historically, this is stored as a 64-bit number on the SIM Card (it is NOT identity of the SIM Card itself), but now can be a software assigned identifier to any mobile subscriber interface. 

An <a href="#{C817C1ED-863B-41f0-B5C1-14117E926A94}"><font color="#0000ff"><u>IMSI</u></font></a> is usually presented as a 15-digit number, but it can be shorter.

The first three digits are the Mobile <a href="#{92EBA9B9-48C2-4082-9FE5-603977BD6846}"><font color="#0000ff"><u>Country</u></font></a> Code (MCC), followed by a 2 or 3 digit Mobile Network Code (MNC) and the remaining digits are the Mobile Subscription Identification Number (MSIN).

For the example shown this would be:
- 404=India,
- 68=MTNL Delhi
- 1234567890=Subscriber ID

### <a id="{321CB600-140F-452f-96B7-640DE8289ECF}"></a>IncarceratingOrganisation
An Organisations's role in incarcerating a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>

### <a id="{06972684-050B-4f36-9393-B8790D510F5C}"></a>Incarceration
A <a href="#{3876B81C-E316-4e11-A6C4-8024E52F769B}"><font color="#0000ff"><u>LawEnforcement</u></font></a> <a href="#{A88ABE99-1D6C-4843-A2E4-7531626D3859}"><font color="#0000ff"><u>EndToEndActivity</u></font></a> where a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> is incarcerated

### <a id="{B5C15382-451A-4446-BBE6-C67FBDB04402}"></a>IncarcerationFacility
A Facility used for incarceration - e.g. a prison, detention centre, or remand facility

### <a id="{D10B4B95-5BF1-4e3f-A2A8-8F52F045C31A}"></a>inCategory
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> belongs to a <a href="$element://{8CA5551A-EAEB-4145-A75F-2E7D7DAD5A57}"><font color="#0000ff"><u>ContentCategory</u></font></a>

### <a id="{BC752C7E-611B-47d6-BA89-05E58CD23803}"></a>IncomingGovernment
The <a href="#{D62DDBB8-53FC-405a-BC43-89CA337563A0}"><font color="#0000ff"><u>Government</u></font></a> that took power after a ChangeOfGovernment

### <a id="{5C4C2871-5F61-4704-83D0-9F8CF42890BF}"></a>IncumbentRepresentative
A <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> in-office prior to the <a href="#{7D9E328D-345E-43f5-8163-9657E4D016BD}"><font color="#0000ff"><u>Election</u></font></a> being decided

### <a id="{F12D45EA-66D5-4016-BDF7-E1CD8F48CCF5}"></a>InDisagreement
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> is in disagreement

### <a id="{0F327324-6B4E-40b1-B96B-97A334BA5E4A}"></a>IndividualDocument
An Asset that is a written, photographed or drawn representation of thoughts. This might include, but not limited to, formal reports, books, legal instruments. Such documents might exist in a wide variety of forms, both printed and in electronic form.

Note: this is an individual document  - i.e. physical or (rarely) a specific electronic copy (e.g. on a specific hard disk...told you it was rare). In most cases, we refer to the document in general - <a href="#{F0B48978-D4E4-45a4-8238-091A5B714D82}"><font color="#0000ff"><u>WorkOfDocumentation</u></font></a> 

### <a id="{D68F4E10-957A-4e98-8447-8F2768940DA7}"></a>IndividualDocumentID
An Identifier used to uniquely identify an <a href="#{0F327324-6B4E-40b1-B96B-97A334BA5E4A}"><font color="#0000ff"><u>IndividualDocument</u></font></a>

### <a id="{411F5C4C-9AD0-462a-BE10-3F43958B7D66}"></a>influencedBy
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and the thing that influences them

### <a id="{5BEE4248-DC98-4625-8553-3BB2171A1EDE}"></a>informationContent
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a WebResourceState and a <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> that asserts the Representation is the content of the WebResource

Note: a state is used here as the content may change over time even though the WebResource persists

### <a id="{C21D2CA2-6F42-4b7c-9092-8B8C5B7BAF9F}"></a>inGroup
A property linking an <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> to a <a href="#{04C2111A-D958-4a95-9271-7208B849DDD8}"><font color="#0000ff"><u>GroupOfItems</u></font></a> indicating that it belongs to that group.

Note: An ExchangedItem may be in more than one group and a group may contain more than one ExchangedItem

### <a id="{FF902F8E-6B22-4f17-9C16-48543251D22E}"></a>inLanguage
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> is in a particular <a href="$element://{82652FF5-258F-459c-BC7F-6DAC65E1ECA1}"><font color="#0000ff"><u>Language</u></font></a>

### <a id="{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"></a>inLocation
A partOf <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate an <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> is entirely within a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a>

### <a id="{2F08EF25-A5C8-48ad-85E3-903DB008AA19}"></a>inPeriod
A partOf <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate an Element's lifetime is entirely within a PeriodOfTime

Example:

Fred's birth is in May 1978



### <a id="{0A28624B-C5E3-461e-B84A-E55B550B5DD6}"></a>inPossessionOf
A Relationship between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and an <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a> they have in their possession.

Note: this is separate to ownership - e.g. the possessor may well be the owner (use the <a href="#{FDD94D9F-F343-4c1b-9688-752C896A3C7C}"><font color="#0000ff"><u>owns</u></font></a> relationship) but may also be a result of borrowing, theft, temporary custodianship, 

### <a id="{6C1949B5-B86B-4940-8912-9008CCD67150}"></a>InPost
A temporal state of a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> when they are in a <a href="#{7C28E83C-1895-4901-ABF8-9D78C9C12C62}"><font color="#0000ff"><u>Post</u></font></a>

### <a id="{7238489D-6802-4733-9F7F-9B31D02B3C81}"></a>inRepresentation
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> is part of another Representation

### <a id="{1FDB4A8F-E28C-4e36-A085-935C20256F52}"></a>InResidence
A temporal state of a ResponsibleActor

Note:  this is the superclass of <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (the whole life person or organisation) because the whole-life state is just a special case of a ResponsibleActorState. This pattern is true for all states. 

### <a id="{7EB9FE85-127C-4918-AC56-62E1BE1DE825}"></a>inScheme
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> is a member of a RepresentationScheme

### <a id="{B37ADF66-D5D0-4144-9539-DA91BA302914}"></a>installedSoftware
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> indicating <a href="#{B6014BB6-FD82-4748-8DFF-65401770515C}"><font color="#0000ff"><u>Software</u></font></a> is installed on a <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a>

### <a id="{F87E3B6F-5872-47eb-89F8-6642DD7C8237}"></a>IntelligenceAgency
A <a href="#{0D042066-06C8-48d6-8387-500CF8EE2592}"><font color="#0000ff"><u>GovernmentOrganisation</u></font></a> that collects, analyses or disseminates intelligence

### <a id="{A0A9CD13-A4B4-415b-9187-64C9B72E2F4E}"></a>IntelligenceOperation
An OperationalEvent that involves the gathering, analysis or dissemination of intelligence

### <a id="{6D5E11EE-C61A-4e38-913F-BBAF2A34A288}"></a>InteractiveCommunication
A Communication that occurs synchronously - e.g. a video or voice call

### <a id="{B1D011F9-9585-49eb-97C4-86E82D6F0BCF}"></a>Interested
A <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> where the <a href="#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B}"><font color="#0000ff"><u>Actor</u></font></a> is interested in something

### <a id="{7BD2B884-F02C-4da2-AF6A-21B790FBF669}"></a>interestedIn
A Relationship between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (or state thereof) and an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> they are interested in.

### <a id="{AE70547D-8E7E-474e-B7FD-F0A81F470157}"></a>InternationalCoalition
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> formed of Nations who have agreed to pursue a particular course (e.g. a war)

### <a id="{39D0AC05-01DB-423a-861A-26E6125DF906}"></a>intimidatedBy
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one (range) intimidates the other (domain).

### <a id="{2912E599-436D-4b79-B94F-02FA2319F201}"></a>Investigation
An IntelligenceOperation that researches a particular threat, or theme. 

### <a id="{3525F314-87ED-43c8-9A84-68EDCD203B30}"></a>Investigator
An <a href="#{6730B57A-3E53-4bd2-B784-78C4FB239DBF}"><font color="#0000ff"><u>Operator</u></font></a> role where a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> is an investigator

### <a id="{82B189F4-9800-4b44-B10D-521B038455F1}"></a>InWork
A temporal state of a ResponsibleActor

Note:  this is the superclass of <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (the whole life person or organisation) because the whole-life state is just a special case of a ResponsibleActorState. This pattern is true for all states. 

### <a id="{4D914AB7-E337-4ff2-9154-9CA0BF7156EB}"></a>InWorship
A temporal state of a ResponsibleActor

Note:  this is the superclass of <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (the whole life person or organisation) because the whole-life state is just a special case of a ResponsibleActorState. This pattern is true for all states. 

### <a id="{451C4C40-4183-4130-B67C-6F746B8B8BCA}"></a>IPAddress
An Identifier that is an Internet Protocol address.

### <a id="{BEC2FDBC-6F37-4446-AEE1-3D4627DDD5F2}"></a>IPAddressRange
A CommunicationIdentifierRange between two IPAddress instances

In these examples the IPv4 address range is specified using the following format:
&lt;lower address&gt; - &lt;upper address&gt; using one of a number of different IPv4 address notations.

The IPv4 address range is all the IPv4 addresses between the &lt;lower address&gt; and the &lt;upper address&gt; (inclusive).

Both examples here represent the same address range (but in different notations).

The Dot Decimal Range notation specifies the &lt;lower address&gt; and the &lt;upper address&gt; in Dot Decimal form � where
each of these 32-bit IPv4 addresses are expressed as four octets expressed individually in decimal and separated by periods.

The Dot Hexadecimal Range notation specifies the &lt;lower address&gt; and the &lt;upper address&gt; in Dot Hexadecimal form � where each of these 32-bit IPv4 addresses are expressed as four octets where each octet is prefixed with 0x, expressed individually in hexadecimal and separated by periods.

### <a id="{0B494F4A-9E82-4667-89AD-3D22FC9B5742}"></a>IPPhoneHandset


### <a id="{142D6D4D-6EF3-48aa-8B7B-86DA73690E3E}"></a>IPv4Address
An IPAddress conforming to v4 of the standard

### <a id="{78549D65-75F2-41c3-AC14-F0D441AD6354}"></a>IPv6Address
An IPAddress conforming to v6 of the standard

### <a id="{1CA57828-3B6B-450b-B477-C59A196EAE34}"></a>isAuthorisedForUseWithPassport
The passport associated with the Visa.

Note: if the IES data does not already contain the associated passport, a <a href="#{13ABC7CA-915E-4069-8EA7-FD205A5336C5}"><font color="#0000ff"><u>Passport</u></font></a> instance must be created, and the appropriate passport number specified.

### <a id="{44ADC197-D9FA-4889-B6AF-929C3546F4A0}"></a>isCentroidOf
An <a href="#{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate a <a href="#{9A9467C3-D5FC-4964-8943-FE63ADF38914}"><font color="#0000ff"><u>PointOnEarthSurface</u></font></a> is the centroid of a <a href="$element://{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a>

### <a id="{B093F8DA-AE08-4819-8E1C-F119EF212566}"></a>isDisposedTo
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts an Element is a member of a DispositionalClass - i.e. it is disposed to (capable of, tends to, etc.) the specified disposition.

### <a id="{EA859D48-5BA4-40b3-A52D-1465D1765262}"></a>isEndOf
An <a href="#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E}"><font color="#0000ff"><u>isStateOf</u></font></a> that relates a <a href="#{892345CD-9FA7-4982-978D-B6D3ABAE839C}"><font color="#0000ff"><u>BoundingState</u></font></a> to the <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> it marks the end of

### <a id="{FBA54EEF-91BF-4ba2-8B67-79C899963149}"></a>isIdentifiedBy
A <a href="#{C3A36E36-0C73-4af7-88E3-81C9243CE456}"><font color="#0000ff"><u>hasName</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts an <a href="#{315E6AD3-F2DA-4f69-864F-DA2B95121E2E}"><font color="#0000ff"><u>Identifier</u></font></a> identifies an <a href="$element://{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a>

### <a id="{2415B865-3C37-4595-9F38-11075EAB5D34}"></a>isLegalTenderIn
The <a href="#{92EBA9B9-48C2-4082-9FE5-603977BD6846}"><font color="#0000ff"><u>Country</u></font></a> in which a <a href="#{A06EE74F-9A66-4b63-8DC3-3B1C2B362862}"><font color="#0000ff"><u>Currency</u></font></a> is legal tender

### <a id="{22B79CFD-DEDA-42e1-8864-E8421D36CF19}"></a>ISO19125-WKT
A <a href="#{A8C07233-5D62-4ad4-B405-2D15CFC37497}"><font color="#0000ff"><u>GeoRepresentation</u></font></a> using Well-Known-Text encoding for ISO19125 simple features.

Note: the WKT must include the coordinate reference system used - e.g WGS 84

### <a id="{B92D79E2-9E7D-4df7-8D38-3D884AA09AD2}"></a>ISO3166_1Alpha_3
ISO 3166-1 alpha 3 (3-Letter <a href="#{92EBA9B9-48C2-4082-9FE5-603977BD6846}"><font color="#0000ff"><u>Country</u></font></a> Code)

### <a id="{ECFED94D-CC69-46b9-B09D-B282D5665787}"></a>ISO639-3Code
ISO639-3 three-letter language code

### <a id="{E9372543-434E-45d3-A1F0-8D711952D10A}"></a>iso8601PeriodRepresentation
A ISO8601 datetime (as <a href="#{57843280-4451-47eb-9616-B0843FE4E2C5}"><font color="#0000ff"><u>xsd:dateTime</u></font></a> if possible) that represents the ParticularPeriod.

Note: the representation is also encoded in the URI of the period, this is an additional required <a href="#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA}"><font color="#0000ff"><u>attribute</u></font></a> to enable querying by dateTime and SPARQL temporal operations.

### <a id="{BAEA86D9-C90E-4f8d-96F5-A01BB0C49711}"></a>isParticipantIn
An <a href="#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC}"><font color="#0000ff"><u>isPartOf</u></font></a> that relates an <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> to the <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> it participates in.

### <a id="{A77A19DA-2775-4dfa-A76C-41C158AC582C}"></a>isParticipantStateIn
An <a href="#{BAEA86D9-C90E-4f8d-96F5-A01BB0C49711}"><font color="#0000ff"><u>isParticipantIn</u></font></a> and an <a href="#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E}"><font color="#0000ff"><u>isStateOf</u></font></a> that relates an <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> to the <a href="$element://{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> it participates, in the case where the participant has the same spatial extent as the Event for that period of time.

Note: This is really just a bit of logical plumbing to enable start and end states of Events to be "all of the event for a period of time".

### <a id="{DF9F6056-CCD4-41aa-9A86-536F6150EC25}"></a>isParticipationOf
An <a href="#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E}"><font color="#0000ff"><u>isStateOf</u></font></a> that relates an <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> to the <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> that is the participant

### <a id="{CD85D7F7-783B-4d06-B023-56DBBDDC02DC}"></a>isPartOf
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking an <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> to another that it is part of.

Examples:

London partOf UK
My Arm partOf Me

### <a id="{D6974F5E-B24C-4a06-9AC1-DB6299E9BF55}"></a>isPrimaryForOrganisation
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking an <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a> to the <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> that prefers the use of that ExchangedItem.

This is used when there are more than one state, name, etc. for a given item, and there is a requirement to specify which one is considered primary / preferred by a particular Organisation.

Examples:

* A primary name for a person (applied to PersonName)
* A primary DoB for a person (applied to BirthState)
* A primary <a href="$element://{45CDA5C1-624D-4f2f-81F6-EF19300820A9}"><font color="#0000ff"><u>nationality</u></font></a> for a person (applied to the <a href="$element://{38F8B795-0BCE-4945-8C69-8678ED935C1A}"><font color="#0000ff"><u>PersonState</u></font></a> that links to the Nation)

### <a id="{D106A0A9-55C4-454f-9E20-35BA54114036}"></a>isRepresentedAs
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> in someway depicts an <a href="#{485CBF1A-04FF-4741-8471-46A03D28C406}"><font color="#0000ff"><u>ExchangedItem</u></font></a>

### <a id="{D9E068B1-2A44-4523-B8FC-F9888212B35C}"></a>isStartOf
An <a href="#{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E}"><font color="#0000ff"><u>isStateOf</u></font></a> that relates a <a href="#{892345CD-9FA7-4982-978D-B6D3ABAE839C}"><font color="#0000ff"><u>BoundingState</u></font></a> to the <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> it marks the start of

### <a id="{F7CBF87A-6ECC-4c9f-B698-FD3CF3F7980E}"></a>isStateOf
An <a href="#{CD85D7F7-783B-4d06-B023-56DBBDDC02DC}"><font color="#0000ff"><u>isPartOf</u></font></a> linking an <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> to a temporal <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> of that Element 

Examples:

You, you yesterday

### <a id="{5E353B12-2503-429f-A683-F7C77E0DFBAD}"></a>issuerIdentificationNumber
The IIN is a number that uniquely identifies the issuer of the <a href="#{4E10343E-8350-4354-B3DB-A7F74B4535EF}"><font color="#0000ff"><u>Bank</u></font></a> Card.

An ISO/IEC 7812 number contains a single-digit <i>major industry identifier </i>(MII), a six-digit <i>issuer identification number </i>(IIN), an <i>individual account identification </i>number, and a single digit checksum.

### <a id="{74D86486-8E18-474a-8930-B92E759BBE06}"></a>issuingAgency
The <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that issued the ticket � this might be different from the travel provider.

### <a id="{B8650A61-3B08-4f62-8EAB-0F9D007B20CE}"></a>isTeacherOf
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities that indicates one teaches the other.

In the case where the teaching is occasional / ad-hoc (i.e. there isn't an ongoing course) then the instance of the <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> should also be an instance of <a href="#{52DB371E-71AC-4812-B3CF-0FD7D73F1BB0}"><font color="#0000ff"><u>DiscontinuousState</u></font></a>

### <a id="{AD17E3D9-CAB2-4a60-99C9-109F4496F92F}"></a>JointAccount
A <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a> held by more than one person

### <a id="{8B571665-0AA1-40be-A7A0-A35BE86B7192}"></a>Journey
A <a href="#{95B5ACC4-956A-4b29-AB9E-BDCD12EF319F}"><font color="#0000ff"><u>Movement</u></font></a> which is made up of two or more TravelLegs

Note:  this may include a number of legs to the journey (i.e. instances of <a href="#{55384377-146A-47c9-8706-18A1343A219C}"><font color="#0000ff"><u>TravelLeg</u></font></a> that are part of the Journey)

### <a id="{6A9A065C-A31A-42be-B7E2-275F076DCA9D}"></a>JsonData
An <a href="#{8AF1DB0B-9BEB-4a33-A459-7EF2BE309E81}"><font color="#0000ff"><u>EncodedData</u></font></a> which is in JSON format

### <a id="{62EF76B2-4AB0-4e1e-98C4-61C3A85BF980}"></a>jurisdictionOfRights
A Relationship between <a href="#{487778E0-4BD7-4d9a-B7F7-63731478E1A2}"><font color="#0000ff"><u>Rights</u></font></a> and the <a href="#{6AE6F8A5-F427-4ea6-BABD-5720F07430F5}"><font color="#0000ff"><u>Nation</u></font></a> under whose laws the Rights are established

### <a id="{57F3607C-0204-4590-9442-24F372A35931}"></a>knownAssociateOf
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where both are known to know each other but the extent to which they interact (e.g. friendship, work, criminal activity, etc.) is not known.

### <a id="{57C9F8DF-AFE6-4374-9403-ACACAC26FCE4}"></a>LandlineHandset
A CommunicationsDevice that connects using fixed line telecommunications

### <a id="{D7F83A2D-6428-4211-964D-E1E8A8089083}"></a>LandlineTelephoneAccount
A <a href="#{593AE684-C2E9-4e40-A7FD-549BFA64900D}"><font color="#0000ff"><u>TelephoneAccount</u></font></a> where the telephones in use connect using a wired network and operate only in a specific location

### <a id="{82652FF5-258F-459c-BC7F-6DAC65E1ECA1}"></a>Language
A ClassOfRepresentation that is a spoken or written form of human communication

### <a id="{EB73AB32-8232-4b58-8271-640DDDDCC7DE}"></a>LanguageProficiency
A <a href="#{92CDC810-9DFA-476b-A2E7-33121F65905B}"><font color="#0000ff"><u>ClassOfPersonState</u></font></a> indicating the proficiency a person has in a particular language at that state in their life.



### <a id="{BD14EF81-DDBC-4bdf-BC40-E5FAE937ADA6}"></a>Latitude
A GeoIdentity that is a decimal representation of an angle of latitude of a <a href="#{9A9467C3-D5FC-4964-8943-FE63ADF38914}"><font color="#0000ff"><u>PointOnEarthSurface</u></font></a> (WGS84)

### <a id="{3876B81C-E316-4e11-A6C4-8024E52F769B}"></a>LawEnforcement
An Event that involves the application of criminal law

### <a id="{15806699-2F00-4891-B2A0-8A211CEDFC10}"></a>LawEnforcementOrganisation
A <a href="#{0D042066-06C8-48d6-8387-500CF8EE2592}"><font color="#0000ff"><u>GovernmentOrganisation</u></font></a> that investigates crimes and brings the perpetrators to justice. 
Wikipedia definition: Law enforcement is any system by which some members of society act in an organized manner to enforce the law by discovering, deterring, rehabilitating, or punishing people who violate the rules and norms governing that society.

### <a id="{E1AF7AFE-FA2F-40f7-88A3-CA6988BC2E0D}"></a>LeadInvestigator
An <a href="#{3525F314-87ED-43c8-9A84-68EDCD203B30}"><font color="#0000ff"><u>Investigator</u></font></a> who is charge of an <a href="#{2912E599-436D-4b79-B94F-02FA2319F201}"><font color="#0000ff"><u>Investigation</u></font></a>

### <a id="{5C21DE93-329F-4209-87FF-19610CB0D367}"></a>Length
The Measure of distance as specified by the International System of Quantities

### <a id="{FA07AB7A-0EE8-4258-BE8B-260F9A1192A7}"></a>LifecycleEvent
An Event that brings about change to its environment or another Element - e.g. creation, destruction or modification

### <a id="{B292748F-D41E-4c3b-9335-04D4B06A1F34}"></a>Likes
An <a href="#{B1D011F9-9585-49eb-97C4-86E82D6F0BCF}"><font color="#0000ff"><u>Interested</u></font></a> <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> likes something

### <a id="{E0D8895D-2230-4c80-8B06-351581C53436}"></a>LineOfAddress
A line in an Address. There may be any number of these.

### <a id="{ECC6E85E-CB08-464d-81A4-BA3ECDCB784C}"></a>LiveCast
An OnlineArtefact that is video or audio streamed online in real time.

Note: the begin and end dates for a <a href="#{ECC6E85E-CB08-464d-81A4-BA3ECDCB784C}"><font color="#0000ff"><u>LiveCast</u></font></a> instance mark its life online rather than the <a href="#{5382F9B3-0A28-4245-8EEB-BF3CEFFD4058}"><font color="#0000ff"><u>duration</u></font></a> of the actual recording. The recording itself should be tracked using an <a href="#{DB70D7EE-5076-4eb2-950B-63C71A3C8859}"><font color="#0000ff"><u>OnlineContentCreation</u></font></a> Event.

### <a id="{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"></a>Location
An Entity that is a geographic place which specifies a point or an area on the Earth's surface or elsewhere.

### <a id="{7CAFACD0-94F9-400e-B20E-E4ECE31943E5}"></a>LocationState
A temporal state of a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a>

### <a id="{8010625F-BA25-457a-93CF-7EC1E99261D7}"></a>Logoff
A OnlineEvent where an <a href="#{E95170B9-2599-46dc-BEDC-012B08F09D43}"><font color="#0000ff"><u>OnlineAccount</u></font></a> logs out of an <a href="#{27BEFD0A-B30B-47db-B863-13E48D1172F9}"><font color="#0000ff"><u>OnlineService</u></font></a>

### <a id="{43CDB7F8-E77E-4eba-A92E-C6A74AF954CA}"></a>Logon
A OnlineEvent where an <a href="#{E95170B9-2599-46dc-BEDC-012B08F09D43}"><font color="#0000ff"><u>OnlineAccount</u></font></a> logs onto an <a href="#{27BEFD0A-B30B-47db-B863-13E48D1172F9}"><font color="#0000ff"><u>OnlineService</u></font></a>

### <a id="{B2C5522F-EA60-455a-B00F-9CC87A76E5B0}"></a>Longitude
The GeoIdentity that is a decimal representation of an angle of longitude of a <a href="#{9A9467C3-D5FC-4964-8943-FE63ADF38914}"><font color="#0000ff"><u>PointOnEarthSurface</u></font></a> (WGS84)

### <a id="{E543978A-06D0-4c79-BCCD-A62DE9294A85}"></a>Loves
A <a href="#{7BD2B884-F02C-4da2-AF6A-21B790FBF669}"><font color="#0000ff"><u>interestedIn</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> where a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> loves another Person

### <a id="{96717346-1DF4-4eae-A7CF-E389B4454B47}"></a>lowerBound
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> a MeasureRange to the Measure that is its lower bound

### <a id="{8431C546-B6F9-406f-9ECD-383FE985D115}"></a>LuminousIntensity
The Measure of radiated light

### <a id="{DE1EDE92-142C-4c05-AD61-BE58822B2E17}"></a>MACAddress
A CommunicationsIdentifier that is used to identify network interface controllers

Various forms of the MAC address can be used:
(a) six groups of two hexadecimal digits, separated by hyphens (-) or colons (:), in transmission order
(b) three groups of four hexadecimal digits separated by dots (.) again in transmission order.
2. The <a href="#{E0036B31-8D73-4268-8959-6E9A5EE55BB2}"><font color="#0000ff"><u>make</u></font></a> &amp; <a href="#{98BDD06F-1BD7-42b8-B338-20A198BCF90A}"><font color="#0000ff"><u>model</u></font></a> of the network interface is encoded within the MAC address.

### <a id="{727175D4-0998-49a0-BAEE-6B8F1F1FD8D4}"></a>maintains
A Relationship between a <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> and an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> they maintain

### <a id="{E0036B31-8D73-4268-8959-6E9A5EE55BB2}"></a>make
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> from the device to its "make" - i.e. organisation that brands it (even if the manufacture is contracted-out)

Example - an iPhone 6S has <a href="#{E0036B31-8D73-4268-8959-6E9A5EE55BB2}"><font color="#0000ff"><u>make</u></font></a> Apple

### <a id="{F0C08ADE-7EE5-4392-9877-5FD8FB4076E9}"></a>MaliciousAccountUse
An OnlineAccountInUse where the account is used to conduct a <a href="#{43E58528-16E4-48b3-8F13-10500879EA83}"><font color="#0000ff"><u>CriminalActivity</u></font></a> online

### <a id="{8991D995-1915-47b7-B180-D9EBC4A1FD1F}"></a>managedBy
A <a href="#{181AAC84-26CE-4531-AC32-A73B8FD8B858}"><font color="#0000ff"><u>worksFor</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> where the managed <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> (domain) is managed by another <a href="$element://{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (range).

### <a id="{18A66904-823F-471d-A465-65ECD2D69867}"></a>MapGridArea
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> whose area is specified by a grid on a map.

Note this is the actual area, not the map grid. 

### <a id="{9DFEDF24-1203-4341-B282-BD37C1B9CDF5}"></a>Marriage
An <a href="#{A88ABE99-1D6C-4843-A2E4-7531626D3859}"><font color="#0000ff"><u>EndToEndActivity</u></font></a> covering the entire extent of a two people's marriage (from the ceremony to either divorce or death)

Note: As IES4 does not increase the scope of IES3, <a href="#{9DFEDF24-1203-4341-B282-BD37C1B9CDF5}"><font color="#0000ff"><u>Marriage</u></font></a> also includes common-law partners and civil partnerships

### <a id="{D03A0D8B-79F5-4901-97BC-2767FD46CD5F}"></a>Married
A <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> when a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> is married to another person

### <a id="{AE8FC416-9650-472d-99C6-F0A46B7359EB}"></a>Mass
The Measure of an Entity's resistance to acceleration as specified by the International System of Quantities

### <a id="{6CF79FCE-E2C9-4e8b-848C-39BD8616F77D}"></a>Measure
An Characteristic which is measurable on a scale

### <a id="{CCBBF963-EB27-40d5-BE9F-47CDF4D352F8}"></a>MeasureRange
A Measure specified by upper and lower bound Measures

### <a id="{161079F3-8089-4124-A67A-5D6A7A4EA511}"></a>measureUnit
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a Measure is represented using a particular UnitOfMeasure

### <a id="{3693B7DE-DCE7-4bf9-BC2A-A8914DA4A11E}"></a>MeasureValue
A <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> of the value of a Measure

Note: A UnitOfMeasure is almost always required. The reason it is not mandatory is that in some cases (due to partial reporting) we do not have complete information - e.g. we know the value was stated to be 10 but we don't know if that's metres or feet

### <a id="{CE2E2EB2-17F7-4054-9107-E8DC275B0B11}"></a>MediaFile
A DataObject that is a stand-alone file - e.g. a video, image or sound recording

### <a id="{6445E51F-3DDF-4dcf-ABDF-3ED123D53188}"></a>Meeting
A <a href="#{3524D10D-D9B0-416d-ADED-D5AAEB99DD09}"><font color="#0000ff"><u>CoLocation</u></font></a> where the attendees (Presence) communicate with each other

### <a id="{B499C172-310D-4c5f-BA92-93B1C7874EEB}"></a>MeetingChair
An Attendance where the <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> involved is the chair of a <a href="#{6445E51F-3DDF-4dcf-ABDF-3ED123D53188}"><font color="#0000ff"><u>Meeting</u></font></a>

### <a id="{70AEDFC7-2B17-43d8-BF49-B5ACF8812317}"></a>Message
A <a href="#{6698805F-F492-4f1f-954C-E1EB3C53E148}"><font color="#0000ff"><u>Communication</u></font></a> or <a href="#{2176DEAE-6B5A-4906-AE37-FC76B0A50C0D}"><font color="#0000ff"><u>OnlineContentEvent</u></font></a> where a message is sent

### <a id="{E1A85BEA-C374-4727-A189-E536BA248D98}"></a>messageContent
An attribute representing the content of a message

Example:
messageContent = See you at Waterloo station at 18:15

### <a id="{8787BE51-8FE0-4d76-97B4-608311434F5B}"></a>MilitaryAttack
A MilitaryEvent where force is used

Note: was called "Attack" in v3.x - now called "MilitaryAttack" to distinguish from domestic attacks, terrorist attacks, hacking attacks, etc.

### <a id="{8EA1764B-26BE-4a72-ADEF-385C4CD657C3}"></a>MilitaryEvent
An OperationalEvent that involves military staff

### <a id="{492AB59A-342E-4d74-B85B-E6CA95BBC3B2}"></a>MilitaryOrganisation
A <a href="#{0D042066-06C8-48d6-8387-500CF8EE2592}"><font color="#0000ff"><u>GovernmentOrganisation</u></font></a> that conducts warfighting, peacekeeping and emergency civil support functions

### <a id="{A6DED556-12B8-45b7-A69C-A6A3D813269B}"></a>missionPurpose
A short description of why an IntelligenceOperation was carried out used for legal justification

Agencies that work in the intelligence domain may wish to standardise these descriptions. 

### <a id="{3BF8FC71-64BD-4fb5-BEFD-D7FCB936FA12}"></a>MobileHandset
A CommunicationsDevice that is a portable telephone using cellular networks

### <a id="{9F5EDA24-5991-48e7-9303-C86E25A196CF}"></a>MobileTelephoneAccount
A <a href="#{593AE684-C2E9-4e40-A7FD-549BFA64900D}"><font color="#0000ff"><u>TelephoneAccount</u></font></a> where the telephones in use connects using a cellular network

### <a id="{7A879268-33C2-4f2b-8928-9E78AFF01E69}"></a>ModelOfDevice
A <a href="#{09F9136C-9069-47ec-A58E-FC26CF9BA55E}"><font color="#0000ff"><u>ClassOfDevice</u></font></a> where the model is specified

Examples:

* Apple iPhone 6S
* Ford Focus

### <a id="{21A341AE-9A38-4f45-BCB5-B29B02DC1B90}"></a>Modifier
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> participates in a <a href="#{3EF09CE4-79B0-42be-9AA1-12B97611BF2B}"><font color="#0000ff"><u>Modify</u></font></a> event as a modifier

### <a id="{3EF09CE4-79B0-42be-9AA1-12B97611BF2B}"></a>Modify
A LifecycleEvent where something is changed

### <a id="{D94ED70F-8CCA-4c6e-8AE5-65450BBA62D7}"></a>MoneyTransfer
A <a href="#{94CEDBD1-8E3D-4cb4-8155-FBD621DA6A0D}"><font color="#0000ff"><u>BusinessEvent</u></font></a> where an <a href="#{0DF94DE5-68B7-45b4-A106-A11CE06C31B8}"><font color="#0000ff"><u>AmountOfMoney</u></font></a> is moved from one <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a> to another.

Usually a Money Transfer event will involve two accounts but we might not know both, or it might be a cash transfer � in which case only one of the participants might be specified.

### <a id="{95B5ACC4-956A-4b29-AB9E-BDCD12EF319F}"></a>Movement
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> moves from one place to another.

### <a id="{D06C3801-F91C-436d-9D7F-DFDE29B48E5C}"></a>Moving
An EventParticipant in which an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> moves from one <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> to another

### <a id="{7D7CC966-56EB-4220-A650-A993E598F2E2}"></a>Name
A <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> that is used to refer to something, usually in context of a NamingScheme

Examples:

GBR - the ISO Trigram for the United Kingdom
GB - the FIPS two-letter code for the United Kingdom
"Michael Caine"  - stage name for Maurice Micklewhite

### <a id="{222534A5-25C8-4ecd-BE55-27DA1534D402}"></a>NamingScheme
An <a href="#{1F9AC8FE-3862-48d6-A3DC-E429B08D2B26}"><font color="#0000ff"><u>ClassOfClassOfEntity</u></font></a> whose instances collect together all Names that belong to a particular scheme - i.e. an organisational identity scheme, a systems primary key format, etc.

### <a id="{6AE6F8A5-F427-4ea6-BABD-5720F07430F5}"></a>Nation
The people of a <a href="#{92EBA9B9-48C2-4082-9FE5-603977BD6846}"><font color="#0000ff"><u>Country</u></font></a> (or group of Countries recognised as a Nation).

Note: this is distinct to a Country which is the land mass under control by the Nation, though ISO Country codes are regularly used to also identify Nations. 

### <a id="{843EDE77-78C4-4a09-9866-DBCC726AD5E6}"></a>NationalIdentityCard
An IdentityDocument issued by a Government to identify a Person

### <a id="{F2CF8705-DA4A-4131-AB60-CF1AC33BED95}"></a>NationalIdentityNumber
An Identifier of a Person that is specified by a GovernmentOrganisation 

### <a id="{45CDA5C1-624D-4f2f-81F6-EF19300820A9}"></a>nationality
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to a <a href="#{6AE6F8A5-F427-4ea6-BABD-5720F07430F5}"><font color="#0000ff"><u>Nation</u></font></a> which recognises the <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> (or <a href="$element://{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> of Person, as it is possible to renounce a nationality) as one of their nationals.

### <a id="{0C0728AF-B9F2-418f-A03E-107689F0ACA0}"></a>natureOfInterest
NatureOfInterest is limited to the following values:
� Personal
� Professional
� Academic

### <a id="{E3BB8B07-9CC5-407a-8CC7-E2B0E1B69476}"></a>nearTo
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> to another Entity it is proximate to in space

### <a id="{FB2EA8AE-164A-4642-82E3-D2622DC6FCCB}"></a>Negotiation
An <a href="#{422B4F1C-DA90-400b-8FFD-43C90B4F10F4}"><font color="#0000ff"><u>AgreementStage</u></font></a> where parties are trying to find agreement

### <a id="{D4B25AAF-F083-45ba-8188-25DE9D86013D}"></a>Negotiator
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> negotiates an agreement

### <a id="{1995033D-7AF2-468c-998D-61E86FB51B16}"></a>nephewOrNieceOf
A Relationship between two <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> Entities that indicates one is the nephew or niece of the other.

Note: people can become nephews or nieces at different stages in their lives (e.g. as people marry) so PersonState should be used in cases where someone has not always been related in this way (i.e. not from birth)

### <a id="{C544CCAC-91C5-4e82-B5D9-7A1B8D48E771}"></a>NetworkInterface
An <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a> (usually part of another Device) that provides wired or wireless access to a network.

Network interfaces can often be removable. To model this, create DeviceStates of the NetworkInterface and make them part of the Device which hosts the interface for that period of time. 

### <a id="{F33CAAA7-85A7-4e41-B0D4-3EAC4E6F73CC}"></a>nextTo
A <a href="#{E3BB8B07-9CC5-407a-8CC7-E2B0E1B69476}"><font color="#0000ff"><u>nearTo</u></font></a> linking an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> to another Entity it is immediately proximate to (i.e. touching) in space

### <a id="{BA4B97EE-58E2-4796-949C-F62EAAAE56C9}"></a>Nickname
A PersonName that is an unofficial or casual name

Note:
An nickname will often be applied to a <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> of the Person, as these tend to be non-permanent names

### <a id="{672C510D-8836-4a41-8921-C732DF430278}"></a>NonDisclosureAgreement
An <a href="#{1B39630B-B00F-4def-9C65-48082C4AD2E0}"><font color="#0000ff"><u>EndToEndAgreement</u></font></a> where parties agree not to disclose certain information

### <a id="{09649FE9-DDD7-4493-B9EC-7A716B0FC616}"></a>Northing
The GeoIdentity that is a representation of the northward componrnent of cartesian point on a map - i.e. on a 2D projection of the globe such as a mercator projection.

### <a id="{C2B4A066-E4A7-4cf5-BD1F-8381364F5D30}"></a>NotForProfitOrganisation
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> where all income is reinvested, or distributed - i.e. no profit is made.

### <a id="{15EF63E0-1223-4874-A2D4-43F75ACF5315}"></a>Notify
An OnlineContentEvent where a notification is raised - i.e.  an application-generated event (not a user-generated event)

### <a id="{222FBD07-DCCF-40c6-BD15-4ADBC64A8AA5}"></a>objectContent
The content of the data object.

Whenever a <a href="#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2}"><font color="#0000ff"><u>DataObject</u></font></a> is exchanged it must include either the ObjectContent or an ObjectContentReference or both.

The ContentStandard qualifier specifies the standard (either by name or by reference) that is applicable to the content of the DataObject.

The ContentFormat qualifier specifies the <a href="#{EF2C13D4-7106-4799-BB72-7CD47714F257}"><font color="#0000ff"><u>format</u></font></a> of the content of the DataObject.

### <a id="{6B06ABDD-05CF-485c-A483-563C5E85F189}"></a>objectContentReference
An ObjectContentReference is a resolvable reference to the �content� of the respective DataObject.

Whenever a <a href="#{CAC97EB4-E0E8-4576-9637-1FBED5F9FEF2}"><font color="#0000ff"><u>DataObject</u></font></a> is exchanged it must include either the ObjectContent or an ObjectContentReference or both.

### <a id="{9A372833-B327-4cb0-9950-786A2FBF7CC3}"></a>ObjectName
A Name given to a DataObject.

### <a id="{8CA40CCF-A099-49fd-80CB-CA6DA733FAB4}"></a>Observation
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where an <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> (Event or Entity) is observed by an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> (i.e. a <a href="$element://{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> or Device)

### <a id="{CC05ABD0-7BAB-4484-8E8C-ED07C1AA3C93}"></a>Observed
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> is <a href="#{CC05ABD0-7BAB-4484-8E8C-ED07C1AA3C93}"><font color="#0000ff"><u>Observed</u></font></a>

### <a id="{C58A1AB4-19E2-48d0-B606-3BDFC5DD3860}"></a>Observer
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> observes another Entity or <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a>

### <a id="{FB2FDA67-B258-4b18-9E95-3B9DFAB8FB14}"></a>ObserverStatus
When a <a href="#{D62DDBB8-53FC-405a-BC43-89CA337563A0}"><font color="#0000ff"><u>Government</u></font></a> has observer rights at a <a href="#{78D65599-BCBB-491a-8C34-75B9F7AB60D5}"><font color="#0000ff"><u>Summit</u></font></a>

### <a id="{66A24EF2-F417-46c7-A68D-D4540260F64F}"></a>OffenceCode
An Identifier for a ClassOfCriminalActivity

The Home Office Offence Classification Index [B] should be used wherever possible to specify the Crime Type

### <a id="{1D589649-490D-4558-91D5-2D977B2B42DE}"></a>OfferForSale
A <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> where one or more Entities of the same type (specified by an ClassOfEntity) are offered for sale or exchange

### <a id="{80AFD655-A969-46be-BE72-035C053C1C4F}"></a>OnJourney
An EventParticipant in which an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is on a <a href="#{8B571665-0AA1-40be-A7A0-A35BE86B7192}"><font color="#0000ff"><u>Journey</u></font></a> (i.e. a multi-part journey)

### <a id="{E95170B9-2599-46dc-BEDC-012B08F09D43}"></a>OnlineAccount
An Account that enables a person, organisation or other entity to participate within a particular online domain.

Note: was called "OnlineIdentifier" in previous versions of IES

### <a id="{BCFD5BED-785D-4c5d-B004-2C8A5C7B40C3}"></a>OnlineAccountInUse
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{E95170B9-2599-46dc-BEDC-012B08F09D43}"><font color="#0000ff"><u>OnlineAccount</u></font></a> participates in an <a href="#{24499751-7D9B-4f2e-B880-8D5BC4FCEF30}"><font color="#0000ff"><u>OnlineEvent</u></font></a>

### <a id="{2CF1B157-A2F6-41c8-8A87-7B82EEB71F40}"></a>onlineAccountProvider
Relates an <a href="#{E95170B9-2599-46dc-BEDC-012B08F09D43}"><font color="#0000ff"><u>OnlineAccount</u></font></a> to the <a href="#{27BEFD0A-B30B-47db-B863-13E48D1172F9}"><font color="#0000ff"><u>OnlineService</u></font></a> that provides and administers the account.

Note:  was called "Domain" in previous IES versions

### <a id="{4C0D1724-B820-4a87-AD36-08C0612CE21E}"></a>OnlineAccountState
A temporal state of an <a href="#{E95170B9-2599-46dc-BEDC-012B08F09D43}"><font color="#0000ff"><u>OnlineAccount</u></font></a>

### <a id="{54500458-51CF-46b5-A5A3-14B1D5C7F755}"></a>OnlineArtefact
A WebResource which is any kind of media presented online that is more granular than a webpage, and user-generated - e.g. a blog post, tweet, facebook post, etc.

Note: when applying begin and end states (and periods of time) to OnlineArtefact, the times should correspond to the life of the content, not the <a href="#{5382F9B3-0A28-4245-8EEB-BF3CEFFD4058}"><font color="#0000ff"><u>duration</u></font></a> of the posting activity.

### <a id="{FE21E354-7770-4e6b-A7EA-E012F759E835}"></a>OnlineArtefactInEvent
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{54500458-51CF-46b5-A5A3-14B1D5C7F755}"><font color="#0000ff"><u>OnlineArtefact</u></font></a> participates in an <a href="#{24499751-7D9B-4f2e-B880-8D5BC4FCEF30}"><font color="#0000ff"><u>OnlineEvent</u></font></a>

### <a id="{FF216817-5B58-4db5-88C5-20AE6A466265}"></a>OnlineComment
An OnlineArtefact that is a comment on an existing OnlineArtefact instance

### <a id="{0A4C12E6-CA4C-43f1-9C6C-FBE23197975F}"></a>onlineCommentOn
Relates an <a href="#{FF216817-5B58-4db5-88C5-20AE6A466265}"><font color="#0000ff"><u>OnlineComment</u></font></a> to the OnlineContent that was commented on

### <a id="{DB70D7EE-5076-4eb2-950B-63C71A3C8859}"></a>OnlineContentCreation
An OnlineContentEvent where a "post" is made.

Examples:

* Posting a blog
* Posting a comment
* Tweeting (other microblogs are available, probably)
* A Facebook, LinkedIn, Instagram, etc. post

### <a id="{2176DEAE-6B5A-4906-AE37-FC76B0A50C0D}"></a>OnlineContentEvent
An <a href="#{24499751-7D9B-4f2e-B880-8D5BC4FCEF30}"><font color="#0000ff"><u>OnlineEvent</u></font></a> where content (text, images, video, etc.) is uploaded, downloaded or viewed

### <a id="{24499751-7D9B-4f2e-B880-8D5BC4FCEF30}"></a>OnlineEvent
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> on the internet

### <a id="{5B50EECC-45FC-4e5b-933E-51BC0FEE0FCD}"></a>OnlineLike
OnlineArtefact that is a "like" of an existing OnlineArtefact instance

### <a id="{4A3F24C6-EEC9-48ce-93FB-26FF64E1268A}"></a>onlineLikeOf
Relates an <a href="#{5B50EECC-45FC-4e5b-933E-51BC0FEE0FCD}"><font color="#0000ff"><u>OnlineLike</u></font></a> to the OnlineContent that was "liked"

### <a id="{34F13F26-7C4E-451a-BDA0-62BA7738039F}"></a>onlinePublisher
Relates an <a href="#{54500458-51CF-46b5-A5A3-14B1D5C7F755}"><font color="#0000ff"><u>OnlineArtefact</u></font></a> to the <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> that produced it.

### <a id="{27BEFD0A-B30B-47db-B863-13E48D1172F9}"></a>OnlineService
A service provided on the internet.

### <a id="{DEE1404A-AAC3-4d46-9BA3-8E097A55C7F5}"></a>onlineServiceProvider
Relates an <a href="#{27BEFD0A-B30B-47db-B863-13E48D1172F9}"><font color="#0000ff"><u>OnlineService</u></font></a> to the <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> that owns/runs it

### <a id="{2C9CEF7F-FA9A-4a0e-9E2C-AC3D3EB51D5C}"></a>onlineServiceType
The class of <a href="#{27BEFD0A-B30B-47db-B863-13E48D1172F9}"><font color="#0000ff"><u>OnlineService</u></font></a>

### <a id="{980404C4-C512-4f36-B3B1-5088CC754DCF}"></a>OnlineShop
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> participates in a <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> as an online shop

### <a id="{A8B06392-A9A3-4de4-93FB-24F08A546434}"></a>OpenAccount
An AccountAdminEvent where a new Account is opened

### <a id="{4F83D781-7E46-4ad4-B2A5-ECD27565EA49}"></a>OperatingSystem
<a href="#{B6014BB6-FD82-4748-8DFF-65401770515C}"><font color="#0000ff"><u>Software</u></font></a> that provides the basic access layer to hardware

### <a id="{59121C21-38E4-4224-8C2D-4D3E94A3A0D9}"></a>OperationalEvent
An Event conducted by military or national security actors

### <a id="{6730B57A-3E53-4bd2-B784-78C4FB239DBF}"></a>Operator
A ResponsibleActor's role in an <a href="#{59121C21-38E4-4224-8C2D-4D3E94A3A0D9}"><font color="#0000ff"><u>OperationalEvent</u></font></a> where they are one of the operators 

### <a id="{436E6ABB-C1E3-484e-B15B-63E700B27EA8}"></a>opposedTo
A coupling between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (or state thereof) and an <a href="#{3C13E07D-5796-4d03-9EBC-C75277E87CA4}"><font color="#0000ff"><u>ClassOfElement</u></font></a> to which they are opposed

Examples: an organisation that is opposed to Nuclear Weapons

### <a id="{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"></a>Organisation
A ResponsibleActor that is a group of people formed for one or more of purposes � e.g. government organisations, educational organisations, terrorists organisations, religious organisations, etc.

### <a id="{C0B7C4B2-C067-4ca8-A9FB-E82782889250}"></a>OrganisationalRole
A <a href="#{0066A327-D497-42e0-9F50-D988F522F4A5}"><font color="#0000ff"><u>Role</u></font></a> that a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> can have in an <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a>

### <a id="{13865B40-B57D-44e7-9658-00C45C8175C8}"></a>OrganisationIdentifier
A unique Identifier for an Organisation (more usually an OrganisationState)

Example:
DUNS number
VAT number
Companies House Number
Registered Charity Number

### <a id="{065C9B64-96E2-47f5-9769-E7942C1A208F}"></a>OrganisationName
A <a href="#{7D7CC966-56EB-4220-A650-A993E598F2E2}"><font color="#0000ff"><u>Name</u></font></a> used to identify an <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a>

### <a id="{F3DB6A59-B2DE-4743-A9A8-7DA9CCC68638}"></a>OrganisationState
A temporal state of an <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a>

### <a id="{71249792-E0AF-4f98-86ED-17115F1734A7}"></a>orGroup
The groups (if any) which the requesting user must be a member of at least one of in order to access the item. See the EDH specification for further details.

Allowable Values:

See EDH Standard

### <a id="{D4A003A3-7FEF-409c-8935-743CD97299E7}"></a>originatingSystem
The <a href="#{F682A265-1AFE-4287-A9CD-0D4C83F54C52}"><font color="#0000ff"><u>System</u></font></a> that produced the dataset

### <a id="{4978D7F3-E686-4b30-9356-F0C4DC7A158D}"></a>originator
The <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> that produced the dataset

### <a id="{697EAA12-8FD3-49e0-A4A2-A045B4570550}"></a>OSGridReference
A GeoIdentity that is an Ordnance Survey Grid Reference - i.e. pertaining to Great Britain.

### <a id="{A5516CD2-940B-4827-B38A-AD86AF934E99}"></a>OutgoingGovernment
The <a href="#{D62DDBB8-53FC-405a-BC43-89CA337563A0}"><font color="#0000ff"><u>Government</u></font></a> that left power following a ChangeOfGovernment

### <a id="{FDD94D9F-F343-4c1b-9688-752C896A3C7C}"></a>owns
A Relationship between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and an <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a> they legally own

### <a id="{6F13083C-505A-473e-9EDB-B0E534A341FB}"></a>parentOf
A Relationship between two <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> Entities that indicates one is the parent of the other

### <a id="{B6A503E5-3FC4-4a45-8DC0-994EA31A895A}"></a>Parked
A temporal state of a <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> where it is not moving. 

Examples:
* A car parked on the roadside
* A ship in dock or at anchor
* An aircraft parked on the tarmac or in a hangar

### <a id="{2173F463-524C-457c-B106-51322F64F122}"></a>ParticularPeriod
A <a href="#{3FDFA898-C340-4279-8B3C-275359D5B02D}"><font color="#0000ff"><u>PeriodOfTime</u></font></a> that is a specific, contiguous extent of time.

IMPORTANT NOTE: The URI of a <a href="#{2173F463-524C-457c-B106-51322F64F122}"><font color="#0000ff"><u>ParticularPeriod</u></font></a> shall be encoded as follows:

http://iso8601.iso.org/2007-01-18T15%3A00%3A00

Where the content <a href="#{FA4DDF04-16DA-4b5c-AE9A-6AB8CD07DCDB}"><font color="#0000ff"><u>after</u></font></a> the / is % encoded (e.g. encodeURIComponent in javascript). In the example above, the unencoded content would be "2007-01-18T15:00:00"

The reason behind using a URI is that receiving systems can resolve the periods of time and de-duplicate. 

Examples:

Tuesday 28th August 2018
2016
December 1944

### <a id="{772CD8A3-3DCA-4cc7-8BA3-17D1C57E94BC}"></a>PartNumber
A unique Identifier for the a ModelOfDevice

Note:  this is different to a serial number which is unique to each <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a>

### <a id="{3EFEA421-6B88-4e51-9B20-4FFA22E8C5CA}"></a>PartOfFacility
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> that is contained within a Facility - e.g. a room, laboratory, floor, etc.

### <a id="{A5713B2C-E098-4dd2-BD46-42DA51899FEA}"></a>PartyInCommunication
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> that is part of (usually one end of) a <a href="#{6698805F-F492-4f1f-954C-E1EB3C53E148}"><font color="#0000ff"><u>Communication</u></font></a> Event.

Sometimes, all we know about a <a href="#{A5713B2C-E098-4dd2-BD46-42DA51899FEA}"><font color="#0000ff"><u>PartyInCommunication</u></font></a> is their <a href="$element://{A82378B9-9774-46b9-9845-CC75BE882F06}"><font color="#0000ff"><u>CommunicationsIdentifier</u></font></a> (phone number, e-mail address, maybe even just an IP address) so the <a href="$element://{FBA54EEF-91BF-4ba2-8B67-79C899963149}"><font color="#0000ff"><u>isIdentifiedBy</u></font></a> <a href="$element://{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> may be applied to PartyInCommunication

### <a id="{AF57E842-9BF7-4f6e-B180-DDEACB0F5386}"></a>PartyToAgreement
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> is party to an EndToEndAgreement

Note:  this includes EndToEndAgreements that were never ratified - i.e. they got to the negotiation stage but were never put into force

### <a id="{D6D07656-1866-4cb4-97A7-FC4C1CB65416}"></a>Passenger
A <a href="#{9888A3F3-7E9B-4806-BD4E-2FC4D87A5902}"><font color="#0000ff"><u>PersonInTransit</u></font></a> where the <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> travelling is a <a href="#{D6D07656-1866-4cb4-97A7-FC4C1CB65416}"><font color="#0000ff"><u>Passenger</u></font></a> on a <a href="$element://{7693D2C9-0F06-4005-BB8D-B5B572B2281A}"><font color="#0000ff"><u>Transit</u></font></a>

### <a id="{E5C1270D-35AD-4f86-B0E4-1DC0039174E3}"></a>PassengerName
The Name of the Person being used for Travel - it may not be known if this is the actual Name the Person travelling, as someone else may be using their ticket.

### <a id="{13ABC7CA-915E-4069-8EA7-FD205A5336C5}"></a>Passport
An IdentityDocument that confirms a Person's nationality and permits them to cross national boundaries

### <a id="{10DEB6B8-80CC-4bfc-B10F-1830B559C21F}"></a>payloadContents
A link from an <a href="#{749B002E-37B1-4754-B3B2-96642B3CF4A7}"><font color="#0000ff"><u>ExchangePayload</u></font></a> to an rdfs:Resource that is in that payload.

If there is no payloadContents link, then it is assumed that all the contents of the file are in the ExchangePayload. Under this circumstance, more than one ExchangePayload would be an error. 

The payloadContents link will usually refer to a named graph, but it can also be used to refer to individual rdf:Statements and rdfs:Resources.

### <a id="{259167E4-D0B3-4f03-9653-CAD778F5F6F3}"></a>payloadLabel
A mandatory link from an <a href="#{749B002E-37B1-4754-B3B2-96642B3CF4A7}"><font color="#0000ff"><u>ExchangePayload</u></font></a> to the <a href="#{CED628E4-8641-486b-BCD7-CB4E147E7AE6}"><font color="#0000ff"><u>SecurityLabel</u></font></a> that provides the default access control for all statements in the payload.

Note: individual statements may deviate from the default by applying their own SecurityLabels

### <a id="{9882D901-1B22-4b89-81D1-031F840A20D0}"></a>PaymentArtefact
An Asset that is means of payment

### <a id="{C793E699-C27B-49cc-9358-C4A0E17E609E}"></a>paymentArtefactProvider
The <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that provided the <a href="#{9882D901-1B22-4b89-81D1-031F840A20D0}"><font color="#0000ff"><u>PaymentArtefact</u></font></a>

### <a id="{10FBBF98-4604-46d9-AD12-211597532B9E}"></a>PeaceTreaty
A <a href="#{59599C4B-F3DE-49a0-B76F-BE4CB1293CBA}"><font color="#0000ff"><u>Treaty</u></font></a> that formalises the end of hostilities in a <a href="#{D4F568F5-7BC4-489d-94BC-AE1305E5C0C2}"><font color="#0000ff"><u>War</u></font></a>

### <a id="{3FDFA898-C340-4279-8B3C-275359D5B02D}"></a>PeriodOfTime
A <a href="#{3FDFA898-C340-4279-8B3C-275359D5B02D}"><font color="#0000ff"><u>PeriodOfTime</u></font></a> is an <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> whose spatial extent is everywhere, but whose temporal extent is limited. 

### <a id="{FA623989-B6A4-40e2-A956-B8FFEA478895}"></a>permittedNationality
The nationalities of those who are permitted to access the item. See the EDH specification for further details.

Allowable Values:

See EDH Standard

### <a id="{90F3E89D-1456-41fe-9354-4E13C4D79564}"></a>permittedOrganisation
The organisations who are permitted to access the item. See the EDH specification for further details.

Allowable Values:

See EDH Standard

### <a id="{D625B538-7D72-4d7d-BA50-D79712A264ED}"></a>Perpetrator
An <a href="#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B}"><font color="#0000ff"><u>Actor</u></font></a> where the <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> conducts a <a href="#{43E58528-16E4-48b3-8F13-10500879EA83}"><font color="#0000ff"><u>CriminalActivity</u></font></a>

### <a id="{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"></a>Person
A human being, living or dead. This also includes what may appear to be a person, but is in fact an Alias

### <a id="{9D84921F-87A3-4ee9-8A3D-A88F564295FA}"></a>PersonalRadioHandset
A CommunicationsDevice for portable radio communications - e.g. a walkie-talkie

### <a id="{57060AD9-A6D7-496d-A2BF-22B930400EEE}"></a>PersonHeight
The Length that is the height of a PersonState

### <a id="{0383D09B-8C40-417d-8C1A-75220EAF496E}"></a>PersonInCommunication
A <a href="#{38F8B795-0BCE-4945-8C69-8678ED935C1A}"><font color="#0000ff"><u>PersonState</u></font></a> (and an EventParticipant) when a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> is involved in communicating. 

### <a id="{9888A3F3-7E9B-4806-BD4E-2FC4D87A5902}"></a>PersonInTransit
An <a href="#{74169219-A47C-48ce-A25F-3948E7E873B6}"><font color="#0000ff"><u>EntityInTransit</u></font></a> where the <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>

### <a id="{F114F86C-3BA8-4be7-A686-A1D80002DF28}"></a>PersonName
A <a href="#{7D7CC966-56EB-4220-A650-A993E598F2E2}"><font color="#0000ff"><u>Name</u></font></a> used to identify / refer to a Person

Note: this is the full name as known to the organisation managing the NamingScheme. For first names, surnames, etc. use a subtype of PersonName

A <a href="#{F114F86C-3BA8-4be7-A686-A1D80002DF28}"><font color="#0000ff"><u>PersonName</u></font></a> may be composed of Surname, GivenName, etc. using the <a href="#{7238489D-6802-4733-9F7F-9B31D02B3C81}"><font color="#0000ff"><u>inRepresentation</u></font></a> <a href="$element://{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a>

### <a id="{38F8B795-0BCE-4945-8C69-8678ED935C1A}"></a>PersonState
A temporal state of a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>

### <a id="{CA36058B-835C-48ef-944A-2507708ADA71}"></a>PersonTitle
The title associated with the name of the person.

### <a id="{37DB1A2C-9382-4dac-8AE8-9DEC5A337E16}"></a>PlaceName
A <a href="#{7D7CC966-56EB-4220-A650-A993E598F2E2}"><font color="#0000ff"><u>Name</u></font></a> that is used to refer to a Location.

Note:  the naming pattern is used here as different parties (even standards bodies !) may have different names for the same <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a>

### <a id="{A11A426E-ED15-4aaf-B9A5-02A4060533AA}"></a>PointOnEarthSurface
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> that is a point (mathematically speaking, of vanishing area) on the surface of the WGS84 spheroid

### <a id="{345E8F46-AC41-452b-B2F9-694DBED556FD}"></a>PolicyAnnouncement
A PoliticalAnnouncement about policy

### <a id="{686C8BFB-6CB2-4185-9FCF-89D2D4BB3051}"></a>PoliticalAgreement
A PoliticalEvent that is also an EndToEndAgreement

Note: was called Agreement in IES 3.x, but that was confusing for business agreements, personal agreements, etc.

### <a id="{53D5957B-E4B6-4cbb-8CE9-887F7152820F}"></a>PoliticalAnnouncement
A PoliticalEvent where information is released to the public

Note: was called Announcement in IES 3.x, but that was confusing for business announcements , personal announcements , etc.

### <a id="{3A0E6FDD-5B3B-4092-9549-C05E8A5FED41}"></a>PoliticalEvent
An Event related to democratic processes or party politics

### <a id="{57860A04-0128-4c7e-9BFD-83D3BA432F8C}"></a>Port
A <a href="#{9CD2C1B1-85B1-4579-9376-07827AD68461}"><font color="#0000ff"><u>Facility</u></font></a> which is a recognised terminus for international travel

### <a id="{15E93B86-6969-47f2-8036-0B7B96E9BDA2}"></a>PossibleWorld
An Element that encompasses a number of Events, Entities and States that may occur / have occurred. A PossibleWorld is used for scenario planning and forensics.  

This is a very simple placeholder for an area of IES that is likely to grow in the future. For now, it can be used to group together a number of elements (using isPartOf relationship) to assert that they share the same truth - i.e. in one possible scenario, all of them were true. The same Element may exist in more than one PossibleWorld - i.e. scenarios may share elements. For version 4.1.0 of IES, PossibleWorld is to be used with AssessToBeTrue in order to specify a level of confidence or probability. More work is needed on this in later IES versions. 

### <a id="{7C28E83C-1895-4901-ABF8-9D78C9C12C62}"></a>Post
A part of an <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that has particular responsibilities

### <a id="{6A0385E2-3FB1-4a42-A254-BC382D92E27A}"></a>PostalCode
A GeoIdentity used to (partially) identify and address

### <a id="{2B02EF33-E12A-42ec-B047-533F6D8F159D}"></a>postModificationState
A partOf <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate a <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> of an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> just <a href="$element://{FA4DDF04-16DA-4b5c-AE9A-6AB8CD07DCDB}"><font color="#0000ff"><u>after</u></font></a> the <a href="$element://{3EF09CE4-79B0-42be-9AA1-12B97611BF2B}"><font color="#0000ff"><u>Modify</u></font></a> event

Note: For BORO purists, this means the post State is part of the Modify <a href="$element://{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> (i.e. the extent of the Modify Event includes the State)

### <a id="{DB51B007-E3E8-431f-9C23-3C0A7E83FB11}"></a>PostState
A temporal state of a <a href="#{7C28E83C-1895-4901-ABF8-9D78C9C12C62}"><font color="#0000ff"><u>Post</u></font></a>

### <a id="{D4BD48E8-76B8-4d3c-AB83-E653DB89170D}"></a>powertype
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts one Class is the powerset of the other (see Cantor's theorem).

### <a id="{4E954855-D50A-42ab-9401-4B1C890542AD}"></a>preModificationState
A partOf <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate a <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> of an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> just prior to the <a href="$element://{3EF09CE4-79B0-42be-9AA1-12B97611BF2B}"><font color="#0000ff"><u>Modify</u></font></a> event

Note: For BORO purists, this means the pre State is part of the Modify <a href="$element://{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> (i.e. the extent of the Modify Event includes the State)

### <a id="{8404464D-3904-4c59-AE0E-B3FAFB46AC4E}"></a>Presence
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is CoLocated with other Entities of interest

### <a id="{885EA1C2-29D7-4b7c-B479-D43E4F77B5BD}"></a>Prisoner
A person's role when incarcerated

### <a id="{024133FE-9D0B-4e5d-A97D-A34B5EA01C41}"></a>Prosecution
A LawEnforcement Event that is the trial of a suspect

### <a id="{ABDC5FD5-3281-4cd5-A9B0-188292D8C6B7}"></a>Prosecutor
A person's role as a prosecutor in a trial

### <a id="{7E5590F8-B142-49d8-8FB0-414716CF9F16}"></a>protectiveMarking
The classification applied to the respective item. This is equivalent to the Classification field within the EDH

Allowable Values:

OFFICIAL
OFFICIAL-SENSITIVE
SECRET
TOP SECRET

### <a id="{CD6E380B-7AD4-43d6-A128-9C666ABD8223}"></a>publicationDate
The date of publication of the respective document.

### <a id="{0A9A9F7D-A6F1-4629-BD2B-7990D2D36493}"></a>Purchase
A <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is bought

### <a id="{B10A694D-31AA-456c-8C51-B7B5F101A39F}"></a>Purchaser
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> participates in a <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> as a purchaser

Note: in the case of a RequestForQuotation, the purchaser is the person or organisation issuing the RfQ

Note: in the case of an online purchase where the buyer is unknown, the participant may be an OnlineIdentifier

### <a id="{7550DA0F-DF0E-4c61-9198-5DE767677A3A}"></a>quantityDelivered
The number of Entities (of the same type) that were delivered

### <a id="{AEC476A1-AE39-4a9e-9EE3-DD45B50B0F26}"></a>quantityOffered
The number of Entities (of the same type) that are being offered for sale

### <a id="{0D2231E8-6AF1-4e59-B8FA-86A26334CC71}"></a>quantityPurchased
The number of Entities (of the same type) that were purchased

### <a id="{3B5E5043-30C2-4e67-86C8-F59F55AEBA90}"></a>radioCoverage
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking a RadioMast to its RadioCoverageArea

### <a id="{7A2CC7C7-6B82-4751-BDBE-A770B3AFBBEB}"></a>RadioCoverageArea
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> whose area is that in which a <a href="#{F02CFF55-12A7-4308-9A60-E2353DE5BE58}"><font color="#0000ff"><u>RadioMast</u></font></a> hast viable communications coverage.

Note: The RadioMast itself may not be part of this area, as often the immediate area around the base of a RadioMast is a deadspot. 

Note: Most radio area coverage is complex in shape, and the preferred representation in IES4 is <a href="#{417C1F4E-6A5D-4631-B275-8E982252791A}"><font color="#0000ff"><u>GeoJSON</u></font></a>. No attempt is made here to differentiate between signal strength zones. To do this, create multople RadioCoverAreas for the same RadioMast and label them appropriately. 

### <a id="{F02CFF55-12A7-4308-9A60-E2353DE5BE58}"></a>RadioMast
An <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a> that is placed in a Location to provide either a link from a wired to wireless connection, or to relay between two wireless endpoints.



### <a id="{31977608-5432-4d6f-AEE0-19838197C813}"></a>Ratification
An <a href="#{422B4F1C-DA90-400b-8FFD-43C90B4F10F4}"><font color="#0000ff"><u>AgreementStage</u></font></a> where parties have arrived at a consensus and approve the agreement

### <a id="{8E0DF17F-34EE-43c6-8DA4-30F698384FD3}"></a>RealEstate
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> (and an Asset) that has been defined or constructed for the purpose of ownership

### <a id="{25965198-3FE0-4bb9-BCA9-808E15A3EE49}"></a>ReceivingAccount
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a> receives money

### <a id="{AAC709FB-0B88-4517-B5BB-FE2320992073}"></a>Recipient
An <a href="#{A5713B2C-E098-4dd2-BD46-42DA51899FEA}"><font color="#0000ff"><u>PartyInCommunication</u></font></a> where the communicating party is the recipient of a message

### <a id="{88E8F5E6-AFE5-4376-8112-EC294A673923}"></a>Reconnaisance
An IntelligenceOperation where an Entity or Event is observed for the purposes of planning

### <a id="{442AC7F0-AE57-4090-88D6-55A3825ECEAA}"></a>recurrentPeriodRepresentation
A modified ISO8601 <a href="#{EF2C13D4-7106-4799-BB72-7CD47714F257}"><font color="#0000ff"><u>format</u></font></a> (hence use of xsd:string) where elements of the time/date are blanked with ?? characters. The purpose of this is to be able to specify e.g.  a time of day with no date - i.e. all recurrences of that time of day.

### <a id="{986E66AC-9092-410b-88AD-30B86EFC32DD}"></a>RecurringPeriod
A <a href="#{3FDFA898-C340-4279-8B3C-275359D5B02D}"><font color="#0000ff"><u>PeriodOfTime</u></font></a> that is composed of regularly recurring periods of time.

ISO8601 is used to represent these periods (recurrentP<i>eriod </i>property), using the blanking technique (e.g. blanking the date to give a daily time). The recurrence can be limited using the recurringFrom<i> </i>and <i>recurringUntil </i>properties 
Examples:

Every Tuesday from 28th August 2018 to 2 October 2018
13:00 to 14:00 on every day from 27th June 2016 to 2 October 2024

### <a id="{A0DC70DD-9237-480b-A712-F5381C5FFA1A}"></a>ReferenceNumber
An Identifier used to uniquely identity a document.

### <a id="{FC55D479-07C4-4d98-B48C-5032190E493D}"></a>RegionalConstituency
The people residing (or entitled to reside / vote in) a particular Location.

### <a id="{B3B6D7F3-F5B0-49d6-886F-F5AF7C56F041}"></a>regionCountry
An <a href="#{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate a <a href="#{65D869DB-19EE-4886-98BA-E579C39C4A68}"><font color="#0000ff"><u>RegionOfCountry</u></font></a> is in a <a href="$element://{92EBA9B9-48C2-4082-9FE5-603977BD6846}"><font color="#0000ff"><u>Country</u></font></a>

### <a id="{65D869DB-19EE-4886-98BA-E579C39C4A68}"></a>RegionOfCountry
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> that is a general subdivision of a Country

e.g. cities, towns, counties, states, etc.

### <a id="{18C405CE-CC09-4e02-A44D-0FB00C6F6B37}"></a>RegionOfWorld
A <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> that is a general subdivision of the world - e.g. continents, sub-continents, economic areas, etc.

Regions of the world may sometimes be spatially separated (e.g. economic areas)

### <a id="{1E784B9C-1A5D-4035-B134-67A758FB869D}"></a>RegistrationNumber
The registration number for the respective <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> (with or without spaces).

For road vehicles this is often referred to as the VRN (vehicle registration number).

For aircraft the tail number is often used as a means of identification and/or registration.

### <a id="{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"></a>relationship
A relationship represents an association between two Entities

### <a id="{BD538820-CE91-4b9a-ADB8-C105FE0F2E7B}"></a>Religion
An <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> whose extent is all the people (PersonState) who share the same belief.

Religions may be part of other religions - e.g. Christianity being made up of Catholic, Protestant, Orthodox, etc. 

1. The religion �practiced� by the respective Person..
2. The religion may be qualified to identity a particular sect.
3. The Metropolitan Police standard [F] shall be used as the reference data standard

### <a id="{E7B02F98-C52E-4db0-AF32-3D5131710EE7}"></a>ReligionState
A temporal state of an <a href="#{BD538820-CE91-4b9a-ADB8-C105FE0F2E7B}"><font color="#0000ff"><u>Religion</u></font></a>

### <a id="{2978340B-C4AA-4331-A68D-54A158798DAC}"></a>ReligiousOrganisation
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> formed around a particular religious belief

### <a id="{F38D2E58-C29A-4e3c-93BF-C33800969720}"></a>RentalAgreement
An <a href="#{1B39630B-B00F-4def-9C65-48082C4AD2E0}"><font color="#0000ff"><u>EndToEndAgreement</u></font></a> where one Party rents an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> to another

### <a id="{8ECC64A4-CED0-4122-AB54-64EA870837FC}"></a>RentalProvider
A <a href="#{AF57E842-9BF7-4f6e-B180-DDEACB0F5386}"><font color="#0000ff"><u>PartyToAgreement</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> provides an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> to rent

### <a id="{E5C65CAB-65BE-4502-8B46-5C5CC3C73B00}"></a>Rented
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is rented

### <a id="{E2FC3A09-EC9D-4ab9-B273-A526CB511B5A}"></a>Renter
A <a href="#{AF57E842-9BF7-4f6e-B180-DDEACB0F5386}"><font color="#0000ff"><u>PartyToAgreement</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> rents an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> from another party

### <a id="{8D510CB0-C9BF-4de3-A442-9070ABB15732}"></a>Report
A WorkOfDocumentation that offers one or more persons view on a particular topic. 

### <a id="{675A5C23-0746-43d0-96D0-AF0DF72CD697}"></a>Representation
An <a href="#{D1B2FB30-36CA-4012-B85F-514E270BF541}"><font color="#0000ff"><u>ClassOfEntity</u></font></a> whose instances are representations of things in the real world

Examples:
* an identifier used for a Person
* a document (though not an individual copy of a document)

### <a id="{AE00F1DE-F42B-4fc0-B07B-21F754F16FD4}"></a>representationValue
The examplar text, number, etc. of a <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a>

### <a id="{C0273975-049B-40f0-817C-DFBFA4A3E5CE}"></a>RequestDocument
A <a href="#{F0B48978-D4E4-45a4-8238-091A5B714D82}"><font color="#0000ff"><u>WorkOfDocumentation</u></font></a> that requests permission

### <a id="{132AFC03-7A64-45fa-9F87-93171BBFBE3D}"></a>requestedActivityType
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking an <a href="#{1D6BAE08-B8F1-4eee-928E-991B3B46EADF}"><font color="#0000ff"><u>AuthorisationRequest</u></font></a> to a <a href="#{057C04F9-EB8A-4e21-9CF8-2D98038570FB}"><font color="#0000ff"><u>AuthorisedEventClass</u></font></a> that the request requires authorisation to do.

For example, someone making request authorisation to travel



### <a id="{300203EC-607A-4d77-AE6F-7EAE7FA44DF2}"></a>RequestForQuotation
A <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> where one or more Entities are is required

### <a id="{CDF94674-D458-4996-9A99-6CBFFF3907EB}"></a>Reservation
<a href="#{487778E0-4BD7-4d9a-B7F7-63731478E1A2}"><font color="#0000ff"><u>Rights</u></font></a> where the rights holder has reserved some future event - e.g. hotel reservation, travel reservation, delivery, etc.

### <a id="{6BC3DDD8-477E-4c8a-B85D-E637CF9DB6DF}"></a>residesIn
A Relationship between a <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> and a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> at which they registered as a resident.

Note this is legal / administrative construct. See also StaysAt

### <a id="{EEBCE0A4-4882-4c95-9C2D-93CE5EB7A275}"></a>respectfulOf
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one respects the other.

Note: this should not be considered a bi-directional relationship. Just because one person respects another person does not necessarily mean the feeling is reciprocated. 

### <a id="{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"></a>ResponsibleActor
An <a href="#{B2B15802-9CE9-4a9d-9DE0-8289D8474E9B}"><font color="#0000ff"><u>Actor</u></font></a> that can be held legally responsible for their actions - generally a <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> or an Organisation. This also includes Posts which may be filled by people or organisations.

Note: there are many situations (mostly due to the law) where a Person or <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> can be the subject of a <a href="$element://{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> or <a href="$element://{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> interchangeably. Hence the need for a parent class in the IES ontology. 

### <a id="{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"></a>ResponsibleActorState
A temporal state of a ResponsibleActor

Note:  this is the superclass of <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (the whole life person or organisation) because the whole-life state is just a special case of a ResponsibleActorState. This pattern is true for all states. 

### <a id="{BA2472AB-56F0-462e-9460-F0192ABCD979}"></a>Retailer
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> participates in a <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> as a retailer

### <a id="{487778E0-4BD7-4d9a-B7F7-63731478E1A2}"></a>Rights
An <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a> which encompasses the legal rights to an <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> 

Strictly speaking, all property (therefore most Assets) are a question of rights. No-one actually <a href="#{FDD94D9F-F343-4c1b-9688-752C896A3C7C}"><font color="#0000ff"><u>owns</u></font></a> something, they have a legal right of that thing. In most cases, we can deal with this just using Asset. However in more complex cases, rights can be bought and sold (and of course owned) to things which aren't generally viewed as assets - e.g. paying a delivery cost, owning the leasehold to a property, etc. 

Examples:

* The performance rights to a Song
* The rights to purchase currency at a pre-agreed rate in the future

### <a id="{04A80EF0-8E34-4bdb-8A8E-31D89028F9B6}"></a>rightsTo
A Relationship between <a href="#{487778E0-4BD7-4d9a-B7F7-63731478E1A2}"><font color="#0000ff"><u>Rights</u></font></a> and the <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> to which the Rights apply 

Example:

* Rights to travel on a particular service (a travel reservation)
* Rights to a parcel of land

### <a id="{830B2164-E880-4bef-A62C-B38CEB6A824D}"></a>RoadVehicle
A <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> that travels by road (surprisingly enough)

### <a id="{0066A327-D497-42e0-9F50-D988F522F4A5}"></a>Role
An <a href="#{0358DDAB-D22C-4ee5-8F9A-CF18F3E432BD}"><font color="#0000ff"><u>ClassOfState</u></font></a> that is the role an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> has in context (as part of) an Element

- e.g. Manager, 

### <a id="{0B2564A8-9A95-4164-BB49-01900DD530AD}"></a>RoomNumber
A GeoIdentity used to identify a PartOfFacility

### <a id="{803AF0E7-01EC-4123-B888-3FB6369C840F}"></a>Sailing
A <a href="#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74}"><font color="#0000ff"><u>TravelService</u></font></a> by sea

### <a id="{3634DBF3-AA3A-402e-9D08-906C06FAFEDB}"></a>SatellitePhoneHandset
A CommunicationsDevice that communicates via satellite. 

### <a id="{6BC73189-2B25-4e1c-A935-EDA8106F3EB3}"></a>scheduledArrivalPort
The <a href="#{57860A04-0128-4c7e-9BFD-83D3BA432F8C}"><font color="#0000ff"><u>Port</u></font></a> from which the <a href="#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74}"><font color="#0000ff"><u>TravelService</u></font></a> is scheduled to arrive

### <a id="{DB3878D9-FF24-4069-A8DD-C24F5D074C0C}"></a>scheduledArrivalTime
The date/time on which the service was scheduled to arrive

The <a href="#{EF2C13D4-7106-4799-BB72-7CD47714F257}"><font color="#0000ff"><u>format</u></font></a> of this <a href="#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA}"><font color="#0000ff"><u>attribute</u></font></a> is a restricted string based upon the ISO 8601 Extended Format.

### <a id="{1312D263-F609-4df3-A1DB-AA0557B3B94B}"></a>scheduledDeparturePort
The <a href="#{57860A04-0128-4c7e-9BFD-83D3BA432F8C}"><font color="#0000ff"><u>Port</u></font></a> from which the <a href="#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74}"><font color="#0000ff"><u>TravelService</u></font></a> is scheduled to depart

### <a id="{340CF0CC-BA75-40b7-8B8A-167CD65C1830}"></a>scheduledDepartureTime
The date/time on which the service was scheduled to depart

The <a href="#{EF2C13D4-7106-4799-BB72-7CD47714F257}"><font color="#0000ff"><u>format</u></font></a> of this <a href="#{4A8E5877-32DF-428f-9A60-6AC3D083FFCA}"><font color="#0000ff"><u>attribute</u></font></a> is a restricted string based upon the ISO 8601 Extended Format.

### <a id="{D3375BB5-6773-40e1-8CA2-B393DD02B98C}"></a>SchemaObject
A DataObject that is a standardised plan or outline for something.

e.g. Bristol City Street Furniture Schema

### <a id="{C2C5FF87-189C-478a-B3BF-4706D798087F}"></a>schemeMasteredIn
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a <a href="#{222534A5-25C8-4ecd-BE55-27DA1534D402}"><font color="#0000ff"><u>NamingScheme</u></font></a> is owned by a <a href="#{F682A265-1AFE-4287-A9CD-0D4C83F54C52}"><font color="#0000ff"><u>System</u></font></a> that is the master for its names / identifiers - i.e. the uniqueness of the name/identifier is limited to the system.

### <a id="{8D42B4A8-30D3-459d-A729-F5C8FE16D418}"></a>schemeOwner
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts a RepresentationScheme is governed and used by a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> 

### <a id="{8C1321B7-8686-4a21-B99A-6C4A98B411A7}"></a>ScreenName
A display Name used by the account which may be non-unique, and may not be the same as the username

### <a id="{03D1711E-F9A7-41b1-B82F-B442FDF82EBF}"></a>SeatNumber
The number of the seat that the Passenger should be travelling in. Whilst this partially identifies the Passenger, there is no guarantee that people have not swapped seats. 

### <a id="{CED628E4-8641-486b-BCD7-CB4E147E7AE6}"></a>SecurityLabel
A SecurityLabel may be assigned at the statement (triple) level or to the entire ExchangePayload. They provide a mechanism to specify access restrictions and handling instructions for specific triples.

Note: In any given IES exchange, a <a href="#{CED628E4-8641-486b-BCD7-CB4E147E7AE6}"><font color="#0000ff"><u>SecurityLabel</u></font></a> must be applied to the ExchangePayload. Individual SecurityLabels at the statement level are used to indicate where individual statements deviate from the overall payload SecurityLabel

### <a id="{44C93DB5-8DFA-4585-9060-EEC789E0A5AC}"></a>Sender
An <a href="#{A5713B2C-E098-4dd2-BD46-42DA51899FEA}"><font color="#0000ff"><u>PartyInCommunication</u></font></a> where the communicating party is the sender of a message

### <a id="{F7172876-85F6-4d29-B11F-A1B36616416A}"></a>SendingAccount
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{44DAC574-2A2E-44bc-ACD2-236811FA8D29}"><font color="#0000ff"><u>FinancialAccount</u></font></a> sends money

### <a id="{51F79BC9-9BB5-47d6-973B-6F86F289B5FB}"></a>SerialNumber
An Identifier for Device that has been assigned at manufacture.

Example Value:

123ABC456DEF

### <a id="{8F8428BA-8586-4e34-9C75-FBA7A647B8EA}"></a>ServiceName
The Name of the OnlineService

This should not be confused with a webpage (see the <a href="#{79098C74-E063-4c45-886D-D0B88A48E954}"><font color="#0000ff"><u>Webpage</u></font></a> entity type). The Online Service may be provided via a webpage.

### <a id="{496683C9-EB89-46ac-87D0-4864F1B54ED4}"></a>ServiceProvider
The role of an <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> in providing a Service (e.g. a TeleConference)

### <a id="{CB4023BB-4B36-43a3-BCED-A7715FD597B0}"></a>ServiceUser
A temporal state of a ResponsibleActor

Note:  this is the superclass of <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (the whole life person or organisation) because the whole-life state is just a special case of a ResponsibleActorState. This pattern is true for all states. 

### <a id="{14098560-1FF3-4599-B9A5-41167861538B}"></a>Ship
A <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> that travels on water

### <a id="{A0D40C4F-B513-4c9f-8D4A-79D0FA7CEF50}"></a>siblingOf
A Relationship between two <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> Entities that indicates one is the sibling of the other

### <a id="{C55A12C9-CF85-4b7c-B422-1D41054E9570}"></a>Signatory
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> ratifies an agreement

### <a id="{3244F6B1-8636-4895-B3B1-283CF057F826}"></a>SIMCard
A CommunicationsDevice that holds data about a IMSI

### <a id="{A4B13044-00FD-4868-8147-1A3C9E84DAAB}"></a>SimilarEntities
An <a href="#{D1B2FB30-36CA-4012-B85F-514E270BF541}"><font color="#0000ff"><u>ClassOfEntity</u></font></a> whose instances are considered similar

### <a id="{333E73AD-563F-443c-A9B3-CA122FDF75B9}"></a>similarEntity
An <a href="#{BBC06281-340F-458f-A057-82193F32C9DD}"><font color="#0000ff"><u>rdf:type</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> that asserts an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is similar to other Entities that are also related to the same <a href="$element://{A4B13044-00FD-4868-8147-1A3C9E84DAAB}"><font color="#0000ff"><u>SimilarEntities</u></font></a> class.

### <a id="{4C19E163-710B-4ccb-9F1C-569F8E348BDC}"></a>SMS
A Message (text and images) sent over a cellular network

### <a id="{1D9F0978-EFD2-4e27-9242-219637C574EF}"></a>socialisesAt
A <a href="#{92FC2C35-D40B-4393-BA0B-88849743FEB6}"><font color="#0000ff"><u>visits</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and a <a href="$element://{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> they socialise in.

Note: more often than not, this will be a statement of occasional socialising, so the instance of the <a href="$element://{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> should also be an instance of DiscontinuousState. In rarer occasions, it may be used to highlight a single, continuous visit, but in that case, <a href="$element://{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> would generally be used.

### <a id="{439817EA-5973-45ab-9C01-9D75ED7D88B8}"></a>Socialising
A temporal state of a ResponsibleActor

Note:  this is the superclass of <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (the whole life person or organisation) because the whole-life state is just a special case of a ResponsibleActorState. This pattern is true for all states. 

### <a id="{3DC012C3-E273-4ec2-A462-CEDEB27262C1}"></a>SocialMediaPage
An OnlineArtefact that is user-created - e.g. a facebook timeline, twitter feed, etc. 

### <a id="{4B3AE19C-6369-49d0-B7B5-949714FFFC95}"></a>SocialMediaPost
An OnlineArtefact that is part of a SocialMediaPage

Note: the content may be created by a different account to the one which created the <a href="#{3DC012C3-E273-4ec2-A462-CEDEB27262C1}"><font color="#0000ff"><u>SocialMediaPage</u></font></a>

### <a id="{DF17458A-3BB8-4851-B88A-1E08C2EFA697}"></a>SocialServicesIdentifier
An NationalIdentityNumber used for managing a citizen's access to social services

In UK, this would be an NI number, in the US, it would be the social security number

### <a id="{B6014BB6-FD82-4748-8DFF-65401770515C}"></a>Software
A <a href="#{F999F59A-7C7B-40f3-8F86-5B2592889E95}"><font color="#0000ff"><u>ClassOfAsset</u></font></a> that is programmatic instructions that control or affect the behaviour of an <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a> (usually a Device). 

Note that <a href="#{B6014BB6-FD82-4748-8DFF-65401770515C}"><font color="#0000ff"><u>Software</u></font></a> is a class, as the same Software may be installed in multiple locations.

### <a id="{FA149043-EA61-4497-A036-589DA1FD312E}"></a>spokenLanguage
The language in which someone is proficient

### <a id="{9B232210-27A3-410a-A713-EFDE7922C61C}"></a>Stalking
A CriminalActivity involving the malicious surveillance of a person, often in threatening manner

### <a id="{C441DE5B-739A-4a83-BE87-96BC63A530B3}"></a>StandardMeasure
A Measure specified in the International system of quantities

### <a id="{773272F0-DBAB-4c47-8E21-01171FC82245}"></a>StandardMeasureValue
A MeasureValue that is expressed in SI units

### <a id="{861E3D08-3659-489a-B100-0E943CF3F3F0}"></a>startsIn
An xsd:DateTime for the start of the period

### <a id="{47301D66-CBD5-4d10-9481-B66966A3F3A2}"></a>State
A temporal state of an Element

Note: IES requires that any <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> must be related to its whole-life Element. In some cases, the identity of the whole-life element may be unknown (or of unknown type) but a whole-life element must still be created and related to the State.

Note: When Events are decomposed into temporal parts, those parts are often Events themselves. The exception is when the temporal part is arbitrary (e.g. the 11th second of a meeting) when a State should be used. These are rare though.

### <a id="{7EC7FCEE-7C60-4233-8938-D6320BD951F2}"></a>statementLabel
A link from an <a href="#{23C7BEF3-23D3-4d16-9401-16E537BE9B35}"><font color="#0000ff"><u>rdf:Statement</u></font></a> (see W3C guidance on RDF reification) to the <a href="#{CED628E4-8641-486b-BCD7-CB4E147E7AE6}"><font color="#0000ff"><u>SecurityLabel</u></font></a> that provides the access control for that statement.

Note: All exchanges should have a default <a href="#{259167E4-D0B3-4f03-9653-CAD778F5F6F3}"><font color="#0000ff"><u>payloadLabel</u></font></a> specified. The use of <a href="$element://{7EC7FCEE-7C60-4233-8938-D6320BD951F2}"><font color="#0000ff"><u>statementLabel</u></font></a> is required when individual statements deviate from the default in terms of their access control.

### <a id="{90332C00-0188-4773-8A71-F9ED15F5ED33}"></a>staysAt
A <a href="#{92FC2C35-D40B-4393-BA0B-88849743FEB6}"><font color="#0000ff"><u>visits</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and a <a href="$element://{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> where the person stays at the Location. This should not be confused with residesIn which is an assertion of legal residence. 
Note: more often than not, this will be a statement of regular/occasional stays, so the instance of the <a href="$element://{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> should also be an instance of DiscontinuousState. In rarer occasions, it may be used to highlight a single, continuous visit, but in that case, <a href="$element://{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> would generally be used.

### <a id="{686293F8-123B-478f-9A67-A6074937B528}"></a>StoreCard
A PaymentArtefact issued by a retail Organisation that can only be used to pay for items supplied by that Organisation. 

### <a id="{2E33B6DC-54D5-4e5e-9894-B2801F174B00}"></a>storedIn
A Relationship between an <a href="#{CA196722-9531-4eb4-A8CF-B9A5145CDCFD}"><font color="#0000ff"><u>AssetState</u></font></a> and a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> where the <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a> is/was stored

### <a id="{49B3D340-AADC-4fcd-80CC-283AE0FC85DF}"></a>strengthOfInterest
StrengthOfInterest is used in its most general sense and is limited to the following values:
� Weak
� Strong
� Fanatical

### <a id="{BFFBC847-AD87-458e-9A86-690D659EB48F}"></a>SubjectOfInterest
A <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> during which an <a href="#{97EDC90F-3B36-4da8-AE77-D5FDBDEA2B21}"><font color="#0000ff"><u>Element</u></font></a> is of interest to an investigation

### <a id="{11F2A275-650F-407d-8E86-F99DDEF4AAAF}"></a>SubjectOfOperation
An EventParticipant where an <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> is the subject of an OperationalEvent

Examples:

* person / organisation under investigation
* recon'd location
* subject of surveillance

### <a id="{BEC84E4F-F407-4a20-BC68-AD1723A3F860}"></a>successorTo
An <a href="#{FA4DDF04-16DA-4b5c-AE9A-6AB8CD07DCDB}"><font color="#0000ff"><u>after</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking two Elements where one ends and the other comes after as a replacement

### <a id="{78D65599-BCBB-491a-8C34-75B9F7AB60D5}"></a>Summit
A PoliticalEvent where senior leaders assemble to discuss and agree policy or treaties

### <a id="{E4D44720-DBEE-434e-A61E-35FE8B66A4BE}"></a>Supplier
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> participates in a <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> as a supplier

### <a id="{4F013D3F-E237-489a-96D5-5E9E54C6A388}"></a>supplierTo
A <a href="#{181AAC84-26CE-4531-AC32-A73B8FD8B858}"><font color="#0000ff"><u>worksFor</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> where the supplier (domain) is contracted to deliver goods or services to client (range)

### <a id="{B5A0C08A-39B3-4bd1-9D19-CE87E0F7DEBB}"></a>Surname
A PersonName that is their inherited or married name

Note:
A surname will often be applied to a <a href="#{47301D66-CBD5-4d10-9481-B66966A3F3A2}"><font color="#0000ff"><u>State</u></font></a> of the Person, as names tend to change over time

### <a id="{AD0F575E-5C28-4594-B346-50E9F22C2A8E}"></a>Surveillance
An IntelligenceOperation that involves the continued observation of a Person or Location

### <a id="{A86EC717-55AF-456c-BEC4-E1BA295D0227}"></a>SurveillanceWarrant
Relates a <a href="#{AD0F575E-5C28-4594-B346-50E9F22C2A8E}"><font color="#0000ff"><u>Surveillance</u></font></a> <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> to a Document that is the warrant for the Surveillance

### <a id="{F682A265-1AFE-4287-A9CD-0D4C83F54C52}"></a>System
An <a href="#{115F2F9B-21F3-4903-8EAA-AB3AEFE97461}"><font color="#0000ff"><u>Device</u></font></a>  comprising software and hardware brought together for a purpose. The Devices may or may not be removable / replaceable

### <a id="{056DDAD3-9315-48a8-8598-3DD4F783C5CF}"></a>SystemState
A temporal state of a <a href="#{F682A265-1AFE-4287-A9CD-0D4C83F54C52}"><font color="#0000ff"><u>System</u></font></a>

### <a id="{5D13DE13-CAAC-4879-9237-D20A6846F4D8}"></a>takesplaceIn
An <a href="#{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to indicate an EventParticipant takes place within a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a>

### <a id="{9BEF1C80-3823-4611-9349-AA1E11E41BE7}"></a>TargetLocation
Relates an <a href="#{8787BE51-8FE0-4d76-97B4-608311434F5B}"><font color="#0000ff"><u>MilitaryAttack</u></font></a> to the location specified for the attack

### <a id="{7B20EC37-6D66-4cd9-97DF-2A30B324C421}"></a>Team
An <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> formed around a particular pursuit or task

### <a id="{6EAC8930-3D16-4e44-9706-989BDF6564A5}"></a>TeleConference
An InteractiveCommunication where 2 or more parties communicate using audio

### <a id="{593AE684-C2E9-4e40-A7FD-549BFA64900D}"></a>TelephoneAccount
A <a href="#{8300451C-1DF9-4545-9174-D8AA69C58CCD}"><font color="#0000ff"><u>CommunicationsAccount</u></font></a> that is used to administer the use of one or more telephone numbers.

### <a id="{79C84EC1-83EC-45a8-A3CE-F88CFFBF9434}"></a>TelephoneCountryCode
The dialing code for a country as specified by the ITU

### <a id="{168D7B01-CD70-4f83-A414-19B6ABEB961C}"></a>TelephoneNumber
A CommunicationsIdentifier that enables calls to be directed to particular handset

### <a id="{007F88AD-9CDF-4aa1-BE73-18C688DA8C05}"></a>TelephoneNumberRange
A CommunicationsIdentifierRange of TelehoneNumbers

### <a id="{3FEB0BB0-F127-431a-B117-CC986B11D61A}"></a>Temperature
The Measure of the thermodynamic temperature of an Element

### <a id="{2B451601-EC1D-4bd4-A782-6E0B7E0D416D}"></a>Tendency
A DispositionalClass where all the instances share the same tendency

Example: People who tend to violence

### <a id="{F8454637-80DD-44a7-AD91-6DECE44F0171}"></a>TerrorAttack
A CriminalActivity that is politically motivated and designed to cause terror

### <a id="{6467A4EF-46BA-401c-A5C7-668BAFB6E228}"></a>TerroristOrganisation
An <a href="#{F3DB6A59-B2DE-4743-A9A8-7DA9CCC68638}"><font color="#0000ff"><u>OrganisationState</u></font></a> that is assessed to be conducting acts of terror to achieve a political or religious goal.


### <a id="{5CD50268-582A-426b-B4CC-F6EE308B84A3}"></a>TheatreTicket
An EntertainmentTicket for a theatre show

### <a id="{0BC61540-2AFB-42e6-A845-79771EE0268D}"></a>Ticket
Documented authority (paid-for or otherwise) entitling the bearer to some specified activity.

### <a id="{A4906B5E-8718-404e-8EEF-20AE29106383}"></a>ticketArrivalLocation
The arrival location as stated on the ticket.

### <a id="{952E5981-257F-429e-9F22-8D2E3B9282C7}"></a>ticketDepartureLocation
The departure location as stated on the ticket.

### <a id="{92470C59-DFA6-47f7-A525-50CDABC8F852}"></a>TicketUsedInCheckIn
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where a Ricket is used in a <a href="#{87308A03-5C79-4d94-99E1-660042AC7929}"><font color="#0000ff"><u>CheckIn</u></font></a> event

e.g. a London Underground ticket being used at a barrier, or a concert ticket being scanned on arrival at the venue

### <a id="{E7A659A5-9059-4ea5-8FAB-8A29AFC47D9A}"></a>TimeBoundedClass
A <a href="#{3C13E07D-5796-4d03-9EBC-C75277E87CA4}"><font color="#0000ff"><u>ClassOfElement</u></font></a> whose instances all begin and end within the bounds specified for the Class. In other words, a class that is defined by the temporal extent of its members. 

Note, if either the begin or end bound are missing, it is taken to be indeterminate. For example, if the begin bound is 1st Jan 2018, the class has instances that all started after that date, and their end is irrelevant. 

Example:
Everything that began and ended in the year 1900 - this would include all activities that took place within that year (but did not extend beyond it), everything created and destroyed within that time, and everything that was born and died during the period. 

### <a id="{30F5944F-75C3-4f12-A315-4E94ABCA809E}"></a>Title
The title of the respective document.

### <a id="{79D9049D-E63F-4c94-B348-49506A75B9F8}"></a>TOID
TOIDs (TOpographic IDentifiers) are unique and persistent identifiers created and managed by Ordnance Survey Great Britain to identify topographic objects in OS datasets. 

Example: the <a href="#{79D9049D-E63F-4c94-B348-49506A75B9F8}"><font color="#0000ff"><u>TOID</u></font></a> for the Tower of London is osgb1000006032892.

### <a id="{54A4E900-7E8E-49fd-91F4-23ADDDF2DA60}"></a>TradeAgreement
A PoliticalAgreement that sets tariffs and standards for trade between nations. 

### <a id="{57ADBC97-C089-4d1a-A334-A9C44EAEC38A}"></a>TradedAsset
An <a href="#{C5AB420C-1AB6-479a-97E1-4F2FD37725CB}"><font color="#0000ff"><u>EventParticipant</u></font></a> where an <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a> is participant in a TradeEvent

This could be a specific Asset (e.g. serial numbered item) being offered for sale (as opposed to a type of Asset) or an Asset being delivered, withdrawn from sale, etc.

### <a id="{A92F03F0-CB9E-4667-B985-25377303416A}"></a>tradedItemType
The type of entity involved in the TradeEvent

e.g. "Dyson Animal Mk3"

Note: there may be no more than one itemType for a given <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> - i.e. a new TradeEvent must be instantiated for each <a href="#{D1B2FB30-36CA-4012-B85F-514E270BF541}"><font color="#0000ff"><u>ClassOfEntity</u></font></a> sold, offered, delivered, etc.

Note: was "ItemType" in IES 3.2

### <a id="{CA86862B-DA7E-487c-907B-26FA5D0564CD}"></a>TradeEvent
An <a href="#{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> where something is offered, bought or exchanged

### <a id="{A8715447-3583-45d0-9550-625CF96B3E2E}"></a>TrainTicket
A <a href="#{0BC61540-2AFB-42e6-A845-79771EE0268D}"><font color="#0000ff"><u>Ticket</u></font></a> that is used to travel by rail

### <a id="{F2D6CFE4-BCE9-4bce-ADB0-075656038A55}"></a>TrainTravel
A <a href="#{3D0FC30A-CF82-44f2-970E-BFD04EADBA74}"><font color="#0000ff"><u>TravelService</u></font></a> by rail

### <a id="{9574377B-6752-4317-94DC-E075C408442D}"></a>transferType
An rdf:type relationship from a MoneyTransfer to a ClassOfMoneyTransfer

### <a id="{A9D01DAB-281E-48ae-BB33-8518701ABBDE}"></a>transferValue
A relationship from a MoneyTransfer to the AmountOfMoney transferred.

### <a id="{7693D2C9-0F06-4005-BB8D-B5B572B2281A}"></a>Transit
A <a href="#{95B5ACC4-956A-4b29-AB9E-BDCD12EF319F}"><font color="#0000ff"><u>Movement</u></font></a> that is an individual transportation - e.g. an individual flight, sailing, etc.

### <a id="{76DC9A0C-F6E8-4ff4-ADD6-072DC1EBE3AB}"></a>TravelBooking
The Purchase of planned travel arrangements.

3. Travel Bookings may include bookings for Flights, Ferry Crossings, Train Journeys (i.e Travel Services), and also Hotels, Hire Cars etc. when these have been modelled. These will be included on the booking as relationships to the appropriate other entities.

### <a id="{E1D8A09D-C260-4dd8-B6FF-C2FA8968A00B}"></a>TravelCard
A PaymentArtefact that permits travel on public transport

### <a id="{55384377-146A-47c9-8706-18A1343A219C}"></a>TravelLeg
An EventParticipant in which a <a href="#{F4EDE167-6F5A-417d-9984-0221CCDF752C}"><font color="#0000ff"><u>Entity</u></font></a> travels. That travel may be part of a Journey.

The <a href="#{55384377-146A-47c9-8706-18A1343A219C}"><font color="#0000ff"><u>TravelLeg</u></font></a> may be part of a <a href="#{8B571665-0AA1-40be-A7A0-A35BE86B7192}"><font color="#0000ff"><u>Journey</u></font></a> (i.e. the Journey has one of more legs).

### <a id="{8B290363-239E-415e-9F2D-8267D1BA2ECB}"></a>TravelReservation
A <a href="#{57ADBC97-C089-4d1a-A334-A9C44EAEC38A}"><font color="#0000ff"><u>TradedAsset</u></font></a> where the asset is a <a href="#{CDF94674-D458-4996-9A99-6CBFFF3907EB}"><font color="#0000ff"><u>Reservation</u></font></a>

### <a id="{3D0FC30A-CF82-44f2-970E-BFD04EADBA74}"></a>TravelService
A transportation service, often provided as a public service � e.g. a scheduled flight, rail journey, ferry crossing, etc.

### <a id="{680FD822-C1F6-4d09-94D5-5D586C947DE1}"></a>TravelServiceIdentifier
The Identifier for the respective Travel Service � this is how humans would usually refer to the service 

Note however that often this identifier does not, on its own, uniquely identify any given instance of a travel service � e.g. <a href="#{375B0887-712F-43f0-BBF4-5C544D75AC39}"><font color="#0000ff"><u>Flight</u></font></a> BA0010 is reused on a daily basis to refer to the flight between London Heathrow and Los Angeles. As such, to uniquely identify any given instance of a Travel Service you would need to combine it with other attributes � typically departure date/time.

For Flights, this will be the Flight Number.

For Ferry Sailings this is typically the name of the vessel that is scheduled to <a href="#{E0036B31-8D73-4268-8959-6E9A5EE55BB2}"><font color="#0000ff"><u>make</u></font></a> that sailing and, when combined with the departure date/time can be used to uniquely identify that sailing. Note that if the actual vessel that makes the sailing is different to that which was scheduled (e.g. as result of the scheduled vessel being out of commission), this identifier is not modified.

### <a id="{6C669BEF-9267-4612-9F29-B28918B203F5}"></a>TravelTicket
A Ticket that permits travel on a particular route or set of routes

### <a id="{C066EEB4-91AF-4ee6-BB02-44A49087946B}"></a>TravelVisa
An IdentityDocument, usually attached to a Passport, which allows a Person to remain in a Country for a set period of time. 

### <a id="{59599C4B-F3DE-49a0-B76F-BE4CB1293CBA}"></a>Treaty
An <a href="#{1B39630B-B00F-4def-9C65-48082C4AD2E0}"><font color="#0000ff"><u>EndToEndAgreement</u></font></a> that is between Nations and subject to international law

### <a id="{37CEEA2E-93E7-446d-A181-A55A091C3B22}"></a>trusts
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities where one <a href="#{37CEEA2E-93E7-446d-A181-A55A091C3B22}"><font color="#0000ff"><u>trusts</u></font></a> the other.

Note: this should not be considered a bi-directional relationship. Just because one person trusts another person does not necessarily mean the feeling is reciprocated. 

### <a id="{07BDCB73-1CDA-4057-9D7E-EC088D304B04}"></a>typeOfCriminality
A link to the <a href="#{69868D83-C3BD-4877-AB5C-374B4C6F4A7E}"><font color="#0000ff"><u>ClassOfCriminalActivity</u></font></a> conducted

### <a id="{AE6D5097-F555-48af-AFBA-88ECAA31BFF3}"></a>typicallyTargets
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> linking a <a href="#{64CE6FEA-7B05-4813-BD55-D56C02A54486}"><font color="#0000ff"><u>ClassOfOperation</u></font></a>alEvent to a <a href="#{69868D83-C3BD-4877-AB5C-374B4C6F4A7E}"><font color="#0000ff"><u>ClassOfCriminalActivity</u></font></a> where the operations are intended to counter or target certain criminal activities.

Example: counter-narcotics operations typically target drug dealing

### <a id="{AEA785BB-B625-41aa-8738-FB0F3726A281}"></a>UN_LOCODE
A GeoIdentity that is a United Nations Code for Trade and Transport Locations

### <a id="{9F2DE0F4-58B1-46b7-B25A-545D765381A8}"></a>UnitOfMeasure
A ClassOfMeasureValue that is used to quantify a Measure on a standard scale

### <a id="{E2D19BE1-B1BF-4e0b-8D44-AFFD739756BA}"></a>UpdateAccount
An AccountAdminEvent where an Account is modified

### <a id="{D700FE64-4100-4ade-93CE-6219A7BC0BCB}"></a>upperBound
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> a MeasureRange to the Measure that is its upper bound

### <a id="{D97141BD-F6CF-4b10-B4E5-B1ECF6DF5178}"></a>uriScheme
URI scheme is the top level of the uniform resource identifier (URI) naming structure. All URIs and absolute URI references are formed with a scheme name, followed by a colon character (":"), and the remainder of the URI called the <i>scheme-specific part</i>.

### <a id="{AAA8DE3D-31D8-4c1e-B114-72E8B37D6CAA}"></a>uriSchemeName
URI scheme is the top level of the uniform resource identifier (URI) naming structure. All URIs and absolute URI references are formed with a scheme name, followed by a colon character (":"), and the remainder of the URI called the scheme-specific part.

A list of official IANA-registered URI schemes can be found at:
http://en.wikipedia.org/wiki/URI_scheme#Official_IANAregistered_schemes

### <a id="{C23AB49C-0734-45b7-A383-8EEA305CDBE4}"></a>URL
An Identifier for a WebResource

### <a id="{9D703CE2-DED0-4aba-BE21-474781670297}"></a>Username
The Identity for an account registered with an internet-based service.

An email address can be used as an online identifier for a specific domain (like Facebook). Where this is the case it can be considered to be both an instance of an email address and an instance of a username for an online identity.

### <a id="{01984617-C96D-48b3-ACDE-25F525719AEF}"></a>userOf
A hasAccessTo relationship between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and an <a href="#{40231334-5ACC-4dd4-A8C1-05012E2170E0}"><font color="#0000ff"><u>Asset</u></font></a> they use.

Note: more often than not, this will be a statement of occasional use, so the instance of the <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> should also be an instance of DiscontinuousState. In rarer occasions, it may be used to highlight a single, continuous use, but generally this would be modelled with the appropriate type of <a href="$element://{B376370E-F5E8-4287-A3EC-AC35532919B1}"><font color="#0000ff"><u>Event</u></font></a> and EventParticipants

### <a id="{958E4D57-8A19-4855-B9B3-6BB2F93F77B7}"></a>usesServicesAt
A <a href="#{92FC2C35-D40B-4393-BA0B-88849743FEB6}"><font color="#0000ff"><u>visits</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and a <a href="$element://{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> where they use services - e.g. banking, shopping, etc..

Note: more often than not, this will be a statement of regular/occasional use, so the instance of the <a href="$element://{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> should also be an instance of DiscontinuousState. In rarer occasions, it may be used to highlight a single, continuous visit, but in that case, <a href="$element://{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> would generally be used.

### <a id="{FCE0D994-4838-48fa-A274-57DB092A2960}"></a>UsuallyParked
A temporal state of a <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> which is the fusion of all its <a href="#{B6A503E5-3FC4-4a45-8DC0-994EA31A895A}"><font color="#0000ff"><u>Parked</u></font></a> states

Examples:
* A car that is usually parked in Acacia Avenue
* A ship that regularly docks at Dover
* An aircraft that regularly resides in a private hangar

### <a id="{6DEB5776-59E6-4645-9566-65EC62A36330}"></a>vafNumber
The Visa Application Form (VAF) number.

### <a id="{6ACC2ACC-46F2-4a02-A3E7-D16BE8EB723B}"></a>validFromDate
The date that the respective <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a> or <a href="#{0BC61540-2AFB-42e6-A845-79771EE0268D}"><font color="#0000ff"><u>Ticket</u></font></a> is valid from.

### <a id="{680F737D-A8AB-4410-9F1D-FAD7BDC98447}"></a>validToDate
The date that the respective <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a> or <a href="#{0BC61540-2AFB-42e6-A845-79771EE0268D}"><font color="#0000ff"><u>Ticket</u></font></a> is valid to.

### <a id="{0C682BA6-23AB-459c-B8FF-A114AA27650B}"></a>ValueInAmperes
A StandardMeasureValue for ElectricCurrent in amperes

### <a id="{391F91E4-768F-406c-A344-CC3331ABE2AC}"></a>ValueInCandela
A StandardMeasureValue for LuminousIntensity in candela

### <a id="{32097C4D-A0FB-4024-BDB8-8E899DDCF217}"></a>ValueInKelvin
A StandardMeasureValue for Temperature in kelvin

### <a id="{E7A9BC2D-85E2-4999-90DC-B76C9CB57C42}"></a>ValueInKilograms
A StandardMeasureValue for Mass in kilograms

### <a id="{C8D4C3CB-16C2-44a7-B709-35CEBF219BF0}"></a>ValueInMetres
A StandardMeasureValue for Length in metres

### <a id="{943CA047-F259-4181-BF04-F6D54065AAD4}"></a>ValueInMoles
A StandardMeasureValue for AmountOfSubstance in moles

### <a id="{E485D394-B9D7-40b6-BD44-E5970B2118BD}"></a>ValueInSeconds
A StandardMeasureValue for Duration in seconds

### <a id="{3B916F09-F3F4-43e9-9C84-99009C685396}"></a>Vehicle
An Asset that is a means of transportation � e.g. car, aircraft, ship.

### <a id="{93A816A9-EB7B-4250-8A1A-8919488029A7}"></a>VehicleController
A <a href="#{9888A3F3-7E9B-4806-BD4E-2FC4D87A5902}"><font color="#0000ff"><u>PersonInTransit</u></font></a> where the <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> is in control of the Transit

e.g. driver of a car, pilot of plane, captain of a ship

### <a id="{AC9AB7B0-6C38-4b08-B2B9-CAA8486F0F4B}"></a>VehicleIdentificationNumber
VIN � <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> Identification Number.

For road vehicles this is often directly referred to as the VIN, but this can also be applied in a generic fashion to other vehicle types.

ISO 3833 for road vehicles (17-digits)

### <a id="{9D24B4BE-2AD4-42d6-A906-8F6EFDA23EC5}"></a>VehicleName
The Name of the respective <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> (if applicable) � often this only applies to ships/boats. 

Examples:

The Saucy Sue
The Bountiful Blumpkin

### <a id="{D3275233-7381-483e-B2D2-77F13D73A52E}"></a>VehicleState
A temporal state of a <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a>

### <a id="{2202F5B0-DF49-4db5-A8F9-31FC2CC89005}"></a>VehicleUsed
An EventParticipant in which a <a href="#{3B916F09-F3F4-43e9-9C84-99009C685396}"><font color="#0000ff"><u>Vehicle</u></font></a> is used to transport Entities

### <a id="{3345AECA-925E-4bfc-820E-2294D5921E71}"></a>venueStatedOnTicket
The venue of the event the <a href="#{0BC61540-2AFB-42e6-A845-79771EE0268D}"><font color="#0000ff"><u>Ticket</u></font></a> is for.

Note: venues change, and the actual event may not run at the stated venue. 

### <a id="{E4C44F5B-5D57-4283-B985-5A2DA87BF212}"></a>VersionNumber
The number or code that identifies a VersionOfDocument.

### <a id="{C01F47A2-F545-4fac-A707-469AD32FBF94}"></a>versionOf
A relationship between a VersionOfDocument and the WorkOfDocumentation it is a version of.

### <a id="{ADB16761-4981-4476-BC53-2843587D1C02}"></a>VersionOfDocument
A <a href="#{F0B48978-D4E4-45a4-8238-091A5B714D82}"><font color="#0000ff"><u>WorkOfDocumentation</u></font></a> and a <a href="#{E7A659A5-9059-4ea5-8FAB-8A29AFC47D9A}"><font color="#0000ff"><u>TimeBoundedClass</u></font></a> that is a versionOf a WorkOfDocumentation

### <a id="{3B47FCD0-E7D1-4b2b-BC07-C96D3F07ABC3}"></a>Victim
An EventParticipant where a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> is the victim of a <a href="#{43E58528-16E4-48b3-8F13-10500879EA83}"><font color="#0000ff"><u>CriminalActivity</u></font></a>

### <a id="{1ED09A3D-7EE9-4b7a-8F0B-8590023C9F81}"></a>VideoConference
A <a href="#{6EAC8930-3D16-4e44-9706-989BDF6564A5}"><font color="#0000ff"><u>TeleConference</u></font></a> where parties communicate over video (with audio)

### <a id="{2ED602C6-C93C-41f3-8A02-10F0CAD0D64A}"></a>visaType
The type of the TravelVisa

Examples:

B1/B2
VISA TIER 4

### <a id="{EB558A61-8725-40d0-B87D-D6AA1FC27C89}"></a>Visiting
A temporal state of a ResponsibleActor

Note:  this is the superclass of <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (the whole life person or organisation) because the whole-life state is just a special case of a ResponsibleActorState. This pattern is true for all states. 

### <a id="{92FC2C35-D40B-4393-BA0B-88849743FEB6}"></a>visits
A Relationship and in <a href="#{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and a <a href="#{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> they visit.

Note: more often than not, this will be a statement of occasional visiting, so the instance of the <a href="$element://{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> should also be an instance of DiscontinuousState. In rarer occasions, it may be used to highlight a single, continuous visit, but in that case, inLocation would generally be used.

### <a id="{F186E39F-A251-4b84-85E9-577C7290F6D9}"></a>VoiceCall
An InteractiveCommunication by voice

### <a id="{2DB8231F-0673-4788-AE41-3F52A3702A2B}"></a>VoipAccount
A <a href="#{593AE684-C2E9-4e40-A7FD-549BFA64900D}"><font color="#0000ff"><u>TelephoneAccount</u></font></a> where the voice communication is over IP. This may also include video communication, screen sharing, etc. 

### <a id="{B94FF143-3681-41eb-8264-D3E85C558EFC}"></a>VotingAttendee
When a <a href="#{D62DDBB8-53FC-405a-BC43-89CA337563A0}"><font color="#0000ff"><u>Government</u></font></a> has voting rights at a <a href="#{78D65599-BCBB-491a-8C34-75B9F7AB60D5}"><font color="#0000ff"><u>Summit</u></font></a>

### <a id="{D4F568F5-7BC4-489d-94BC-AE1305E5C0C2}"></a>War
A <a href="#{E73C74A9-B356-40a4-BDBB-40567592BBD0}"><font color="#0000ff"><u>Disagreement</u></font></a> where at least one party has declared war

### <a id="{4CAD884A-1EA7-473d-9881-8B76EBF8526F}"></a>Warrant
An <a href="#{8177A2FB-CA54-4dc5-9884-33FBA660B174}"><font color="#0000ff"><u>AuthorisationDocument</u></font></a> that provides legal permission, usually for something that would be considered illegal or intrusive otherwise

### <a id="{CA2023C6-1677-4d24-A1E6-22BC4D595E6F}"></a>Warrantry
An EndToEndAuthorisation where the process involves legal warrants. 

### <a id="{7A58C9AD-C198-4a61-8244-DE5BBC591416}"></a>wasAuthorisedBy
A <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> to the <a href="#{1ECB4C6E-6A30-4dc5-A4AC-9A9DF5B6A54F}"><font color="#0000ff"><u>Organisation</u></font></a> that was the authorising agency for the <a href="#{BDF4EBD9-7F41-4d90-91A7-571177330C1B}"><font color="#0000ff"><u>IdentityDocument</u></font></a>

### <a id="{B513F0D8-E527-4548-8453-D905775E3A4F}"></a>WeaponLocation
Relates an <a href="#{8787BE51-8FE0-4d76-97B4-608311434F5B}"><font color="#0000ff"><u>MilitaryAttack</u></font></a> to the location of the attacking weapon system

### <a id="{79098C74-E063-4c45-886D-D0B88A48E954}"></a>Webpage
An OnlineArtefact that is a page on the web.

### <a id="{46D508B4-F1CC-45d7-9E4B-BA8A3C88D82A}"></a>WebResource
Any http presence on the web

### <a id="{3BE61CCF-DCD0-411d-9D43-5DEABF8381F2}"></a>WebResourceState
A temporal state of an <a href="#{46D508B4-F1CC-45d7-9E4B-BA8A3C88D82A}"><font color="#0000ff"><u>WebResource</u></font></a>

### <a id="{B2262900-BF01-4691-8DE1-46A726A6D1CB}"></a>What3words
A GeoIdentity that is a what3words Location specifier

(see what3words.com)

### <a id="{9FC35E2C-3D28-4f21-8FF7-3BAA51860958}"></a>WinningCandidate
The <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a> who won the <a href="#{7D9E328D-345E-43f5-8163-9657E4D016BD}"><font color="#0000ff"><u>Election</u></font></a>

### <a id="{9416F72A-9BF9-4c99-839C-76905F02B63B}"></a>WithdrawFromSale
A <a href="#{CA86862B-DA7E-487c-907B-26FA5D0564CD}"><font color="#0000ff"><u>TradeEvent</u></font></a> where a type of entity is withdrawn from sale

### <a id="{9C9ED058-4BB5-43d0-A311-FF7A532ED6D6}"></a>Witness
A <a href="#{5D5C5B9B-5E90-4100-8353-8EE9F3D772E2}"><font color="#0000ff"><u>Person</u></font></a>'s role as a witness in a trial

### <a id="{F0B48978-D4E4-45a4-8238-091A5B714D82}"></a>WorkOfDocumentation
A <a href="#{675A5C23-0746-43d0-96D0-AF0DF72CD697}"><font color="#0000ff"><u>Representation</u></font></a> that is the general case of a document - i.e. "War and Peace" as opposed to "My copy of <a href="#{D4F568F5-7BC4-489d-94BC-AE1305E5C0C2}"><font color="#0000ff"><u>War</u></font></a> and Peace"

### <a id="{55161540-8869-4af9-B159-51857E0B0BDB}"></a>worksAt
A <a href="#{92FC2C35-D40B-4393-BA0B-88849743FEB6}"><font color="#0000ff"><u>visits</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and a <a href="$element://{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> they work in.

Note: more often than not, this will be a statement of occasional presence, so the instance of the <a href="$element://{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> should also be an instance of DiscontinuousState. In rarer occasions, it may be used to highlight a single, continuous presence, but in that case, <a href="$element://{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> would generally be used.

### <a id="{181AAC84-26CE-4531-AC32-A73B8FD8B858}"></a>worksFor
A Relationship between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> (range - employer) and a <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> (domain- employed) that indicates one works for the other.

In the case where the work is occasional / ad-hoc (i.e. there isn't an ongoing work contract) then the instance of the ResponsibleActorState should also be an instance of <a href="#{52DB371E-71AC-4812-B3CF-0FD7D73F1BB0}"><font color="#0000ff"><u>DiscontinuousState</u></font></a>

### <a id="{25DD07E3-2500-4b9b-AF50-446EEC927AD2}"></a>worksWith
A Relationship between two <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> Entities that indicates one works with the other.

In the case where the work is occasional / ad-hoc (i.e. there isn't an ongoing job) then the instance of the <a href="#{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> should also be an instance of DiscontinuousState

Note: this <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> should only be used when it is not known who the two people work for (in which case create an organisation and used employedBy) or when the working relationship is rather loose - e.g. in cases of criminal cooperation.

### <a id="{475617C7-BEE3-4c5e-8749-9386B68A8DA5}"></a>worshipsAt
A <a href="#{92FC2C35-D40B-4393-BA0B-88849743FEB6}"><font color="#0000ff"><u>visits</u></font></a> <a href="#{DCE662F5-7BDB-457e-AE7E-2E5FE43DBA1A}"><font color="#0000ff"><u>relationship</u></font></a> between a <a href="#{D09EDE21-E862-4ec1-BC0F-045CCE5454A9}"><font color="#0000ff"><u>ResponsibleActor</u></font></a> and a <a href="$element://{E1A494ED-D493-44ab-8BF9-ABC6889D4D9A}"><font color="#0000ff"><u>Location</u></font></a> where they undertake religious worship

Note: more often than not, this will be a statement of regular/occasional worship, so the instance of the <a href="$element://{100B93CD-937E-4fdd-8851-02D1DC07F5B6}"><font color="#0000ff"><u>ResponsibleActorState</u></font></a> should also be an instance of DiscontinuousState. In rarer occasions, it may be used to highlight a single, continuous visit, but in that case, <a href="$element://{463F9B14-2D14-4364-B4F0-658A20DFCBFA}"><font color="#0000ff"><u>inLocation</u></font></a> would generally be used.

### <a id="{23C7BEF3-23D3-4d16-9401-16E537BE9B35}"></a>rdf:Statement


### <a id="{BBC06281-340F-458f-A057-82193F32C9DD}"></a>rdf:type


### <a id="{58C6DE35-5E57-4009-A6CE-69C889B31D82}"></a>rdfs:Class


### <a id="{1EC962A4-1138-4c75-B4D0-F38500AD80A2}"></a>rdfs:Resource


### <a id="{AFCFCF17-78EC-4f6c-B62A-C6B3467D880B}"></a>rdfs:subClassOf


### <a id="{57843280-4451-47eb-9616-B0843FE4E2C5}"></a>xsd:dateTime


### <a id="{C3FB8FEF-C23B-4d49-A902-31CAA27CA566}"></a>xsd:float


