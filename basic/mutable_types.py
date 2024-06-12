temps = [87, 76, 79]
highs = temps
print(temps is highs)
temps += [81]
print(temps is highs)
print(highs)
print(temps)
