import pandas as pd

# FutureWarning: from_items is deprecated. Please use DataFrame.from_dict(dict(items), ...) instead. DataFrame.from_dict(OrderedDict(items)) may be used to preserve the key order.
df1 = pd.DataFrame.from_items([('column1', [1, 2, 3])])
print(df1)

df2 = pd.DataFrame.from_dict({'column1': [1, 2, 3]})
print(df2)

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)
print(s.index)