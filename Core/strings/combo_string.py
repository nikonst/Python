'''
Given 2 strings, a and b, return a string of the form short+long+short,
with the shorter string on the outside and the longer string on the inside.
The strings will not be the same length, but they may be empty (length 0).

combo_string('Hello', 'hi') - 'hiHellohi'
combo_string('hi', 'Hello') - 'hiHellohi'
combo_string('aaa', 'b') - 'baaab'
'''

def combo(s1,s2):
    if len(s1) > len(s2):
        s = s2 + s1 + s2
    else:
        s = s1 + s2 + s1
    return s

s1 = raw_input('Enter the first string > ')
s2 = raw_input('Enter the second string > ')

print combo(s1,s2)
