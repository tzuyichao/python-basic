import jieba
import jieba.analyse

s = "台中銀保險經紀人股份有限公司違反保險相關法令裁罰案"

print('*'*40)
print(s)
print('*'*40)

print('-'*40)
print(' TextRank')
print('-'*40)


for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

