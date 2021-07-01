#!/usr/bin/env python3
"""run as script with .ttl input file as argument"""

from pyshacl import validate
import rdflib
import sys

def load_file(querypath):
    return open(querypath, "r").read()

def validate_aas_graph(aasfile):
    """
    :param aasfile: filename of aas onto
    """
    g = rdflib.Graph()
    g.parse(aasfile, format="ttl")
    r = validate(g,
        shacl_graph="comp_check.ttl",
        abort_on_error=False,
        meta_shacl=False,
        advanced=True,
        js=False,
        debug=False)
    conforms, results_graph, results_text = r
    return conforms, results_text

def validate_several(inputs):
    """
    :input: ttl files
    """
    for i in inputs:
        results = validate_aas_graph(i)
        print(f"results for {i}:")
        print(*results, sep="\n")

if __name__ == "__main__":
    validate_several(sys.argv[1:])
