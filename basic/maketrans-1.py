x = "~x^(y%z)"
table = x.maketrans("~^()", "!&[]")
print(x.translate(table))