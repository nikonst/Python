'''
Given a string, return a version without the first and last char, so "Hello" yields "ell".
The string length will be at least 2.

without_end('Hello') - 'ell'
without_end('java') - 'av'
without_end('coding') - 'odin'
'''

def no_end(word):
    return word[1:len(word)-1]

s = raw_input('Enter a string > ')
print no_end(s)