from nltk import ngrams
from nltk import word_tokenize
from nltk.corpus import stopwords
import string

str = 'The cute little boy is playing with the kitten.'

print('source:', str)
print('Using split()')
print(list(ngrams(str.split(), 2)))
print('Using word_tokenize()')
print('tokenized: ', word_tokenize(str))
print('stopwords: ', stopwords.words('english'))
print('string punctuation: ', string.punctuation)

transtab = str.maketrans(string.punctuation, ' '*len(string.punctuation))
str = str.translate(transtab)
print('translated source:', str)

print(list(ngrams(word_tokenize(str), 2)))
