def my_division(x,y):
    assert y != 0, "Cant divide by zero"
    return x / y

x = 1
y = 10
print(my_division(x,y))
x = 2
y = 0
print(my_division(x,y))