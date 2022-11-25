'''Tuples are immutable. This means that elements of a tuple cannot be changed once it has been assigned.'''

a = ['S', 'a', 't', 'i', 's', 'h']  # List
a[0] = 'c'
print(a)

b = ('s', 'k', 's')  # tuple
b[0] = 'n'
print(b)

s = "iamsks"  # string
s[0] = 'C'  # cannot be added => string doesn't support.
