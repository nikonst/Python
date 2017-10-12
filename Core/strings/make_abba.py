'''
Given two strings, a and b, return the result of putting them together in the order abba,
e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') - 'HiByeByeHi'
make_abba('Yo', 'Alice') - 'YoAliceAliceYo'
make_abba('What', 'Up') - 'WhatUpUpWhat'
'''

def abba(s1,s2):
    return s1 + 2*s2 + s1


s1 = raw_input('Enter String 1 > ')
s2 = raw_input('Enter String 2 > ')
print abba(s1,s2)

