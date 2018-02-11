import numpy as np
import pandas as pd

#data set from UCI Machine Learning Repository
#https://s3-ap-southeast-1.amazonaws.com/he-public-data/datafiles19cdaf8.zip

#load data
train=pd.read_csv("train.csv")
test=pd.read_csv("test.csv")

#check data
train.info()
print(train.shape)#(32561, 15)
print(test.shape)#(16281, 15)

#have a glimpse of the data set
train.head()

#check missing values
#how many rows have missing values
nans=train.shape[0]-train.dropna().shape[0]
nans/len(train)#7% rows have missing values in train

nans=test.shape[0]-test.dropna().shape[0]
nans/len(test)#7% rows have missing values in test

#check which columns have missing values.
train.isnull().sum()#only 3 columns have missing values

#count the unique values from each categorical variables
cat=train.select_dtypes(include=['O'])#object
cat.apply(pd.Series.nunique)
