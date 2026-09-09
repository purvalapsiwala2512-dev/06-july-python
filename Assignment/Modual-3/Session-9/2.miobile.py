import re

str = "qnvjltq7777947219gds"
number = re.search("\d{10}",str)
total = number.group()
print(total)