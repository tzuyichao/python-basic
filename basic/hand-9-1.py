def reverse(*arg):
    for i in range(0, len(arg)):
        print(arg[len(arg) - i - 1])

reverse()
reverse(1, 3, 4)