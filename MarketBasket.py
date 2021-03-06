# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 22:35:29 2021

@author: hj
"""

from efficient_apriori import apriori
import pandas as pd
import numpy as np

#读取数据，转为transactions列表
data = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
list1 = data.values.tolist()
transactions = []
for i in list1:
    while np.nan in i:
        i.remove(np.nan)
    transactions.append(set(i))
# 挖掘频繁项集和频繁规则
itemsets, rules = apriori(transactions, min_support=0.05,  min_confidence=0.1)
print("频繁项集：", itemsets)
print("关联规则：", rules)