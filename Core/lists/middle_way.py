'''
Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

middle_way([1, 2, 3], [4, 5, 6]) - [2, 5]
middle_way([7, 7, 7], [3, 8, 0]) - [7, 8]
middle_way([5, 2, 9], [1, 4, 5]) - [2, 4]
'''
import random

def mid_way(a,b):
    newList = []
    mid = len(a)/2
    newList+=[a[mid],b[mid]]
    return newList


l1 = []
l2 = []

for i in range(0,10):
    l1.append(random.randint(0, 100))
    l2.append(random.randint(0, 100))

print l1
print l2
newList = mid_way(l1,l2)
print newList


