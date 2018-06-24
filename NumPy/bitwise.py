import numpy as np

print 'Binary 1 and 3:'
a,b = 1, 3

print np.binary_repr(a, width = 8)
print np.binary_repr(b, width = 8)
print '\n'

print 'Bitwise AND:'
_and = np.bitwise_and(a, b)
print np.binary_repr(_and, width = 8)

print 'Bitwise OR:'
_or = np.bitwise_or(a, b)
print np.binary_repr(_or, width = 8)

print 'Variable a Inverted:'
_inv = np.invert(a)
print np.binary_repr(_inv, width = 8)

print 'Variable a Left Shifted:'
_shifted = np.left_shift(a,5)
print np.binary_repr(_shifted, width = 8)
print _shifted

print 'Variable b Shifted:'
_bshifted = np.right_shift(a,5)
print np.binary_repr(_bshifted, width = 8)
print _bshifted