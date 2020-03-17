from nltk import ngrams
from nltk import word_tokenize

str = 'The cute little boy is playing with the kitten.'

print('source:', str)
print('Using split()')
print(list(ngrams(str.split(), 2)))
print('Using word_tokenize()')
print(list(ngrams(word_tokenize(str), 2)))
