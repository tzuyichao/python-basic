from protobufs.user_pb2 import User

u = User()
u.id = 1
u.name = 'John Doe'
u.email = 'john@email.com'

output = u.SerializeToString()
print(output)

user = User()
user.ParseFromString(output)
print(str(user))

print('id: ', user.id, ', name: ', user.name, ', email: ', user.email)

