import pandas as pd

dates = pd.date_range('2016-04-01', periods=6, freq='D')

print(dates)

temps1 = pd.Series([80, 82, 85, 90, 83, 87], index=dates)
temps2 = pd.Series([70, 75, 69, 83, 79, 77], index=dates)

tempa_df = pd.DataFrame({'Missoula': temps1, 'Philadephia': temps2})

print('Print temperature DataFrame')
print(tempa_df)

print('Print Philadephia in temperature DataFrame')
print(tempa_df['Philadephia'])

print('tempa_df[Missoula] - tempa_df[Philadephia]')
print(tempa_df['Missoula'] - tempa_df['Philadephia'])

print('Add Difference colum from two cloumn\'s computation')
tempa_df['Difference'] = tempa_df['Missoula'] - tempa_df['Philadephia']
print(tempa_df)