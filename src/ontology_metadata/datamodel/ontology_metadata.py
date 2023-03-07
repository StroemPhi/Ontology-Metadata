# Auto generated from ontology_metadata.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-07T14:23:36
# Schema: Ontology-Metadata-TIB
#
# id: http://terminology.tib.eu/schema
# description: The metadata schema of the TIB Terminology Service that formalizes which metadata annotations are
#              required, recommended and optional for an OWL ontology or SKOS vocabulary that is supposed to be
#              index in the TIB TS.
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = "0.0.1"

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
MOD = CurieNamespace('MOD', 'http://purl.obolibrary.org/obo/MOD_')
NCBITAXON = CurieNamespace('NCBITaxon', 'http://purl.obolibrary.org/obo/NCBITaxon_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
OBI = CurieNamespace('OBI', 'http://purl.obolibrary.org/obo/OBI_')
ADMS = CurieNamespace('adms', 'http://www.w3.org/ns/adms#')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
BIOREGISTRY_SCHEMA = CurieNamespace('bioregistry_schema', 'https://bioregistry.io/schema/#')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERM = CurieNamespace('dcterm', 'http://example.org/UNKNOWN/dcterm/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DOAP = CurieNamespace('doap', 'http://example.org/UNKNOWN/doap/')
IDOT = CurieNamespace('idot', 'http://identifiers.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MOD = CurieNamespace('mod', 'http://purl.obolibrary.org/obo/MOD_')
OIO = CurieNamespace('oio', 'http://www.geneontology.org/formats/oboInOwl#')
ORCID = CurieNamespace('orcid', 'https://orcid.org/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PAV = CurieNamespace('pav', 'http://purl.org/pav/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov-o#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SDO = CurieNamespace('sdo', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
TIBTS = CurieNamespace('tibts', 'hhttp://terminology.tib.eu/schema')
VANN = CurieNamespace('vann', 'http://example.org/UNKNOWN/vann/')
DEFAULT_ = TIBTS


# Types

# Class references
class RequiredMetadataPurl(URIorCURIE):
    pass


class OntologyPurl(URIorCURIE):
    pass


class SkosConceptSchemePurl(URIorCURIE):
    pass


@dataclass
class RequiredMetadata(YAMLRoot):
    """
    A mixin that provides the required properties needed to index an ontology or SKOS vocabulary in the TIB
    Terminology Service.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIBTS.RequiredMetadata
    class_class_curie: ClassVar[str] = "tibts:RequiredMetadata"
    class_name: ClassVar[str] = "RequiredMetadata"
    class_model_uri: ClassVar[URIRef] = TIBTS.RequiredMetadata

    purl: Union[str, RequiredMetadataPurl] = None
    title: str = None
    preferredPrefix: str = None
    license: Union[str, URIorCURIE] = None
    creator: Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]] = None
    versionInfo: str = None
    versionNotes: str = None
    created: str = None
    modificationDate: Union[str, List[str]] = None
    description: str = None
    issueTracker: str = None
    documentation: str = None
    imports: str = None
    acronym: Optional[str] = None
    versionIRI: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.purl):
            self.MissingRequiredField("purl")
        if not isinstance(self.purl, RequiredMetadataPurl):
            self.purl = RequiredMetadataPurl(self.purl)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.preferredPrefix):
            self.MissingRequiredField("preferredPrefix")
        if not isinstance(self.preferredPrefix, str):
            self.preferredPrefix = str(self.preferredPrefix)

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, URIorCURIE):
            self.license = URIorCURIE(self.license)

        if self._is_empty(self.creator):
            self.MissingRequiredField("creator")
        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.creator]

        if self._is_empty(self.versionInfo):
            self.MissingRequiredField("versionInfo")
        if not isinstance(self.versionInfo, str):
            self.versionInfo = str(self.versionInfo)

        if self._is_empty(self.versionNotes):
            self.MissingRequiredField("versionNotes")
        if not isinstance(self.versionNotes, str):
            self.versionNotes = str(self.versionNotes)

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, str):
            self.created = str(self.created)

        if self._is_empty(self.modificationDate):
            self.MissingRequiredField("modificationDate")
        if not isinstance(self.modificationDate, list):
            self.modificationDate = [self.modificationDate] if self.modificationDate is not None else []
        self.modificationDate = [v if isinstance(v, str) else str(v) for v in self.modificationDate]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.issueTracker):
            self.MissingRequiredField("issueTracker")
        if not isinstance(self.issueTracker, str):
            self.issueTracker = str(self.issueTracker)

        if self._is_empty(self.documentation):
            self.MissingRequiredField("documentation")
        if not isinstance(self.documentation, str):
            self.documentation = str(self.documentation)

        if self._is_empty(self.imports):
            self.MissingRequiredField("imports")
        if not isinstance(self.imports, str):
            self.imports = str(self.imports)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.versionIRI is not None and not isinstance(self.versionIRI, str):
            self.versionIRI = str(self.versionIRI)

        super().__post_init__(**kwargs)


@dataclass
class RecommendedMetadata(YAMLRoot):
    """
    A mixin that provides the recommended properties needed to index an ontology or SKOS vocabulary in the TIB
    Terminology Service.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIBTS.RecommendedMetadata
    class_class_curie: ClassVar[str] = "tibts:RecommendedMetadata"
    class_name: ClassVar[str] = "RecommendedMetadata"
    class_model_uri: ClassVar[URIRef] = TIBTS.RecommendedMetadata

    contributor: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    contactInfo: Optional[str] = None
    fundingInfo: Optional[str] = None
    audience: Optional[str] = None
    domainCovered: Optional[str] = None
    languageCovered: Optional[str] = None
    languageExpressedIn: Optional[str] = None
    status: Optional[str] = None
    sourceRepository: Optional[str] = None
    distributions: Optional[str] = None
    applicationExample: Optional[str] = None
    references: Optional[str] = None
    citations: Optional[str] = None
    derivedFrom: Optional[Union[str, List[str]]] = empty_list()
    rootTerms: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.contributor]

        if self.contactInfo is not None and not isinstance(self.contactInfo, str):
            self.contactInfo = str(self.contactInfo)

        if self.fundingInfo is not None and not isinstance(self.fundingInfo, str):
            self.fundingInfo = str(self.fundingInfo)

        if self.audience is not None and not isinstance(self.audience, str):
            self.audience = str(self.audience)

        if self.domainCovered is not None and not isinstance(self.domainCovered, str):
            self.domainCovered = str(self.domainCovered)

        if self.languageCovered is not None and not isinstance(self.languageCovered, str):
            self.languageCovered = str(self.languageCovered)

        if self.languageExpressedIn is not None and not isinstance(self.languageExpressedIn, str):
            self.languageExpressedIn = str(self.languageExpressedIn)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.sourceRepository is not None and not isinstance(self.sourceRepository, str):
            self.sourceRepository = str(self.sourceRepository)

        if self.distributions is not None and not isinstance(self.distributions, str):
            self.distributions = str(self.distributions)

        if self.applicationExample is not None and not isinstance(self.applicationExample, str):
            self.applicationExample = str(self.applicationExample)

        if self.references is not None and not isinstance(self.references, str):
            self.references = str(self.references)

        if self.citations is not None and not isinstance(self.citations, str):
            self.citations = str(self.citations)

        if not isinstance(self.derivedFrom, list):
            self.derivedFrom = [self.derivedFrom] if self.derivedFrom is not None else []
        self.derivedFrom = [v if isinstance(v, str) else str(v) for v in self.derivedFrom]

        if self.rootTerms is not None and not isinstance(self.rootTerms, str):
            self.rootTerms = str(self.rootTerms)

        super().__post_init__(**kwargs)


@dataclass
class OptionalMetadata(YAMLRoot):
    """
    A mixin that provides the optional properties needed to index an ontology or SKOS vocabulary in the TIB
    Terminology Service.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = TIBTS.OptionalMetadata
    class_class_curie: ClassVar[str] = "tibts:OptionalMetadata"
    class_name: ClassVar[str] = "OptionalMetadata"
    class_model_uri: ClassVar[URIRef] = TIBTS.OptionalMetadata

    relatedVersions: Optional[str] = None
    socialMediaAccount: Optional[str] = None
    identifierPattern: Optional[str] = None
    format: Optional[str] = None
    homepage: Optional[str] = None
    publisher: Optional[str] = None
    comments: Optional[str] = None
    exampleIdentifier: Optional[str] = None
    exampleClass: Optional[str] = None
    mailingList: Optional[str] = None
    logo: Optional[str] = None
    otherIdentifier: Optional[str] = None
    developmentEnvironment: Optional[str] = None
    mappingRessources: Optional[str] = None
    competencyQuestions: Optional[str] = None
    appliedMethodology: Optional[str] = None
    alternativeTitle: Optional[str] = None
    alternativePrefix: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.relatedVersions is not None and not isinstance(self.relatedVersions, str):
            self.relatedVersions = str(self.relatedVersions)

        if self.socialMediaAccount is not None and not isinstance(self.socialMediaAccount, str):
            self.socialMediaAccount = str(self.socialMediaAccount)

        if self.identifierPattern is not None and not isinstance(self.identifierPattern, str):
            self.identifierPattern = str(self.identifierPattern)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.comments is not None and not isinstance(self.comments, str):
            self.comments = str(self.comments)

        if self.exampleIdentifier is not None and not isinstance(self.exampleIdentifier, str):
            self.exampleIdentifier = str(self.exampleIdentifier)

        if self.exampleClass is not None and not isinstance(self.exampleClass, str):
            self.exampleClass = str(self.exampleClass)

        if self.mailingList is not None and not isinstance(self.mailingList, str):
            self.mailingList = str(self.mailingList)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.otherIdentifier is not None and not isinstance(self.otherIdentifier, str):
            self.otherIdentifier = str(self.otherIdentifier)

        if self.developmentEnvironment is not None and not isinstance(self.developmentEnvironment, str):
            self.developmentEnvironment = str(self.developmentEnvironment)

        if self.mappingRessources is not None and not isinstance(self.mappingRessources, str):
            self.mappingRessources = str(self.mappingRessources)

        if self.competencyQuestions is not None and not isinstance(self.competencyQuestions, str):
            self.competencyQuestions = str(self.competencyQuestions)

        if self.appliedMethodology is not None and not isinstance(self.appliedMethodology, str):
            self.appliedMethodology = str(self.appliedMethodology)

        if self.alternativeTitle is not None and not isinstance(self.alternativeTitle, str):
            self.alternativeTitle = str(self.alternativeTitle)

        if self.alternativePrefix is not None and not isinstance(self.alternativePrefix, str):
            self.alternativePrefix = str(self.alternativePrefix)

        super().__post_init__(**kwargs)


@dataclass
class Ontology(YAMLRoot):
    """
    An OWL ontology.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = OWL.Ontology
    class_class_curie: ClassVar[str] = "owl:Ontology"
    class_name: ClassVar[str] = "Ontology"
    class_model_uri: ClassVar[URIRef] = TIBTS.Ontology

    purl: Union[str, OntologyPurl] = None
    title: str = None
    preferredPrefix: str = None
    license: Union[str, URIorCURIE] = None
    creator: Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]] = None
    versionInfo: str = None
    versionNotes: str = None
    created: str = None
    modificationDate: Union[str, List[str]] = None
    description: str = None
    issueTracker: str = None
    documentation: str = None
    imports: str = None
    acronym: Optional[str] = None
    versionIRI: Optional[str] = None
    contributor: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    contactInfo: Optional[str] = None
    fundingInfo: Optional[str] = None
    audience: Optional[str] = None
    domainCovered: Optional[str] = None
    languageCovered: Optional[str] = None
    languageExpressedIn: Optional[str] = None
    status: Optional[str] = None
    sourceRepository: Optional[str] = None
    distributions: Optional[str] = None
    applicationExample: Optional[str] = None
    references: Optional[str] = None
    citations: Optional[str] = None
    derivedFrom: Optional[Union[str, List[str]]] = empty_list()
    rootTerms: Optional[str] = None
    relatedVersions: Optional[str] = None
    socialMediaAccount: Optional[str] = None
    identifierPattern: Optional[str] = None
    format: Optional[str] = None
    homepage: Optional[str] = None
    publisher: Optional[str] = None
    comments: Optional[str] = None
    exampleIdentifier: Optional[str] = None
    exampleClass: Optional[str] = None
    mailingList: Optional[str] = None
    logo: Optional[str] = None
    otherIdentifier: Optional[str] = None
    developmentEnvironment: Optional[str] = None
    mappingRessources: Optional[str] = None
    competencyQuestions: Optional[str] = None
    appliedMethodology: Optional[str] = None
    alternativeTitle: Optional[str] = None
    alternativePrefix: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.purl):
            self.MissingRequiredField("purl")
        if not isinstance(self.purl, OntologyPurl):
            self.purl = OntologyPurl(self.purl)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.preferredPrefix):
            self.MissingRequiredField("preferredPrefix")
        if not isinstance(self.preferredPrefix, str):
            self.preferredPrefix = str(self.preferredPrefix)

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, URIorCURIE):
            self.license = URIorCURIE(self.license)

        if self._is_empty(self.creator):
            self.MissingRequiredField("creator")
        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.creator]

        if self._is_empty(self.versionInfo):
            self.MissingRequiredField("versionInfo")
        if not isinstance(self.versionInfo, str):
            self.versionInfo = str(self.versionInfo)

        if self._is_empty(self.versionNotes):
            self.MissingRequiredField("versionNotes")
        if not isinstance(self.versionNotes, str):
            self.versionNotes = str(self.versionNotes)

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, str):
            self.created = str(self.created)

        if self._is_empty(self.modificationDate):
            self.MissingRequiredField("modificationDate")
        if not isinstance(self.modificationDate, list):
            self.modificationDate = [self.modificationDate] if self.modificationDate is not None else []
        self.modificationDate = [v if isinstance(v, str) else str(v) for v in self.modificationDate]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.issueTracker):
            self.MissingRequiredField("issueTracker")
        if not isinstance(self.issueTracker, str):
            self.issueTracker = str(self.issueTracker)

        if self._is_empty(self.documentation):
            self.MissingRequiredField("documentation")
        if not isinstance(self.documentation, str):
            self.documentation = str(self.documentation)

        if self._is_empty(self.imports):
            self.MissingRequiredField("imports")
        if not isinstance(self.imports, str):
            self.imports = str(self.imports)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.versionIRI is not None and not isinstance(self.versionIRI, str):
            self.versionIRI = str(self.versionIRI)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.contributor]

        if self.contactInfo is not None and not isinstance(self.contactInfo, str):
            self.contactInfo = str(self.contactInfo)

        if self.fundingInfo is not None and not isinstance(self.fundingInfo, str):
            self.fundingInfo = str(self.fundingInfo)

        if self.audience is not None and not isinstance(self.audience, str):
            self.audience = str(self.audience)

        if self.domainCovered is not None and not isinstance(self.domainCovered, str):
            self.domainCovered = str(self.domainCovered)

        if self.languageCovered is not None and not isinstance(self.languageCovered, str):
            self.languageCovered = str(self.languageCovered)

        if self.languageExpressedIn is not None and not isinstance(self.languageExpressedIn, str):
            self.languageExpressedIn = str(self.languageExpressedIn)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.sourceRepository is not None and not isinstance(self.sourceRepository, str):
            self.sourceRepository = str(self.sourceRepository)

        if self.distributions is not None and not isinstance(self.distributions, str):
            self.distributions = str(self.distributions)

        if self.applicationExample is not None and not isinstance(self.applicationExample, str):
            self.applicationExample = str(self.applicationExample)

        if self.references is not None and not isinstance(self.references, str):
            self.references = str(self.references)

        if self.citations is not None and not isinstance(self.citations, str):
            self.citations = str(self.citations)

        if not isinstance(self.derivedFrom, list):
            self.derivedFrom = [self.derivedFrom] if self.derivedFrom is not None else []
        self.derivedFrom = [v if isinstance(v, str) else str(v) for v in self.derivedFrom]

        if self.rootTerms is not None and not isinstance(self.rootTerms, str):
            self.rootTerms = str(self.rootTerms)

        if self.relatedVersions is not None and not isinstance(self.relatedVersions, str):
            self.relatedVersions = str(self.relatedVersions)

        if self.socialMediaAccount is not None and not isinstance(self.socialMediaAccount, str):
            self.socialMediaAccount = str(self.socialMediaAccount)

        if self.identifierPattern is not None and not isinstance(self.identifierPattern, str):
            self.identifierPattern = str(self.identifierPattern)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.comments is not None and not isinstance(self.comments, str):
            self.comments = str(self.comments)

        if self.exampleIdentifier is not None and not isinstance(self.exampleIdentifier, str):
            self.exampleIdentifier = str(self.exampleIdentifier)

        if self.exampleClass is not None and not isinstance(self.exampleClass, str):
            self.exampleClass = str(self.exampleClass)

        if self.mailingList is not None and not isinstance(self.mailingList, str):
            self.mailingList = str(self.mailingList)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.otherIdentifier is not None and not isinstance(self.otherIdentifier, str):
            self.otherIdentifier = str(self.otherIdentifier)

        if self.developmentEnvironment is not None and not isinstance(self.developmentEnvironment, str):
            self.developmentEnvironment = str(self.developmentEnvironment)

        if self.mappingRessources is not None and not isinstance(self.mappingRessources, str):
            self.mappingRessources = str(self.mappingRessources)

        if self.competencyQuestions is not None and not isinstance(self.competencyQuestions, str):
            self.competencyQuestions = str(self.competencyQuestions)

        if self.appliedMethodology is not None and not isinstance(self.appliedMethodology, str):
            self.appliedMethodology = str(self.appliedMethodology)

        if self.alternativeTitle is not None and not isinstance(self.alternativeTitle, str):
            self.alternativeTitle = str(self.alternativeTitle)

        if self.alternativePrefix is not None and not isinstance(self.alternativePrefix, str):
            self.alternativePrefix = str(self.alternativePrefix)

        super().__post_init__(**kwargs)


