'''
Return the "centered" average of an array of ints, which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value,
ignore just one copy, and likewise for the largest value. Use int division to produce the final average.
You may assume that the array is length 3 or more.

centered_average([1, 2, 3, 4, 100]) - 3
centered_average([1, 1, 5, 5, 10, 8, 7]) - 5
centered_average([-10, -4, -2, -4, -2, 0]) - -3
'''

import random

def cent_avg(aList):
    return (sum(aList) - min(aList) -  max(aList)) / len(list)

list = []
listSize = random.randint(3,20)
for i in range(0,listSize):
    list.append(random.randint(1,100))
print 'The Size of List is :', listSize
print 'The List : ', list
print 'Centered Averege = ', cent_avg(list)

