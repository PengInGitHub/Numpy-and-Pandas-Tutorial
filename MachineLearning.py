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

