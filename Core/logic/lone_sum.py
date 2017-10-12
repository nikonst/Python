'''
Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values,
it does not count towards the sum.

lone_sum(1, 2, 3) - 6
lone_sum(3, 2, 3) - 2
lone_sum(3, 3, 3) - 0
'''

import random

def lon_sum(aList):
    if aList[0] == aList[1]:
        s = aList[2]
    elif aList[0] == aList[2]:
        s = aList[1]
    elif aList[1] == aList[2]:
        s = aList[0]
    elif aList[0] == aList[1] and aList[0] == aList[2]:
        s = 0
    else:
        s = sum(aList)
    return s

list = []
for i in range(0,3):
    list.append(random.randint(1,10))

print 'The list is : ', list
print 'The Lone Sum is : ',lon_sum(list)


