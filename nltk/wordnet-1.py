import nltk
from nltk.corpus import wordnet as wn

nltk.download('wordnet')
print(wn.synsets('dog'))

print(wn.synset('dog.n.01').definition())