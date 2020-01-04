import jieba
import jieba.analyse

s = "富蘭克林華美高科技基金經理人郭修伸指出，終端客戶啟動農曆年前拉貨潮，這次農曆新年落在1月底，台廠受此影響提前備貨，且市場資金充沛，及半導體、電子、汽車、橡膠、醫療、生技類股良性互補輪動，大盤表現並無疑慮。可檢視美國那斯達克指數是否繼續創新高，將有機會推升台灣科技股往上。"
for x, w in jieba.analyse.extract_tags(s, withWeight=True):
    print('%s %s' % (x, w))

print('-'*40)
print(' TextRank')
print('-'*40)