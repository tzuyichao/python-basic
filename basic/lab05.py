temperatures = []
with open('lab_05.txt') as infile:
  for row in infile:
    temperatures.append(int(row.strip()))

print(temperatures)
print('max:', max(temperatures))
print('min:', min(temperatures))
print('len:', len(temperatures))
print('sum:', sum(temperatures))
temperatures.sort()
print('sort:', temperatures)