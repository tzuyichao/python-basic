# source: https://medium.com/@falconives/day-91-gensim-for-text-summarization-12aeb6485326
import requests
from gensim.summarization import summarize, keywords

text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt').text

print("Summary:")
print(summarize(text, ratio=0.01))

print("\nKeywords:")
print(keywords(text, ratio=0.01))

# Result
# Keywords:
# neo
# morpheus
# trinity
# cypher
# smith
# agents
# agent
# tank
# says
# saying
# 覺得應該做lemma

print("\nKeywords with lemma:")
print(keywords(text, ratio=0.01, lemmatize=True))