items = ["apple", "banana", "orange", "mango"]

print("Welcome to Python items sorter. This is the list: ")

for i in range(len(items)):
    print(items[i])



while True:
    while True:
        try:
            tomb = int(input
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
        items.sort()
        for i in range(len(items)):
            print(items[i])

    elif tomb == 2:
        desce = sorted(items, reverse = True)
        for i in range(len(desce)):
            print(desce[i])

    elif tomb == 3:
        print("Goodbye!")
        break
