# def before(or_fun):
#     def execute():
#         print("before function calling...")
#         or_fun()
#     return execute 


# def after(or_fun):
#     def execute():
#         or_fun()
#         print("after function calling...")
#     return execute

# @before
# @after
# def test():
#     print("Test Calling")

# test()


# def add(or_fun):
#     def execute(*a):
#         or_fun(*a)
#         sum=0
#         for i in a:
#             sum+=i
#         print(sum)
#     return execute



# def mul(or_fun):
#     def execute(*a):
#         or_fun(*a)
#         sum=1
#         for i in a:
#             sum*=i
#         print(sum)
#     return execute



# @mul
# def calc(*a):
#     print("***calc***")

# calc(10,20,30)


def digit(or_fun):
    def execute(data):
        if str(data).isdigit():
            or_fun
        else:
            print("invalid data")    

    
@digit
def get(data):
    print(data)

get(123)