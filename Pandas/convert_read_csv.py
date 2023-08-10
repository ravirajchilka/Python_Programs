import os
os.system('cls')

import numpy as n
import pandas as pd
from numpy.random import randn

pd.set_option("display.max_rows", 1000)

'''
Manually create data set
data = randn(4,3)
rows = ["aaa","bfdsa","cfdsa","drew"]
cols = ["monday","tuesday","friday"]
df = pd.DataFrame(data,rows,cols)
print(df)
'''

data = {
    'Name': ['John', 'Emily', 'Michael', 'Sophia', 'William', 'Olivia', 'James', 'Ava', 'Ethan', 'Isabella'],
    'Age': [25, 28, 22, 30, 27, 24, 29, 26, 23, 31],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Miami', 'Dallas', 'Boston', 'Seattle', 'San Francisco', 'Austin']
}

df = pd.DataFrame(data)
df.to_csv('sample_data.csv', index=False)

df2 = pd.read_csv("sample_data.csv")
print(df2)

print(df2.loc[[0,4,5]])


