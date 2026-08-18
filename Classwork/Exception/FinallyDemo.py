def test():
    try:
        k= int(input("Enter number :"))
        return k
    except Exception as e:
        return e
    finally:
        print("Always execute")

print(test())