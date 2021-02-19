# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 10:40:28 2021

@author: HuangJie3
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame(columns = ['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
i = 0
url1 = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-'
url2 = '.shtml'
for a in range(1,3):
    url = url1+str(a)+url2
    data = requests.get(url)
    content = data.text
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    temp = soup.find('div',class_='tslb_b')
    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list = tr.find_all('td')
        if len(td_list) >0:
            id, brand, car_model, type, desc, problem, datetime, status = td_list[0].text,td_list[1].text,\
                td_list[2].text,td_list[3].text,td_list[4].text,td_list[5].text,td_list[6].text,td_list[7].text
            df.loc[i,'id'] = id
            df.loc[i,'brand'] = brand
            df.loc[i,'car_model'] = car_model
            df.loc[i,'type'] = type
            df.loc[i,'desc'] = desc
            df.loc[i,'problem'] = problem
            df.loc[i,'datetime'] = datetime
            df.loc[i,'status'] = status
            i +=1
print(df)
df.to_csv("car_complain.csv",encoding='gbk',index=False)
          