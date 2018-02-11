import numpy as np
import pandas as pd
from sklearn import preprocessing

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


#input missing values by mode

#Workclass
train.workclass.value_counts(sort=True)
train.workclass.fillna(' Private',inplace=True)

#Occuation
train.occupation.value_counts(sort=True)
train.occupation.fillna(' Prof-specialty',inplace=True)

#Native Country
train['native.country'].value_counts(sort=True)
train['native.country'].fillna(' United-States',inplace=True)

#check target vairable distrobution
train.target.value_counts()/train.shape[0]#76% is under 50k

#create cross tab of target variable with critical variable
pd.crosstab(train.education,train.target,margins=True)/train.shape[0]

#encode categorical variablesvia sklearn.preprocessing
for x in train.columns:
    if train[x].dtype == 'object':
        lbl=preprocessing.LabelEncoder()
        lbl.fit(list(train[x].values))
        train[x]=lbl.transform(list(train[x].values))
#all the variables have been converted to numeric, including the target variable


#Building a Random Forest Model        






















