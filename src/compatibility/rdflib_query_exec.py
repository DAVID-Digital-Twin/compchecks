#!/usr/bin/env python3
"""run as script with .ttl input file as argument"""

import rdflib
import sys

def load_query(querypath):
    return open(querypath, "r").read()

def query_aas_graph(aasfile):
    """
    :param aasfile: filename of aas onto
    """
    g = rdflib.Graph()
    g.parse(aasfile, format="ttl")
    return list(g.query(load_query("comp_check.sparql")))

def query_several(inputs):
    """
    :input: ttl files
    """
    for i in inputs:
        results = [[str(e) for e in row] for row in query_aas_graph(i)]
        print(f"results for {i}:")
        print(*results, sep="\n")

if __name__ == "__main__":
    query_several(sys.argv[1:])
