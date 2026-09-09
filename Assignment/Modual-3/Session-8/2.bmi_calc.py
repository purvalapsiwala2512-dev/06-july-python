import math

weight = float(input("Enter weight in kg:"))
height = float(input("Enter height in meters:"))

squared = math.pow(height,2)
bmi =weight/squared
a = round(bmi,2)
print(a)