import jieba
import jieba.analyse
from hanziconv import HanziConv

s = HanziConv.toSimplified("金融監督管理委員會(下稱金管會)近日通過對台中銀保險經紀人股份有限公司(下稱台中銀保經)違反法令之處分案。金管會於107年對台中銀保經之母公司台中商業銀行辦理一般業務檢查，發現台中銀保經有違反保險相關法令規定之情事，爰核處台中銀保經2項限期1個月改正，併處罰鍰新臺幣（下同）480萬元整。")

print('*'*40)
print(s)
print('*'*40)

print('-'*40)
print(' TextRank')
print('-'*40)


for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

