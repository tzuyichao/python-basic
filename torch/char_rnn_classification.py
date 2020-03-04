# from https://pytorch.org/tutorials/intermediate/char_rnn_classification_tutorial.html
from __future__ import unicode_literals, print_function, division
from io import open
import glob
import os

def findFiles(path):
    return glob.glob(path)

print(findFiles('../data/names/*.txt'))

import unicodedata
import string

all_letters = string.ascii_letters + " .,;'"
n_letters = len(all_letters)

print(all_letters)
print(n_letters)

def unicodeToAscii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) 
    if unicodedata.category(c) != 'Mn' 
    and c in all_letters)

text = 'Ślusàrski'
print(unicodeToAscii(text))

for c in unicodedata.normalize('NFD', text):
    print(unicodedata.category(c))
