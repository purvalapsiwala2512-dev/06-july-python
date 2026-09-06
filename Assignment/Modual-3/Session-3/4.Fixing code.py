my_list = [1,2,3]
my_dict = {'a': 1}

try:
    print(my_list[5])
except IndexError:
    print("IndexError:Wrong Position!")

try:
    print(my_dict['b'])
except KeyError:
    print("KeyError:Wrong Key!")