from sklearn.feature_extraction.text import CountVectorizer

corpus = [  
    'This is the first document.',  
    'This is the second second document.',  
    'And the third one.',  
    'Is this the first document?',  
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(corpus)

word = vectorizer.get_feature_names()

print(word)
print(X.toarray())

from sklearn.feature_extraction.text import TfidfTransformer

transform = TfidfTransformer()
print(transform)
tfidf = transform.fit_transform(X)
print(tfidf.toarray())

from sklearn.feature_extraction.text import TfidfVectorizer

tfidfVectorizer = TfidfVectorizer(use_idf=True)
X1 = tfidfVectorizer.fit_transform(corpus)
print(tfidfVectorizer.idf_)
idf = tfidfVectorizer.idf_
print(dict(zip(tfidfVectorizer.get_feature_names(), idf)))