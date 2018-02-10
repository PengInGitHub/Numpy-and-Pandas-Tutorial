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
x2=np.random.randint(10, size=(3,4)) #two dimension
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

#get the second last value
print(x1[-2])

#in a multidimensional array, we need to specify row and column index
#1st row and 2nd column value
print("x2",x2)
print("1st row and 2nd column value: ",x2[2,3])

#3rd row and last value from the 3rd column
print("3rd row and last value from the 3rd column: ",x2[2,-1])

#replace value at 0,0 index
x2[0,0]=122
print("replace value at 0,0 index ",x2)


#Array Slicing
#access multiple or a range of elements from an array.

x=np.arange(10)
#from start to 4th position
print(x[:5])

#from 4th position to end
print(x[4:])

#from 4th to 6th position
print(x[4:7])

#return elements at even place
print(x[::2])

#return elements from first position step by two
print(x[1::2])

#reverse the array
print(x[::-1])


#Array Concatenation
#combine different arrays
#concatenate two or more arrays at once.
x=np.array([1,2,3])
y=[3,22,1]
z=np.array([34,89,9])
print(np.concatenate([x,y,z]))

#use np.concatenate to create 2-dimensional arrays.
grid=np.array([[1,2,3],[4,5,6]])
print(np.concatenate([grid,grid]))

#define row-wise or column-wise matrix via axis parameter
print(np.concatenate([grid,grid],axis=1))

#np.vstack
print(np.vstack([x,grid]))

#np.hstack
z=np.array([[3],[4]])
print(np.hstack([grid,z]))


