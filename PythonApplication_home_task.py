# Super Simple Calculator Program

while True:
    print("\nType 1 for Calculator")
    print("Type 2 to check Even or Odd")
    print("Type 3 to calculate Percentage")
    print("Type 4 to Exit")

    choice = input("Enter your option (1-4): ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        op = input("Enter operator (+ - * /): ")

        if op == "+":
            print("The sum is:", a + b)
        elif op == "-":
            print("The difference is:", a - b)
        elif op == "*":
            print("The product is:", a * b)
        elif op == "/":
            print("The result is:", a / b)
        else:
            print("Invalid operator")

    elif choice == "2":
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")

    elif choice == "3":
        part = float(input("Enter the part value: "))
        total = float(input("Enter the total value: "))
        percent = (part / total) * 100
        print("Percentage is:", percent, "%")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
