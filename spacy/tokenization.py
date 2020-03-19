import spacy

nlp = spacy.load('en_core_web_sm')

review = "I’m so happy I went to this awesome Vegas buffet!"

doc = nlp(review)

for token in doc:
    print(token.text, token.pos_, token.lemma_, token.is_stop)
