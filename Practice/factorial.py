number = 10
fact = 1
for i in range(number,0,-1):
    fact = fact*i

print(fact)


#using while loop:

number = 10
fact = 1
i = number

while i > 0:
    fact = fact * i
    i -= 1

print(fact)