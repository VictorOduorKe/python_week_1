#python program tha asks user to enter two number and operator then perfom the calculation

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (e.g., +, -, /, *): ")

#match operator allows the program to loop and check the type of oerator entered
match operator:
    case "+":
        print(f"The sum of {num1} and {num2} is: {num1 + num2}")
    case "-":
        print(f"The difference between {num1} and {num2} is: {num1 - num2}")
    case "/":
        if num2 != 0:
            print(f"Division of {num1} by {num2} is: {num1 / num2}")
        else:
            print("Error: Division by zero is not allowed.")
    case "*":
        print(f"Multiplication of {num1} and {num2} is: {num1 * num2}")
    case _:
        print("Invalid operator entered.")
