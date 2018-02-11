import pandas as pd
import numpy as np

data = pd.DataFrame({'Country': ['Russia','Colombia','Chile','Equador','Nigeria'],
                    'Rank':[121,40,100,130,11]})

#quick analysis of data
#describe() method computes summary statistics of integer / double variables
data.describe()

#get the complete information about the data set
data.info()

#add new data
data = pd.DataFrame({'group':['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],'ounces':[4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

#sort the data frame by ounces
data.sort_values(by='ounces',ascending=True,inplace=False)


#get ride of duplicate rows
#remove duplicates based on matching row values across all columns.
data = pd.DataFrame({'k1':['one']*3 + ['two']*4, 'k2':[3,2,1,3,3,4,4]})
data.sort_values(by='k2')
data.drop_duplicates()

#remove duplicates based on a particular column
data.drop_duplicates(subset='k1')


#Create A New Variable
#categorize a variable
#create a new column based on the values of another column
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

#Alternative 1: dict, map
#Firstly create a dictionary to map the known variable values to the unknown feature dict(value:type)
meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}

#Then use map function to map the dictionary's values to the keys
data['animal'] = data['food'].map(str.lower).map(meat_to_animal)

#Alternative 2: lambda, self-defined method, apply
#alternative: use lambda and apply
lower=lambda x:x.lower()
data['food']=data['food'].apply(lower)

def meat_2_animal(series):
    if series['food']=='bacon':
        return 'pig'
    elif series['food']=='pulled pork':
        return 'pig'
    elif series['food']=='pastrami':
        return 'cow'
    elif series['food']=='corned beef':
        return 'cow'
    elif series['food']=='honey ham':
        return 'pig'
    else:
        return 'salmon'

data['animal2']=data.apply(meat_2_animal,axis='columns')

#Alternative 3: assign function
data.assign(new_variable=data['ounces']*10)


#remove variable
data.drop('animal2',axis='columns',inplace=True)


#imput missing values
#series function from pandas are used to create arrays
data=pd.Series([1,-222,32,932,32,43,-23])

#replace 932 with NaN values
#np.nan is NaN
data.replace(932,np.nan,inplace=True)

#replace multiple at once
data.replace([1,-222,-23],np.nan,inplace=True)



#rename column names and axis (row names).
data=pd.DataFrame(np.arange(12).reshape(3,4),index=['Ohio','Coorado','New York'],columns=['One','Two','Three','Four'])

#Using rename function
data.rename(columns={'One':'One_p'},inplace=True)
data.rename(index={'Ohio':'SanF'},inplace=True)


#use string functions
data.rename(index=str.upper,columns=str.title,inplace=True)



