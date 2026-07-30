total = 0
deposit = 1

for day in range(1, 31):
    total = total + deposit
    deposit = deposit * 2

print("Total money in 30 days:", total)