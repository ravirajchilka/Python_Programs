import os
os.system('cls')

import numpy as n
import pandas as pd
from numpy.random import randn

pd.set_option("display.max_rows", 100)
pd.set_option("display.max_columns", 100)

# Generate random data for the DataFrame
# n.random.seed(42)
data = {
    'Race': ['White', 'Black', 'Asian', 'Hispanic', 'White', 'Black', 'Asian', 'Hispanic', 'White', 'Black'],
    'Population': [197000000, 42900000, 22000000, 63000000, 198000000, 43200000, 22400000, 64800000, 199000000, 43500000],
    'Percentage': [61.1, 13.4, 7.0, 20.3, 61.4, 13.4, 7.1, 20.6, 61.7, 13.5],
    'State': ['California', 'Texas', 'New York', 'Florida', 'California', 'Texas', 'New York', 'Florida', 'California', 'Texas']
}

df = pd.DataFrame(data)
print(df)
print(df["Race"].value_counts())

print(df["Race"].value_counts()["White"])

# Race
# White       3
# Black       3
# Asian       2
# Hispanic    2
# Name: count, dtype: int64
# 3
