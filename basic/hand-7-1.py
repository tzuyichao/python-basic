data = {}
for i in range(0, 3):
    name = raw_input("Name? ")
    age = int(raw_input("Age? "))
    data[name] = age

print(data)
lookup = raw_input("Lookup name?")
if lookup in data.keys():
    print("Age: ", data[lookup])
else:
    print("Not Found")