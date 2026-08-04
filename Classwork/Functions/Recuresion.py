
def square(a):
    print(a*a)
    a+=1
    if a<=20:
        square(a)

square(1)

def factorial(n):
    print(n)
    # Base case: 0