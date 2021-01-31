# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 23:49:28 2021

@author: hj
"""
import pandas as pd

result = pd.DataFrame()
data = pd.read_csv('E:/python作业/car_complain.csv',encoding="gbk")
data.replace({'一汽-大众':'一汽大众'})
#这里替换名称好像没成功
for i in range(600):
    problems = str(data['problem'][i])
    problems_list = problems.split(',')
    problems_list.pop()
    for j in problems_list:
        data.loc[i,j] = 1
data = data.fillna(0)
data['id'] = str(data['id'] )
brandproblem = data.groupby(['brand']).sum()
# 这里对所有问题数量求和还不太理解，会带上id一起求和，暂时用str（id）处理
carmodel = data['car_model'].groupby(data['brand']).nunique()
result['brandproblemtotal'] = brandproblem.sum(axis=1)
result['carmodeltotal'] = carmodel
result['problem_per_model'] = result['brandproblemtotal']/result['carmodeltotal']
print(result)
print('平均车型投诉最多的品牌是：'+str(result['problem_per_model'].idxmax()))