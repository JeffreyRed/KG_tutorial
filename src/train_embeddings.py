from pykeen.pipeline import pipeline
from pykeen.triples import TriplesFactory

# Load your triples
tf = TriplesFactory.from_path("data/kg_triples.tsv")

# For tiny datasets, just split manually (80/20 or copy everything to testing)
# Here we simply use the same tf for training and testing for demo purposes
training_tf = tf
testing_tf = tf  # toy example, same triples

# Run pipeline
result = pipeline(
    training=training_tf,
    testing=testing_tf,
    model="TransE",
    training_kwargs=dict(num_epochs=50),
)

print("Training complete")
print(result.model)