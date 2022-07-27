import string
import pandas as pd
import math
from github import Github
import os
from pprint import pprint
import requests
import csv


df1 = pd.read_csv('MainDataset.csv')
df2 = pd.read_csv('MainDataset2.csv')
df3 = pd.read_csv('MainDataset3.csv')
df4 = pd.read_csv('MainDataset4.csv')
df5 = pd.read_csv('MainDataset5.csv')

out = df1.append(df2)
out = out.append(df3)
out = out.append(df4)
out = out.append(df5)

with open('FinalDataset.csv', 'w', encoding='utf-8') as f:
    out.to_csv(f, index=False)