
class MyException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def checkge(age):
    if age>18:
        print("valid")
    else:
        raise MyException("Invalid age")

    
try:
    checkge(11)
except MyException as e:
    print(e)    