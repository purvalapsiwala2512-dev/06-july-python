print("--- Basic Calculator ---")

number1 = float(input("Enter first number: "))
operator = input("Enter an operator (+, -, *, /): ").strip()
number2 = float(input("Enter second number: "))


if operator == "+":
    result = number1 + number2
    print(f"Result: {number1} + {number2} = {result}")
elif operator == "-":
    result = number1 - number2
    print(f"Result: {number1} - {number2} = {result}")
elif operator == "*":
    result = number1 * number2
    print(f"Result: {number1} * {number2} = {result}")
elif operator == "/":
    if number2 != 0:
        result = number1 / number2
        print(f"Result: {number1} / {number2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator!")