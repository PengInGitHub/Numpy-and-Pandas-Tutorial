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
#list comprehension offers a versatile way to handle list manipulations tasks easily.
S= [str(c) for c in L]
print(S)

print([type(i) for i in L])


#Creating Arrays
#Numpy arrays are homogeneous in nature, i.e., they comprise one data type (integer, float, double, etc.) unlike lists.
print(np.zeros(10,dtype='int'))

#creating a 3 row x 5 column matrix
print(np.ones((3,5),dtype='int'))

#creating a matrix with a predefined value
print(np.full((4,5),1.23))

#create an array with a set sequence
print(np.arange(0,20,4))

#create an array of even space between the given range of values
print(np.linspace(0,1,5))

#create a 3x3 array with mean 0 and standard deviation 1 in a given dimension
print(np.random.normal(0,1,(3,3)))

#create an identity matrix
print(np.eye(3))

#set a random seed
np.random.seed(0)
x1=np.random.randint(10,size=6) #one dimension
print(x1)
x2=np.random.randint(10,size=(3,4)) #one dimension
print(x2)
x3=np.random.randint(10,size=(3,4,5)) #one dimension
print(x3)
print(x3.ndim)
print(x3.shape)
print(x3.size)


#Array Indexing
#The important thing to remember is that indexing in python starts at zero.
x1=np.array([3,2,1,2,4,6,4,32])
print(x1)

#assess value to index zero
print(x1[0])

#assess fifth value
print(x1[4])

#get the last value
print(x1[-1])




