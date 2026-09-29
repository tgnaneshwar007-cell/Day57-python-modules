ch = 1

while ch != 5:
    print("\n1. Add")
    print("2. Sub")
    print("3. Mult")
    print("4. Div")
    print("5. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 5:
        print("Program ended")
        break

    if ch >= 1 and ch <= 4:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        if ch == 1:
            print("Result:", a + b)

        elif ch == 2:
            print("Result:", a - b)

        elif ch == 3:
            print("Result:", a * b)

        elif ch == 4:
            if b != 0:
                print("Result:", a / b)
            else:
                print("Cannot divide by zero")

    else:
        print("Invalid choice")