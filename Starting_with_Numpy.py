import numpy as np

##load the library and check its version

print(np.__version__)

##create a list comprising numbers from 0 to 9
L = list(range(10))
print(L)

#converting integers to string - this style of handling lists is known as list comprehension.
S= [str(c) for c in L]
print(S)
