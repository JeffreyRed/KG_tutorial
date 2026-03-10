import spacy

nlp = spacy.load("en_core_web_sm")


def extract_triples(text):

    triples = []
    doc = nlp(text)

    for sent in doc.sents:

        sent_doc = nlp(sent.text)

        persons = [ent.text.replace(" ", "_") for ent in sent_doc.ents if ent.label_ == "PERSON"]
        locations = [ent.text.replace(" ", "_") for ent in sent_doc.ents if ent.label_ == "GPE"]
        orgs = [ent.text.replace(" ", "_") for ent in sent_doc.ents if ent.label_ == "ORG"]

        if "born" in sent.text and persons and locations:
            triples.append((persons[0], "born_in", locations[0]))

        if "worked" in sent.text and persons and orgs:
            triples.append((persons[0], "worked_at", orgs[0]))

    return triples


def save_triples(triples, file="data/kg_triples.tsv"):

    with open(file, "w") as f:
        for h, r, t in triples:
            f.write(f"{h}\t{r}\t{t}\n")


if __name__ == "__main__":

    text = """
    Albert Einstein was born in Germany.
    Albert Einstein worked at Princeton University.
    Marie Curie was born in Poland.
    """

    triples = extract_triples(text)

    print(triples)

    save_triples(triples)