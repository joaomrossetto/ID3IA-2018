import pandas as pd 
import numpy as np

adults = pd.read_csv('adult.data.txt', sep=r'\s*,\s*', na_values="?", engine='python', names = ['age',
'workclass',
'fnlwgt',
'education',
'education-num',
'marital-status',
'occupation',
'relationship',
'race',
'sex',
'capital-gain',
'capital-loss',
'hours-per-week',
'native-country',
'50k-year'])

adults.dropna(how='any',inplace = True)
print adults

#print(adults.isnull().sum())
