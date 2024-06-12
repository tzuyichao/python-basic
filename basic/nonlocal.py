spam = True
# eggs = 10

def order():
    eggs = 12

    def cook():
        nonlocal eggs

        if spam:
            print("Spam!")
        if eggs:
            eggs -= 1
            print(f"...and eggs. {eggs}")
    cook()

order()
