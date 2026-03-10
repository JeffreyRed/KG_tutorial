from rdflib import Graph

g = Graph()

g.parse("data/knowledge_graph.ttl", format="turtle")

print("Triples in graph:", len(g))

for s, p, o in g:
    print(s, p, o)