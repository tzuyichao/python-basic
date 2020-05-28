from rake_nltk import Rake

text = '''Challenges in natural language processing frequently involve
 speech recognition, natural language understanding, natural language
 generation (frequently from formal, machine-readable logical forms),
 connecting language and machine perception, dialog systems, or some
 combination thereof.'''

r = Rake(min_length=2, max_length=4)
r.extract_keywords_from_text(text)

print(r.get_ranked_phrases())

print(r.get_ranked_phrases_with_scores())