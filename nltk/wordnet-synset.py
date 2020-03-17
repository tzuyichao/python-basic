from nltk.corpus import wordnet as wn 

print('all synset in trunk synsets')
for synset in wn.synsets('trunk'):
    print('Attributes')
    print('=================')
    print('Name: ', synset.name())
    print('Pos: ', synset.pos())
    print('Lemmas: ', synset.lemmas())
    print('Definition: ', synset.definition())
    print('Offset: ', synset.offset())
    print('Methods')
    print('=================')
    print('Root Hypernyms: ', synset.root_hypernyms())
    print('Hypernyms: ', synset.hypernyms())
    print('Hyponyms: ', synset.hyponyms())
    print()