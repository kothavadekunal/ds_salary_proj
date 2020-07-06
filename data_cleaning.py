# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 16:15:23 2020

@author: M&K
"""

import pandas as pd

df = pd.read_csv('glassdoor_jobs.csv')

df = df[df['Salary Estimate'] != '-1']

salary = df['Salary Estimate'].apply(lambda x: x.split("(")[0])

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided' in x.lower() else 0)

minusDK = salary.apply(lambda x: x.replace('$',"").replace('K',""))

minushr = minusDK.apply(lambda x: x.lower().replace("per hour","").replace("employer provided salary:",""))

df['minSal'] = minushr.apply(lambda x: int(x.split('-')[0]))

df['maxSal'] = minushr.apply(lambda x: int(x.split('-')[1]))

df['avgSal'] = (df.minSal + df.maxSal) / 2

df['Company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3] , axis = 1)

df['State'] = df['Location'].apply(lambda x: x.split(',')[1])
df.State.value_counts()

df['age'] = df['Founded'].apply(lambda x: x if x<0 else 2020- x)

df.columns

df_out = df.drop(['Unnamed: 0'] , axis = 1)
