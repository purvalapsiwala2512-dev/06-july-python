num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))


total_sum = num1 + num2
difference = num1 - num2
product = num1 * num2


if num2 != 0:
    quotient = num1/num2
else:
    quotient = "Cannot divide by zero"


print(f"Sum: {total_sum}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")