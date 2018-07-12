def aClosure(n):
    def addFunction(x):
        return n + x
    return addFunction

a = aClosure(5)
print(a(3))
print(a(4))
print(a(5))

'''
Output

8
9
10
'''