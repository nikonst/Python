'''
Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
The string length will be at least 2.

extra_end('Hello') - 'lololo'
extra_end('ab')  - 'ababab'
extra_end('Hi') - 'HiHiHi'
'''

def ex_end(s):
    if len(s) >= 2:
        return 3 * str[-2:]
    else:
        return 'Imvalid String, Sorry...'

str = raw_input('Enter a string > ')

print ex_end(str)