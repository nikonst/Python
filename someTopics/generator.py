def aGen(power):
    for i in range(power):
        yield 2**i

print(aGen(4))

for item in aGen(5):
    print(item)

print("*"*10)

def bGen():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

    n += 1
    yield n

for item in bGen():
    print(item)

'''Output
<generator object aGen at 0x0000024E53461DB0>
1
2
4
8
16
**********
1
2
3
4

'''