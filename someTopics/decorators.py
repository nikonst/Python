def starWrapper(somefun):
    def innerFun(*args, **kwargs):
        print("I star decorate")
        somefun(*args, **kwargs)
        print("*"*10)
    return innerFun

def dashWrapper(somefun):
    def innerFun(*args, **kwargs):
        print("I dash decorate")
        somefun(*args, **kwargs)
        print("-"*10)
    return innerFun

@starWrapper
def secondPower(x):
    print(x**2)

secondPower(2)

@dashWrapper
def thirdPower(x):
    print(x**3)

thirdPower(2)

@dashWrapper
@starWrapper
def fourthPower(x):
    print(x**4)

fourthPower(2)

'''
Output

I star decorate
4
**********
I dash decorate
8
----------
I dash decorate
I star decorate
16
**********
----------
'''