import nltk

text = "I'd like this"

tokens = nltk.wordpunct_tokenize(text)
print(tokens)

from nltk.tokenize.treebank import TreebankWordTokenizer

print(TreebankWordTokenizer().tokenize(text))