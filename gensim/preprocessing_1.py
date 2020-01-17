texts = [['human', 'interface', 'computer'],
['survey', 'user', 'computer', 'system', 'response', 'time'],
['eps', 'user', 'interface', 'system'],
['system', 'human', 'system', 'eps'],
['user', 'response', 'time'],
['trees'],
['graph', 'trees'],
['graph', 'minors', 'trees'],
['graph', 'minors', 'survey']]

from gensim import corpora

dictionary = corpora.Dictionary(texts)
print(dictionary)
print("num docs:", dictionary.num_docs)
print("num docs:", dictionary.num_docs)

corpus = [dictionary.doc2bow(text) for text in texts]
print(corpus[0])
print(corpus[1])
print(corpus[2])

print(dictionary.get(0))
# id2token是lazy所以要先呼叫get(id)之類的才會work
print(dictionary.id2token[1])
print(dictionary.id2token[2])
