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
    bind_namespace(g)
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

def bind_namespace(graph):
    graph.namespace_manager.bind('aas', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/'))
    graph.namespace_manager.bind('aasaas', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/AssetAdministrationShell/'))
    graph.namespace_manager.bind('aasdata', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/HasDataSpecification/'))
    graph.namespace_manager.bind('aasida', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/Identifiable/'))
    graph.namespace_manager.bind('aaside', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/Identifier/'))
    graph.namespace_manager.bind('aaskey', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/Key/'))
    graph.namespace_manager.bind('aaskeyelem', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/KeyElements/'))
    graph.namespace_manager.bind('aasprop', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/Property/'))
    graph.namespace_manager.bind('aasrange', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/Range/'))
    graph.namespace_manager.bind('aasref', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/Reference/'))
    graph.namespace_manager.bind('aasrel', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/RelationshipElement/'))
    graph.namespace_manager.bind('aassem', rdflib.URIRef('https://admin-shell.io/aas/3/0/RC01/HasSemantics/'))
    graph.namespace_manager.bind('owl', rdflib.URIRef('http://www.w3.org/2002/07/owl#'))
    graph.namespace_manager.bind('xsd', rdflib.URIRef('http://www.w3.org/2001/XMLSchema#'))

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
