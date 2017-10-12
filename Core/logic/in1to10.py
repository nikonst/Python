'''
Given a number n, return True if n is in the range 1..10, inclusive.
Unless outside_mode is True, in which case return True if the number is less or equal to 1,
or greater or equal to 10.

in1to10(5, False) - True
in1to10(11, False) - False
in1to10(11, True) - True
'''

def in1to10(n, outside_mode):
    if outside_mode == False:
        if n>=1 and n<=10:
            result = True
        else:
            result = False
    else:
        if n>1 and n<10:
            result = False
        else:
            result = True
    return result

n = input('Enter an integer > ')
mode = input('Enter outside mode (1- True, 2- False) > ')
if type(n) == int and (mode == 1 or mode ==2):
    if mode == 1:
        mode = True
    else:
        mode = False
    print in1to10(n,mode)
else:
    print('Invalid input...')


