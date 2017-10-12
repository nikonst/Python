'''
Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array.
Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

big_diff([10, 3, 5, 6]) - 7
big_diff([7, 2, 10, 9]) - 8
big_diff([2, 10, 7, 2]) - 8
'''
import random

def b_diff(nums):
    if len(nums) == 1:
        diff = nums[0]
    else:
        diff = max(nums) - min(nums)
    return diff

theList = []

listSize = random.randint(1,20)

for i in range(0,listSize):
    theList.append(random.randint(0, 100))
print 'Size of list ', listSize,' The List : ',theList
print 'Big Difference: ',b_diff(theList)