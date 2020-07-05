# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 20:24:32 2020

@author: M&K
"""

import scrapper as sc
import pandas as pd

df = sc.get_jobs("data scientist",1000 ,False)
df.to_csv('glassdoor_jobs.csv',index = False)
