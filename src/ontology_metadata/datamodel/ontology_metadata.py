# Auto generated from ontology_metadata.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-03-07T13:57:03
# Schema: Ontology-Metadata-TIB
#
# id: http://terminology.tib.eu/schema
# description: The metadata schema of the TIB Terminology Service that formalizes which metadata annotations are
#              required, recommended and optional for an OWL ontology or SKOS vocabulary that is supposed to be
#              index in the TIB TS:
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
    acronym: Optional[str] = None

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

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

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

    alternativeTitle: Optional[str] = None
    alternativePrefix: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.alternativeTitle is not None and not isinstance(self.alternativeTitle, str):
            self.alternativeTitle = str(self.alternativeTitle)

        if self.alternativePrefix is not None and not isinstance(self.alternativePrefix, str):
            self.alternativePrefix = str(self.alternativePrefix)

        super().__post_init__(**kwargs)


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
    acronym: Optional[str] = None
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

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

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
    acronym: Optional[str] = None
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

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

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
                   model_uri=TIBTS.creator, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.versionInfo = Slot(uri=OWL.versionInfo, name="versionInfo", curie=OWL.curie('versionInfo'),
                   model_uri=TIBTS.versionInfo, domain=None, range=str)

slots.versionURI = Slot(uri=OWL.versionIRI, name="versionURI", curie=OWL.curie('versionIRI'),
                   model_uri=TIBTS.versionURI, domain=None, range=Optional[str])

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

slots.derivedFrom = Slot(uri=DCTERMS.source, name="derivedFrom", curie=DCTERMS.curie('source'),
                   model_uri=TIBTS.derivedFrom, domain=None, range=Optional[Union[str, List[str]]])

slots.alternativePrefix = Slot(uri=IDOT.alternatePrefix, name="alternativePrefix", curie=IDOT.curie('alternatePrefix'),
                   model_uri=TIBTS.alternativePrefix, domain=None, range=Optional[str])

slots.alternativeTitle = Slot(uri=DCTERMS.alternative, name="alternativeTitle", curie=DCTERMS.curie('alternative'),
                   model_uri=TIBTS.alternativeTitle, domain=None, range=Optional[str])