import re
lst = ['ORD55','ORD420','ORD999','ORD101']

for i in lst:
    list = re.match("ORD\d*[02468]$",i)
    if list:
        print(i)
    else:
        pass