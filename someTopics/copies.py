print("EQUALS")
l1 = [1,2,3,4,5]
l2 = l1
print("l1 = ",l1)
print("l2 = ",l2)
print("l1:",id(l1))
print("l2:",id(l2))
l1.append(6)
print("l1 = ",l1)
print("l2 = ",l2)
print("l1:",id(l1))
print("l2:",id(l2))

import copy

#Shallow Copy
print("\nSHALLOW COPY")
l3 = copy.copy(l1)
print("l1 =",l1)
print("l3 =",l3)
print("l1:",id(l1))
print("l3:",id(l3))

l1.append(200)
print("l1 = ",l1)
print("l3 = ",l3)
print("l1:",id(l1))
print("l3:",id(l3))

#but...
l1[1] = 100
print("l1 = ",l1)
print("l3 = ",l3)
print("l1:",id(l1))
print("l3:",id(l3))

#Deep Copy
print("\nDEEP COPY")
l4 = copy.deepcopy(l1)
print(l1)
print(l4)
print(id(l1))
print(id(l4))
l1.append(8)
print(l1)
print(l4)
print(id(l1))
print(id(l4))
