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
    bindings = prebind()
    for uq in updatequeries:
        g.update(load_query(uq), initBindings={'ordinal': bindings["first"], 'value': bindings["firstValue"] })
        g.update(load_query(uq), initBindings={'ordinal': bindings["second"], 'value': bindings["secondValue"] })
        g.update(load_query(uq), initBindings={'xsdType': bindings["float"], 'dtype': rdflib.Literal('float')})
        g.update(load_query(uq), initBindings={'xsdType': bindings["integer"], 'dtype': rdflib.Literal('integer')})
        g.update(load_query(uq), initBindings={'xsdType': bindings["string"], 'dtype': rdflib.Literal('string')})
    g.serialize(destination=output, format="turtle")

def simplify_several(inputs):
    """
    :inputs: ttl files
    """
    querynames = ["keyfix","semanticidfix", "dataspecfix",\
                  "relfix_DP", "relfix_OP",\
                  "dtfix_prop",\
                  "dtfix_range"]
    queries = [s + ".sparql" for s in querynames]
    for i in inputs:
        simplify_aas_graph(i, "_"+ i, *queries)


def prebind():
    prebindings = { "float": rdflib.URIRef("http://www.w3.org/2001/XMLSchema#float"),
                    "integer": rdflib.URIRef("http://www.w3.org/2001/XMLSchema#integer"),
                    "string": rdflib.URIRef("http://www.w3.org/2001/XMLSchema#string"),
                    "first": rdflib.URIRef("https://admin-shell.io/aas/3/0/RC01/RelationshipElement/first"),
                    "firstValue": rdflib.URIRef("https://admin-shell.io/aas/3/0/RC01/RelationshipElement/firstValue"),
                    "second": rdflib.URIRef("https://admin-shell.io/aas/3/0/RC01/RelationshipElement/second"),
                    "secondValue": rdflib.URIRef("https://admin-shell.io/aas/3/0/RC01/RelationshipElement/secondValue"),
                    }
    return prebindings

if __name__ == "__main__":
    simplify_several(sys.argv[1:])
