

CREATE TABLE "Ontology" (
	purl TEXT NOT NULL, 
	title TEXT NOT NULL, 
	"preferredPrefix" TEXT NOT NULL, 
	acronym TEXT, 
	license TEXT NOT NULL, 
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
	"alternativeTitle" TEXT, 
	"alternativePrefix" TEXT, 
	PRIMARY KEY (purl)
);
