'''
Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6
and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

sum67([1, 2, 2]) - 5
sum67([1, 2, 2, 6, 99, 99, 7]) - 5
sum67([1, 1, 6, 7, 2]) - 4
'''

import random

def s67(aList):
    return sum(aList[:aList.index(6)]) + sum(aList[aList.index(7)+1:])
    
def testTheIndices(aList):
    print 'Number 6 is at index: ',aList.index(6)
    print 'Number 7 is at index: ',aList.index(7)
    print 'The number needed to be sumed are : '
    print aList[:aList.index(6)]
    print aList[aList.index(7)+1:]

lists = [[2,4,1,5,6,8,9,7,8,9],
         [6,4,5,7,9,9,9],
         [4,5,6,9,9,8,7,3,4,5,3]]

random_index= random.randint(0,2)
list_to_test = lists[random_index] # Pick a random list to check
print 'The list is : ',list_to_test
testTheIndices(list_to_test)
print 'Sum = ',s67(list_to_test)
