# compchecks
compatibility checks based on semantic digital twins

## content
* src
  * specs: ontology supplement
  * transformation: source files for running transformation based on [RMLio's RMLMapper](https://github.com/RMLio/rmlmapper-java)
    * functions: custom function implementation for the rmlmapper
    * maps: rml map based on [aas-specs' rdf-ontology.ttl (V3.0.RC01)](https://github.com/admin-shell-io/aas-specs/blob/master/schemas/rdf/rdf-ontology.ttl)
  * simplification: SPARQL queries for graph simplification; Python module for easy execution using RDFLib
  * compatibility: SPARQL query and SHACL shape for checking compatibility; Python module for easy execution using RDFLib
  * xml2ttl.sh: helper script for running the transformation
* data: AAS XML input files

## requirements
* Python 3.8.3+
* bash recommended
* Java

## instructions
* install dependencies: ```make setup```
* transform example aas files: ```make transform```
* simplify example graphs: ```make simplify```
* run compatibility checks: ```make check```
* or combined (after setup): ```make compcheck```

## citation (accepted)
Please use the following bibtex entry:
```
@inproceedings{ocker2021ieem,
author = {Ocker, Felix and Vogel-Heuser, Birgit and Sch{\"o}n, Hauke and Mieth, Robert},
booktitle = {IEEM},
publisher = {IEEE},
title = {{Leveraging Digital Twins for Compatibility Checks in Production Systems Engineering (accepted)}},
year = {2021}
}
```

## license
GPL v3.0

## contact
Felix Ocker - [felix.ocker@tum.de](mailto:felix.ocker@tum.de)\
Robert Mieth - [robert.mieth@tum.de](mailto:robert.mieth@tum.de)\
Technical University of Munich - Institute of Automation and Information Systems <https://www.mw.tum.de/en/ais/homepage/>
