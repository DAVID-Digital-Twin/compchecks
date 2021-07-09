#!/usr/bin/env python3
"""run as script with .ttl input files as arguments"""

import rdflib
import sys

def load_query(querypath):
    return open(querypath, "r").read()

def simplify_aas_graph(aasfile, output, *updatequeries):
    """
    :param updatequeries: ordered 2-tuples of insert and delete queries
    """
    g = rdflib.Graph()
    g.parse(aasfile, format="ttl")
    for uq in updatequeries:
        g.update(load_query(uq))
    g.serialize(destination=output, format="turtle")

def simplify_several(inputs):
    """
    :inputs: ttl files
    """
    querynames = ["keyfix", "semanticidfix", "dataspecfix",\
                  "relfix_first_DP", "relfix_first_OP", "relfix_second_DP", "relfix_second_OP",\
                  "dtfix_prop_int", "dtfix_prop_float", "dtfix_prop_str",\
                  "dtfix_range_int", "dtfix_range_float", "dtfix_range_str"]
    queries = [s + ".sparql" for s in querynames]
    for i in inputs:
        simplify_aas_graph(i, "_"+ i, *queries)

if __name__ == "__main__":
    simplify_several(sys.argv[1:])
