import pandas as pd

df = pd.read_csv('../data/goog.csv')
print(df)
print(df.Date)
print(type(df.Date))
print(df.Date[0])
print(type(df.Date[0]))

df = pd.read_csv('../data/goog.csv', parse_dates=['Date'])
print(df)
print(df.Date[0])
print(type(df.Date[0]))
