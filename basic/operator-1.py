import operator

d = [1, 2, 3, 4, 5]
select1 = operator.itemgetter(1)
select2 = operator.itemgetter(4, 2)

print(select1(d))
print(select2(d))