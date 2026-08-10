marks = int(input("Enter your marks (0-100): "))

# Validating input scope and assigning grades
if marks < 0 or marks > 100:
    print("Error: Please enter a valid score between 0 and 100.")
elif marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 40:
    print("Grade: D")
else:
    print("Grade: F")