x = [1, 3, 5, 0, -1, 3, -2]
result = []
for item in x:
    if item >= 0:
        result.append(item)

print("result: ", result)

result2 = [item for item in x if item >= 0]
print(result2)