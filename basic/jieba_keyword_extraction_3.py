import jieba
import jieba.analyse
import requests

text = requests.get('http://rare-technologies.com/the_matrix_synopsis.txt').text

print('-'*40)
print(' TextRank')
print('-'*40)


for x, w in jieba.analyse.extract_tags(text, withWeight=True):
    print('%s %s' % (x, w))

