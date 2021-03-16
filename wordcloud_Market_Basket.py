# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:33:36 2021

@author: hj
"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import collections

#读取文字
text = open('Market_Basket_Optimisation.csv').read()
#对每种商品数量统计
word_list = list(text.split(','))
word_counts = collections.Counter(word_list) 
#获取Top10商品并显示
word_counts_top10 = word_counts.most_common(10) 
print (word_counts_top10)
#生成词云
wc = WordCloud().generate(text=text)
#显示词云
plt.imshow(wc)
plt.axis('off')
plt.show()



