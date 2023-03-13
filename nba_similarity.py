# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:53:24 2020

@author: Andrew 
"""
#FInsa archetype for the most efficient players in NBA history
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv('player_info.csv')

df["player_weight"] = df["player_weight"].round()
df["player_height"] = df["player_height"].round()

corrlst = []
for h in df:
    if df.dtypes[h] == 'float64':
        corrlst.append(h)
statcorr = df[corrlst].corr()

sns.heatmap(statcorr, annot=True)
plt.show()