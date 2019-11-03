import spacy

texts = [
    "Net income was $9.4 million compared to the prior year of $2.7 million.",
    "Revenue exceeded twelve billion dollars, with a loss of $1b.",
]

nlp = spacy.load('en_core_web_sm')

for doc in nlp.pipe(texts, disable=["tagger", "parser"]):
    print([(ent.text, ent.label_) for ent in doc.ents])


print(nlp.pipeline)

doc = nlp.make_doc("Net income was $9.4 million compared to the prior year of $2.7 million.")
for name, proc in nlp.pipeline:
    print('name: ', name)
    doc = proc(doc)

print([(ent.text, ent.label_) for ent in doc.ents])
