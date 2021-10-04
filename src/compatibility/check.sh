#!/bin/bash

# wrapper for running compatibility checks
# Usage: bash check.sh

cp ../../data/__direct.ttl . && ../../.venv/bin/python rdflib_shape_val.py __direct.ttl && rm ./__direct.ttl
cp ../../data/__eclass.ttl . && ../../.venv/bin/python rdflib_query_exec.py __eclass.ttl && rm ./__eclass.ttl