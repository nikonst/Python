'''
Given an array of ints length 3, figure out which is larger, the first or last element in the array,
and set all the other elements to be that value. Return the changed array.

max_end3([1, 2, 3]) - [3, 3, 3]
max_end3([11, 5, 9]) - [11, 11, 11]
max_end3([2, 11, 3]) - [3, 3, 3]
'''

def maxEnd3(nums):
    newList = []
    print '***', nums[len(nums)-1]
    if nums[0] >= nums[len(nums)-1]:
        for i in range(0,len(nums)):
            newList.append(nums[0])
    else:
        for i in range(0,len(nums)):
            newList.append(nums[len(nums)-1])
    return newList

list =[]
x = input('Enter list number (0 - Stop) > ')
while x != 0:
    list.append(x)
    x = input('Enter list number (0 - Stop) > ')
print list
list = maxEnd3(list)
print list


