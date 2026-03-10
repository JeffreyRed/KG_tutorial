import pandas as pd
from py2neo import Graph, Node, Relationship

# --------------------------
# 1. Connect to Neo4j
# --------------------------
graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Clear existing graph (for demo purposes)
graph.delete_all()

# --------------------------
# 2. Load triples
# --------------------------
triples = pd.read_csv("data/kg_triples.tsv", sep="\t", names=["head","relation","tail"])

# --------------------------
# 3. Create nodes and relationships
# --------------------------
for _, row in triples.iterrows():
    # Create or merge nodes
    h_node = Node("Entity", name=row["head"])
    t_node = Node("Entity", name=row["tail"])
    graph.merge(h_node, "Entity", "name")
    graph.merge(t_node, "Entity", "name")

    # Create relationship
    rel = Relationship(h_node, row["relation"], t_node)
    graph.merge(rel)

print("✅ Knowledge graph loaded into Neo4j!")

# --------------------------
# 4. Example queries
# --------------------------

# a) Find all triples for Albert_Einstein
query1 = """
MATCH (h:Entity {name: 'Albert_Einstein'})-[r]->(t:Entity)
RETURN r.type AS relation, t.name AS tail
"""
result1 = graph.run(query1).data()
print("\nAlbert_Einstein relations:")
for record in result1:
    print(record["relation"], "->", record["tail"])

# b) Find all entities born in Germany
query2 = """
MATCH (h:Entity)-[:born_in]->(t:Entity {name: 'Germany'})
RETURN h.name AS entity
"""
result2 = graph.run(query2).data()
print("\nEntities born in Germany:")
for record in result2:
    print(record["entity"])