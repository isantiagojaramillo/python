"""System module."""

message = "Menu:\n"
message += "1. Add\n"
message += "2. Substraction\n"
message += "3. Multiplication\n"
message += "4. Division\n"
message += "5. Log out\n"



while True:
    print(message)

    option=int(input("Enter an option: "))

    if option == 1:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        result = number1 + number2
        print("The result is: ", result)
    elif option == 2:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        result = number1 - number2
        print("The result is: ",result)
    elif option == 3:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        result = number1 * number2
        print("The result is: ",result)
    elif option == 4:
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        result = number1 / number2
        print("The result is: ",result)
    elif option == 5:
        print("Thank you for using the calculator!")
        break
    else:
        print("Invalid option")





