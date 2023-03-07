# Ontology-Metadata

CAVE: Work in Progress - based on [this draft](https://docs.google.com/document/d/1FRmCQ7eD6PcqSQgPbqCGjki3t39ROoYozsehCPX9E0Q)

The metadata schema of the TIB Terminology Service that formalizes which metadata annotations are required, recommended and optional for an OWL ontology or SKOS vocabulary that is supposed to be index in the TIB TS.
## Website

* [https://stroemphi.github.io/Ontology-Metadata](https://stroemphi.github.io/Ontology-Metadata)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
    * [ontology_metadata](src/ontology_metadata)
        * [schema](src/ontology_metadata/schema) -- LinkML schema (edit this)
* [datamodel](src/ontology_metadata/datamodel) -- Generated python datamodel
* [tests](tests/) - python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

- `make all`: make everything
- `make deploy`: deploys site

</details>

## Credits

this project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)
