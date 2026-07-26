items = ["apple", "banana", "orange", "mango"]      # Existing hardcoded list.

print("Welcome to Python items sorter. This is the list: ")

for item in items:   
    print(item)



while True:
    while True:
        try:
            tomb = int(input    # In case you're wondering what is tomb, I just put a random variable name that came in my mind. It's not that deep.
                ("""
Choose what you want to do:
1. Sort in ascending order.
2. Sort in descending order.
3. Exit from the program.
                """))
            break
        
        except ValueError:
            print("Please enter a number corresponding to the choice")
            continue

    if tomb == 1:
        sorted(items)    # .sort() automatically sets the items inside a list in ascending order. It does not return any value.
        for item in items:   
            print(item)

    elif tomb == 2:
        desce = sorted(items, reverse = True)   # sorted() returns a new sorted list
        for desc in desce:   
            print(desc)


    elif tomb == 3:
        print("Goodbye!")
        break
