

CREATE TABLE "Ontology" (
	purl TEXT NOT NULL, 
	title TEXT NOT NULL, 
	"preferredPrefix" TEXT NOT NULL, 
	acronym TEXT, 
	license TEXT NOT NULL, 
	"versionInfo" TEXT NOT NULL, 
	"versionIRI" TEXT NOT NULL, 
	"versionNotes" TEXT NOT NULL, 
	created TEXT NOT NULL, 
	description TEXT NOT NULL, 
	"issueTracker" TEXT NOT NULL, 
	documentation TEXT NOT NULL, 
	imports TEXT NOT NULL, 
	"contactInfo" TEXT, 
	"fundingInfo" TEXT, 
	audience TEXT, 
	"domainCovered" TEXT, 
	"languageCovered" TEXT, 
	"languageExpressedIn" TEXT, 
	status TEXT, 
	"sourceRepository" TEXT, 
	distributions TEXT, 
	"applicationExample" TEXT, 
	"references" TEXT, 
	citations TEXT, 
	"rootTerms" TEXT, 
	"relatedVersions" TEXT, 
	"socialMediaAccount" TEXT, 
	"identifierPattern" TEXT, 
	format TEXT, 
	homepage TEXT, 
	publisher TEXT, 
	comments TEXT, 
	"exampleIdentifier" TEXT, 
	"exampleClass" TEXT, 
	"mailingList" TEXT, 
	logo TEXT, 
	"otherIdentifier" TEXT, 
	"developmentEnvironment" TEXT, 
	"mappingRessources" TEXT, 
	"competencyQuestions" TEXT, 
	"appliedMethodology" TEXT, 
	"alternativeTitle" TEXT, 
	"alternativePrefix" TEXT, 
	PRIMARY KEY (purl)
);

CREATE TABLE "SkosConceptScheme" (
	purl TEXT NOT NULL, 
	title TEXT NOT NULL, 
	"preferredPrefix" TEXT NOT NULL, 
	acronym TEXT, 
	license TEXT NOT NULL, 
	"versionInfo" TEXT NOT NULL, 
	"versionIRI" TEXT NOT NULL, 
	"versionNotes" TEXT NOT NULL, 
	created TEXT NOT NULL, 
	description TEXT NOT NULL, 
	"issueTracker" TEXT NOT NULL, 
	documentation TEXT NOT NULL, 
	imports TEXT NOT NULL, 
	"contactInfo" TEXT, 
	"fundingInfo" TEXT, 
	audience TEXT, 
	"domainCovered" TEXT, 
	"languageCovered" TEXT, 
	"languageExpressedIn" TEXT, 
	status TEXT, 
	"sourceRepository" TEXT, 
	distributions TEXT, 
	"applicationExample" TEXT, 
	"references" TEXT, 
	citations TEXT, 
	"rootTerms" TEXT, 
	"relatedVersions" TEXT, 
	"socialMediaAccount" TEXT, 
	"identifierPattern" TEXT, 
	format TEXT, 
	homepage TEXT, 
	publisher TEXT, 
	comments TEXT, 
	"exampleIdentifier" TEXT, 
	"exampleClass" TEXT, 
	"mailingList" TEXT, 
	logo TEXT, 
	"otherIdentifier" TEXT, 
	"developmentEnvironment" TEXT, 
	"mappingRessources" TEXT, 
	"competencyQuestions" TEXT, 
	"appliedMethodology" TEXT, 
	"alternativeTitle" TEXT, 
	"alternativePrefix" TEXT, 
	PRIMARY KEY (purl)
);

CREATE TABLE "Ontology_creator" (
	backref_id TEXT, 
	creator TEXT NOT NULL, 
	PRIMARY KEY (backref_id, creator), 
	FOREIGN KEY(backref_id) REFERENCES "Ontology" (purl)
);

CREATE TABLE "Ontology_modificationDate" (
	backref_id TEXT, 
	"modificationDate" TEXT NOT NULL, 
	PRIMARY KEY (backref_id, "modificationDate"), 
	FOREIGN KEY(backref_id) REFERENCES "Ontology" (purl)
);

CREATE TABLE "Ontology_contributor" (
	backref_id TEXT, 
	contributor TEXT, 
	PRIMARY KEY (backref_id, contributor), 
	FOREIGN KEY(backref_id) REFERENCES "Ontology" (purl)
);

CREATE TABLE "Ontology_derivedFrom" (
	backref_id TEXT, 
	"derivedFrom" TEXT, 
	PRIMARY KEY (backref_id, "derivedFrom"), 
	FOREIGN KEY(backref_id) REFERENCES "Ontology" (purl)
);

CREATE TABLE "SkosConceptScheme_creator" (
	backref_id TEXT, 
	creator TEXT NOT NULL, 
	PRIMARY KEY (backref_id, creator), 
	FOREIGN KEY(backref_id) REFERENCES "SkosConceptScheme" (purl)
);

CREATE TABLE "SkosConceptScheme_modificationDate" (
	backref_id TEXT, 
	"modificationDate" TEXT NOT NULL, 
	PRIMARY KEY (backref_id, "modificationDate"), 
	FOREIGN KEY(backref_id) REFERENCES "SkosConceptScheme" (purl)
);

CREATE TABLE "SkosConceptScheme_contributor" (
	backref_id TEXT, 
	contributor TEXT, 
	PRIMARY KEY (backref_id, contributor), 
	FOREIGN KEY(backref_id) REFERENCES "SkosConceptScheme" (purl)
);

CREATE TABLE "SkosConceptScheme_derivedFrom" (
	backref_id TEXT, 
	"derivedFrom" TEXT, 
	PRIMARY KEY (backref_id, "derivedFrom"), 
	FOREIGN KEY(backref_id) REFERENCES "SkosConceptScheme" (purl)
);
