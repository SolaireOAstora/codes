import numpy as np 
import pandas as pd 

# create a pandas dataframe

# arr = np.array([['Zhang',60,90], 
#     ['Li',80,70],['Wang',100,50]])

# arr = dict({'name':['Zhang','Li','Wang'],
#     'math':[60,80,100],'english':[90,70,50]})

# print(arr)

# df = pd.DataFrame(arr,index = [1,2,3], 
#     columns = ['name','math','english'])


df = pd.read_csv('./data.csv')

df.index = [1,2,3]

df['total'] = df.math + df.english

print(df)