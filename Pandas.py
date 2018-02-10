import pandas as pd

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


#categorize a variable
#create a new column based on the values of another column
data = pd.DataFrame({'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami','corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

#create a new variable
#Firstly create a dictionary to map the known variable values to the unknown feature dict(value:type)
meat_to_animal = {
'bacon': 'pig',
'pulled pork': 'pig',
'pastrami': 'cow',
'corned beef': 'cow',
'honey ham': 'pig',
'nova lox': 'salmon'
}












