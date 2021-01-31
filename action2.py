# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 23:39:38 2021

@author: hj
"""

import pandas as pd

data = {'语文':[68, 95, 98, 90,80], '数学':[65, 76, 86, 88, 90], '英语':[30, 98, 88, 77, 90]}
a = list(data.keys())
df = pd.DataFrame(data,index=['张飞','关羽','刘备','典韦','许褚'], columns=a)
for i in a:
    print(i+'最低分'+str(df[i].min()))
    print(i+'最高分'+str(df[i].max()))
    print(i+'成绩方差'+str(df[i].var()))
    print(i+'成绩标准差'+str(df[i].std()))
    print(i+'平均分'+str(df[i].mean()))
df['total'] = df.sum(axis=1)
print(df.sort_values(by='total',ascending=False))   