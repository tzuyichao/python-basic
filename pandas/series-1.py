import pandas as pd

dates = pd.date_range('2016-04-01', '2016-04-06')

print('dates:', dates)

temps1 = pd.Series([80, 82, 85, 90, 83, 87], index=dates)

print('temps1:', temps1)

temps2 = pd.Series([70, 75, 69, 83, 79, 77], index=dates)

print('temps2:', temps2)

temp_diff = temps1 - temps2

print('temp_diff:', temp_diff)
print(temp_diff[2])
print('temperature diff mean:', temp_diff.mean())
