#!/bin/bash

# wrapper for transforming xmls to ttl
# Usage: bash xml2ttl.sh inputfiles

cat specs/rdf-ontology.ttl >> ./../data/output.ttl

for file in "$@"
do
    path=".\/..\/data\/"
    sed -i "s/unique_input_filename_placeholder/$path$file/g" transformation/maps/XML2RDF.rml.ttl
    java -jar transformation/rmlmapper.jar -v -m transformation/maps/XML2RDF.rml.ttl -f transformation/functions/functions.ttl transformation/functions/functions_grel.ttl transformation/functions/grel_java_mapping.ttl -s turtle -o $file.ttl
    git checkout transformation/maps/XML2RDF.rml.ttl
    echo >> output.ttl
    cat $file.ttl >> ./../data/output.ttl
    rm $file.ttl
done

