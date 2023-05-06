from rdflib import Graph
from graphql_to_rdf import graphql_to_rdf
from rdf_to_graphql import rdf_to_graphql
from validation import validate_rdf

def main():
    # Generate sample GraphQL data
    graphql_query = """
    {
        character(name: "Scarlet Witch") {
            name
            alias
            abilities
            team {
                name
                members {
                    name
                }
            }
        }
    }
    """

    # Convert GraphQL to RDF/OWL
    rdf_graph = graphql_to_rdf(graphql_query)
    rdf_data = rdf_graph.serialize(format='turtle').decode('utf-8')

    # Validate RDF/OWL
    is_valid = validate_rdf(rdf_data)
    if not is_valid:
        print("Invalid RDF/OWL data.")
        return

    # Convert RDF/OWL to GraphQL
    rdf_graph = Graph().parse(data=rdf_data, format='turtle')
    graphql_query = rdf_to_graphql(rdf_graph)
    print("Converted GraphQL query:")
    print(graphql_query)

if __name__ == '__main__':
    main()
