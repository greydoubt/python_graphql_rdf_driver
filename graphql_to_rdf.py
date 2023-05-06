from rdflib import Graph, Namespace, RDF, RDFS


def graphql_to_rdf(graphql_query):
    graph = Graph()

    # Define your custom ontology namespaces
    my_ns = Namespace("http://example.com/ontology#")

    # convert GraphQL query to RDF triples

    subject = my_ns['subject']
    predicate = my_ns['predicate']
    object = my_ns['object']
    graph.add((subject, predicate, object))



    return graph
