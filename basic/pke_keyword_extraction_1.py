import pke

pos = {'NOUN', 'PROPN', 'ADJ'}

text = '''Challenges in natural language processing frequently involve
 speech recognition, natural language understanding, natural language
 generation (frequently from formal, machine-readable logical forms),
 connecting language and machine perception, dialog systems, or some
 combination thereof.'''
 
extractor = pke.unsupervised.TextRank()

extractor.load_document(input=text,
                        language='zh',
                        normalization=None)

extractor.candidate_weighting(window=2,
                              pos=pos,
                              top_percent=0.33)

keyphrases = extractor.get_n_best(n=10)

print(keyphrases)