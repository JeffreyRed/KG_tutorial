import spacy

nlp = spacy.load("en_core_web_sm")


def extract_entities(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities


if __name__ == "__main__":
    text = """
    Albert Einstein was born in Germany.
    Albert Einstein worked at Princeton University.
    Marie Curie was born in Poland.
    """

    entities = extract_entities(text)

    for e in entities:
        print(e)