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