@dataclass
class SkosConceptScheme(YAMLRoot):
    """
    A SKOS vocabulary serialized in RDF using the skos:ConceptScheme
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SKOS.ConceptScheme
    class_class_curie: ClassVar[str] = "skos:ConceptScheme"
    class_name: ClassVar[str] = "SkosConceptScheme"
    class_model_uri: ClassVar[URIRef] = TIBTS.SkosConceptScheme

    purl: Union[str, SkosConceptSchemePurl] = None
    title: str = None
    preferredPrefix: str = None
    license: Union[str, URIorCURIE] = None
    creator: Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]] = None
    versionInfo: str = None
    versionNotes: str = None
    created: str = None
    modificationDate: Union[str, List[str]] = None
    description: str = None
    issueTracker: str = None
    documentation: str = None
    imports: str = None
    acronym: Optional[str] = None
    versionIRI: Optional[str] = None
    contributor: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    contactInfo: Optional[str] = None
    fundingInfo: Optional[str] = None
    audience: Optional[str] = None
    domainCovered: Optional[str] = None
    languageCovered: Optional[str] = None
    languageExpressedIn: Optional[str] = None
    status: Optional[str] = None
    sourceRepository: Optional[str] = None
    distributions: Optional[str] = None
    applicationExample: Optional[str] = None
    references: Optional[str] = None
    citations: Optional[str] = None
    derivedFrom: Optional[Union[str, List[str]]] = empty_list()
    rootTerms: Optional[str] = None
    relatedVersions: Optional[str] = None
    socialMediaAccount: Optional[str] = None
    identifierPattern: Optional[str] = None
    format: Optional[str] = None
    homepage: Optional[str] = None
    publisher: Optional[str] = None
    comments: Optional[str] = None
    exampleIdentifier: Optional[str] = None
    exampleClass: Optional[str] = None
    mailingList: Optional[str] = None
    logo: Optional[str] = None
    otherIdentifier: Optional[str] = None
    developmentEnvironment: Optional[str] = None
    mappingRessources: Optional[str] = None
    competencyQuestions: Optional[str] = None
    appliedMethodology: Optional[str] = None
    alternativeTitle: Optional[str] = None
    alternativePrefix: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.purl):
            self.MissingRequiredField("purl")
        if not isinstance(self.purl, SkosConceptSchemePurl):
            self.purl = SkosConceptSchemePurl(self.purl)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.preferredPrefix):
            self.MissingRequiredField("preferredPrefix")
        if not isinstance(self.preferredPrefix, str):
            self.preferredPrefix = str(self.preferredPrefix)

        if self._is_empty(self.license):
            self.MissingRequiredField("license")
        if not isinstance(self.license, URIorCURIE):
            self.license = URIorCURIE(self.license)

        if self._is_empty(self.creator):
            self.MissingRequiredField("creator")
        if not isinstance(self.creator, list):
            self.creator = [self.creator] if self.creator is not None else []
        self.creator = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.creator]

        if self._is_empty(self.versionInfo):
            self.MissingRequiredField("versionInfo")
        if not isinstance(self.versionInfo, str):
            self.versionInfo = str(self.versionInfo)

        if self._is_empty(self.versionNotes):
            self.MissingRequiredField("versionNotes")
        if not isinstance(self.versionNotes, str):
            self.versionNotes = str(self.versionNotes)

        if self._is_empty(self.created):
            self.MissingRequiredField("created")
        if not isinstance(self.created, str):
            self.created = str(self.created)

        if self._is_empty(self.modificationDate):
            self.MissingRequiredField("modificationDate")
        if not isinstance(self.modificationDate, list):
            self.modificationDate = [self.modificationDate] if self.modificationDate is not None else []
        self.modificationDate = [v if isinstance(v, str) else str(v) for v in self.modificationDate]

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.issueTracker):
            self.MissingRequiredField("issueTracker")
        if not isinstance(self.issueTracker, str):
            self.issueTracker = str(self.issueTracker)

        if self._is_empty(self.documentation):
            self.MissingRequiredField("documentation")
        if not isinstance(self.documentation, str):
            self.documentation = str(self.documentation)

        if self._is_empty(self.imports):
            self.MissingRequiredField("imports")
        if not isinstance(self.imports, str):
            self.imports = str(self.imports)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.versionIRI is not None and not isinstance(self.versionIRI, str):
            self.versionIRI = str(self.versionIRI)

        if not isinstance(self.contributor, list):
            self.contributor = [self.contributor] if self.contributor is not None else []
        self.contributor = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.contributor]

        if self.contactInfo is not None and not isinstance(self.contactInfo, str):
            self.contactInfo = str(self.contactInfo)

        if self.fundingInfo is not None and not isinstance(self.fundingInfo, str):
            self.fundingInfo = str(self.fundingInfo)

        if self.audience is not None and not isinstance(self.audience, str):
            self.audience = str(self.audience)

        if self.domainCovered is not None and not isinstance(self.domainCovered, str):
            self.domainCovered = str(self.domainCovered)

        if self.languageCovered is not None and not isinstance(self.languageCovered, str):
            self.languageCovered = str(self.languageCovered)

        if self.languageExpressedIn is not None and not isinstance(self.languageExpressedIn, str):
            self.languageExpressedIn = str(self.languageExpressedIn)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.sourceRepository is not None and not isinstance(self.sourceRepository, str):
            self.sourceRepository = str(self.sourceRepository)

        if self.distributions is not None and not isinstance(self.distributions, str):
            self.distributions = str(self.distributions)

        if self.applicationExample is not None and not isinstance(self.applicationExample, str):
            self.applicationExample = str(self.applicationExample)

        if self.references is not None and not isinstance(self.references, str):
            self.references = str(self.references)

        if self.citations is not None and not isinstance(self.citations, str):
            self.citations = str(self.citations)

        if not isinstance(self.derivedFrom, list):
            self.derivedFrom = [self.derivedFrom] if self.derivedFrom is not None else []
        self.derivedFrom = [v if isinstance(v, str) else str(v) for v in self.derivedFrom]

        if self.rootTerms is not None and not isinstance(self.rootTerms, str):
            self.rootTerms = str(self.rootTerms)

        if self.relatedVersions is not None and not isinstance(self.relatedVersions, str):
            self.relatedVersions = str(self.relatedVersions)

        if self.socialMediaAccount is not None and not isinstance(self.socialMediaAccount, str):
            self.socialMediaAccount = str(self.socialMediaAccount)

        if self.identifierPattern is not None and not isinstance(self.identifierPattern, str):
            self.identifierPattern = str(self.identifierPattern)

        if self.format is not None and not isinstance(self.format, str):
            self.format = str(self.format)

        if self.homepage is not None and not isinstance(self.homepage, str):
            self.homepage = str(self.homepage)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.comments is not None and not isinstance(self.comments, str):
            self.comments = str(self.comments)

        if self.exampleIdentifier is not None and not isinstance(self.exampleIdentifier, str):
            self.exampleIdentifier = str(self.exampleIdentifier)

        if self.exampleClass is not None and not isinstance(self.exampleClass, str):
            self.exampleClass = str(self.exampleClass)

        if self.mailingList is not None and not isinstance(self.mailingList, str):
            self.mailingList = str(self.mailingList)

        if self.logo is not None and not isinstance(self.logo, str):
            self.logo = str(self.logo)

        if self.otherIdentifier is not None and not isinstance(self.otherIdentifier, str):
            self.otherIdentifier = str(self.otherIdentifier)

        if self.developmentEnvironment is not None and not isinstance(self.developmentEnvironment, str):
            self.developmentEnvironment = str(self.developmentEnvironment)

        if self.mappingRessources is not None and not isinstance(self.mappingRessources, str):
            self.mappingRessources = str(self.mappingRessources)

        if self.competencyQuestions is not None and not isinstance(self.competencyQuestions, str):
            self.competencyQuestions = str(self.competencyQuestions)

        if self.appliedMethodology is not None and not isinstance(self.appliedMethodology, str):
            self.appliedMethodology = str(self.appliedMethodology)

        if self.alternativeTitle is not None and not isinstance(self.alternativeTitle, str):
            self.alternativeTitle = str(self.alternativeTitle)

        if self.alternativePrefix is not None and not isinstance(self.alternativePrefix, str):
            self.alternativePrefix = str(self.alternativePrefix)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.provenanceProperty = Slot(uri=TIBTS.provenanceProperty, name="provenanceProperty", curie=TIBTS.curie('provenanceProperty'),
                   model_uri=TIBTS.provenanceProperty, domain=None, range=Optional[str])

slots.versionInformation = Slot(uri=TIBTS.versionInformation, name="versionInformation", curie=TIBTS.curie('versionInformation'),
                   model_uri=TIBTS.versionInformation, domain=None, range=Optional[str])

slots.purl = Slot(uri=DCAT.accessURL, name="purl", curie=DCAT.curie('accessURL'),
                   model_uri=TIBTS.purl, domain=None, range=URIRef)

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=TIBTS.title, domain=None, range=str)

slots.preferredPrefix = Slot(uri=VANN.preferredNamespacePrefix, name="preferredPrefix", curie=VANN.curie('preferredNamespacePrefix'),
                   model_uri=TIBTS.preferredPrefix, domain=None, range=str)

slots.acronym = Slot(uri=MOD.acronym, name="acronym", curie=MOD.curie('acronym'),
                   model_uri=TIBTS.acronym, domain=None, range=Optional[str])

slots.license = Slot(uri=DCTERMS.license, name="license", curie=DCTERMS.curie('license'),
                   model_uri=TIBTS.license, domain=None, range=Union[str, URIorCURIE])

slots.creator = Slot(uri=DCTERMS.creator, name="creator", curie=DCTERMS.curie('creator'),
                   model_uri=TIBTS.creator, domain=None, range=Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]])

slots.versionInfo = Slot(uri=OWL.versionInfo, name="versionInfo", curie=OWL.curie('versionInfo'),
                   model_uri=TIBTS.versionInfo, domain=None, range=str)

slots.versionIRI = Slot(uri=OWL.versionIRI, name="versionIRI", curie=OWL.curie('versionIRI'),
                   model_uri=TIBTS.versionIRI, domain=None, range=Optional[str])

slots.versionNotes = Slot(uri=ADMS.versionNotes, name="versionNotes", curie=ADMS.curie('versionNotes'),
                   model_uri=TIBTS.versionNotes, domain=None, range=str)

slots.created = Slot(uri=DCTERMS.created, name="created", curie=DCTERMS.curie('created'),
                   model_uri=TIBTS.created, domain=None, range=str)

slots.modificationDate = Slot(uri=DCTERMS.modified, name="modificationDate", curie=DCTERMS.curie('modified'),
                   model_uri=TIBTS.modificationDate, domain=None, range=Union[str, List[str]])

slots.description = Slot(uri=DCTERM.description, name="description", curie=DCTERM.curie('description'),
                   model_uri=TIBTS.description, domain=None, range=str)

slots.issueTracker = Slot(uri=DOAP['bug-database'], name="issueTracker", curie=DOAP.curie('bug-database'),
                   model_uri=TIBTS.issueTracker, domain=None, range=str)

slots.documentation = Slot(uri=DCTERMS.isReferencedBy, name="documentation", curie=DCTERMS.curie('isReferencedBy'),
                   model_uri=TIBTS.documentation, domain=None, range=str)

slots.imports = Slot(uri=OWL.imports, name="imports", curie=OWL.curie('imports'),
                   model_uri=TIBTS.imports, domain=None, range=str)

slots.contributor = Slot(uri=DCTERMS.contributor, name="contributor", curie=DCTERMS.curie('contributor'),
                   model_uri=TIBTS.contributor, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.contactInfo = Slot(uri=TIBTS.contactInfo, name="contactInfo", curie=TIBTS.curie('contactInfo'),
                   model_uri=TIBTS.contactInfo, domain=None, range=Optional[str])

slots.fundingInfo = Slot(uri=TIBTS.fundingInfo, name="fundingInfo", curie=TIBTS.curie('fundingInfo'),
                   model_uri=TIBTS.fundingInfo, domain=None, range=Optional[str])

slots.audience = Slot(uri=TIBTS.audience, name="audience", curie=TIBTS.curie('audience'),
                   model_uri=TIBTS.audience, domain=None, range=Optional[str])

slots.domainCovered = Slot(uri=TIBTS.domainCovered, name="domainCovered", curie=TIBTS.curie('domainCovered'),
                   model_uri=TIBTS.domainCovered, domain=None, range=Optional[str])

slots.languageCovered = Slot(uri=TIBTS.languageCovered, name="languageCovered", curie=TIBTS.curie('languageCovered'),
                   model_uri=TIBTS.languageCovered, domain=None, range=Optional[str])

slots.languageExpressedIn = Slot(uri=TIBTS.languageExpressedIn, name="languageExpressedIn", curie=TIBTS.curie('languageExpressedIn'),
                   model_uri=TIBTS.languageExpressedIn, domain=None, range=Optional[str])

slots.status = Slot(uri=TIBTS.status, name="status", curie=TIBTS.curie('status'),
                   model_uri=TIBTS.status, domain=None, range=Optional[str])

slots.sourceRepository = Slot(uri=TIBTS.sourceRepository, name="sourceRepository", curie=TIBTS.curie('sourceRepository'),
                   model_uri=TIBTS.sourceRepository, domain=None, range=Optional[str])

slots.distributions = Slot(uri=TIBTS.distributions, name="distributions", curie=TIBTS.curie('distributions'),
                   model_uri=TIBTS.distributions, domain=None, range=Optional[str])

slots.applicationExample = Slot(uri=TIBTS.applicationExample, name="applicationExample", curie=TIBTS.curie('applicationExample'),
                   model_uri=TIBTS.applicationExample, domain=None, range=Optional[str])

slots.references = Slot(uri=TIBTS.references, name="references", curie=TIBTS.curie('references'),
                   model_uri=TIBTS.references, domain=None, range=Optional[str])

slots.citations = Slot(uri=TIBTS.citations, name="citations", curie=TIBTS.curie('citations'),
                   model_uri=TIBTS.citations, domain=None, range=Optional[str])

slots.derivedFrom = Slot(uri=DCTERMS.source, name="derivedFrom", curie=DCTERMS.curie('source'),
                   model_uri=TIBTS.derivedFrom, domain=None, range=Optional[Union[str, List[str]]])

slots.rootTerms = Slot(uri=TIBTS.rootTerms, name="rootTerms", curie=TIBTS.curie('rootTerms'),
                   model_uri=TIBTS.rootTerms, domain=None, range=Optional[str])

slots.alternativePrefix = Slot(uri=IDOT.alternatePrefix, name="alternativePrefix", curie=IDOT.curie('alternatePrefix'),
                   model_uri=TIBTS.alternativePrefix, domain=None, range=Optional[str])

slots.alternativeTitle = Slot(uri=DCTERMS.alternative, name="alternativeTitle", curie=DCTERMS.curie('alternative'),
                   model_uri=TIBTS.alternativeTitle, domain=None, range=Optional[str])

slots.relatedVersions = Slot(uri=TIBTS.relatedVersions, name="relatedVersions", curie=TIBTS.curie('relatedVersions'),
                   model_uri=TIBTS.relatedVersions, domain=None, range=Optional[str])

slots.socialMediaAccount = Slot(uri=TIBTS.socialMediaAccount, name="socialMediaAccount", curie=TIBTS.curie('socialMediaAccount'),
                   model_uri=TIBTS.socialMediaAccount, domain=None, range=Optional[str])

slots.identifierPattern = Slot(uri=TIBTS.identifierPattern, name="identifierPattern", curie=TIBTS.curie('identifierPattern'),
                   model_uri=TIBTS.identifierPattern, domain=None, range=Optional[str])

slots.format = Slot(uri=TIBTS.format, name="format", curie=TIBTS.curie('format'),
                   model_uri=TIBTS.format, domain=None, range=Optional[str])

slots.homepage = Slot(uri=TIBTS.homepage, name="homepage", curie=TIBTS.curie('homepage'),
                   model_uri=TIBTS.homepage, domain=None, range=Optional[str])

slots.publisher = Slot(uri=TIBTS.publisher, name="publisher", curie=TIBTS.curie('publisher'),
                   model_uri=TIBTS.publisher, domain=None, range=Optional[str])

slots.comments = Slot(uri=TIBTS.comments, name="comments", curie=TIBTS.curie('comments'),
                   model_uri=TIBTS.comments, domain=None, range=Optional[str])

slots.exampleIdentifier = Slot(uri=TIBTS.exampleIdentifier, name="exampleIdentifier", curie=TIBTS.curie('exampleIdentifier'),
                   model_uri=TIBTS.exampleIdentifier, domain=None, range=Optional[str])

slots.exampleClass = Slot(uri=TIBTS.exampleClass, name="exampleClass", curie=TIBTS.curie('exampleClass'),
                   model_uri=TIBTS.exampleClass, domain=None, range=Optional[str])

slots.mailingList = Slot(uri=TIBTS.mailingList, name="mailingList", curie=TIBTS.curie('mailingList'),
                   model_uri=TIBTS.mailingList, domain=None, range=Optional[str])

slots.logo = Slot(uri=TIBTS.logo, name="logo", curie=TIBTS.curie('logo'),
                   model_uri=TIBTS.logo, domain=None, range=Optional[str])

slots.otherIdentifier = Slot(uri=TIBTS.otherIdentifier, name="otherIdentifier", curie=TIBTS.curie('otherIdentifier'),
                   model_uri=TIBTS.otherIdentifier, domain=None, range=Optional[str])

slots.developmentEnvironment = Slot(uri=TIBTS.developmentEnvironment, name="developmentEnvironment", curie=TIBTS.curie('developmentEnvironment'),
                   model_uri=TIBTS.developmentEnvironment, domain=None, range=Optional[str])

slots.mappingRessources = Slot(uri=TIBTS.mappingRessources, name="mappingRessources", curie=TIBTS.curie('mappingRessources'),
                   model_uri=TIBTS.mappingRessources, domain=None, range=Optional[str])

slots.competencyQuestions = Slot(uri=TIBTS.competencyQuestions, name="competencyQuestions", curie=TIBTS.curie('competencyQuestions'),
                   model_uri=TIBTS.competencyQuestions, domain=None, range=Optional[str])

slots.appliedMethodology = Slot(uri=TIBTS.appliedMethodology, name="appliedMethodology", curie=TIBTS.curie('appliedMethodology'),
                   model_uri=TIBTS.appliedMethodology, domain=None, range=Optional[str])