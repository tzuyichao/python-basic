from tasks import add

r = add.delay(4, 4)

print(r.ready())

print(r.get(timeout=2))

print("Done.")