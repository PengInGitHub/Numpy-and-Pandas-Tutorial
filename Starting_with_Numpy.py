import numpy as np


#Check Version
##load the library and check its version
print(np.__version__)


#Create List 
##create a list comprising numbers from 0 to 9
L = list(range(10))
print(L)


#List Comprehension
#converting integers to string - this style of handling lists is known as list comprehension.
#List comprehension offers a versatile way to handle list manipulations tasks easily.
S= [str(c) for c in L]
print(S)
print([type(i) for i in L])


#Creating Arrays
print(np.zeros(10,dtype='int'))
#creating a 3 row x 5 column matrix
print(np.ones((3,5),dtype='int'))

