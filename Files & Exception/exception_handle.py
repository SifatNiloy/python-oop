def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Can not divide by zero")
print(div(10,2))
print(div(3,0))
print(div(9,3))