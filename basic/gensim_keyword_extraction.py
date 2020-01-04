from gensim.summarization import keywords

text = '''Challenges in natural language processing frequently involve
 speech recognition, natural language understanding, natural language
 generation (frequently from formal, machine-readable logical forms),
 connecting language and machine perception, dialog systems, or some
 combination thereof.'''
print(keywords(text).split('\n'))