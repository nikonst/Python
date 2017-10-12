'''
When squirrels get together for a party, they like to have cigars.
A squirrel party is successful when the number of cigars is between 40 and 60, inclusive.
Unless it is the weekend, in which case there is no upper bound on the number of cigars.
Return True if the party with the given values is successful, or False otherwise.

cigar_party(30, False) - False
cigar_party(50, False) - True
cigar_party(70, True) - True
'''

def cig_party(cigars,is_weekend):
    if is_weekend == 1 and cigars >= 40:
        return True
    elif is_weekend == 2 and cigars >= 40 and cigars <= 60:
        return True
    else:
        return False

n = input('Enter the number of cigars > ')
w = input('Enter 1 if it\'s weekend and 2 if it\'s not > ')
if (w ==1 or w ==2) and (type(n) == int):
    print cig_party(n,w)
else:
    print 'Ivalid input...'
