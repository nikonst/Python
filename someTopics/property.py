class Person:
    def __init__(self,name):
        self._name = name

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def deleteName(self):
        del self._name
        print("Object deleted")

    thename = property(getName, setName, deleteName, "Name property")

p = Person("Alexandra")
print(p.thename)
p.thename = "Mary"
print(p.thename)
del p.thename

print("="*10)

class House:
    def __init__(self,address):
        self._address = address

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    @address.deleter
    def address(self):
        del self._address
        print("Object deleted")


h = House("189 Schultz Highway")
print(h.address)
h.address = "87591 Botsford Court"
print(h.address)
del h.address

'''
Output

Alexandra
Mary
Object deleted
==========
189 Schultz Highway
87591 Botsford Court
Object deleted
'''