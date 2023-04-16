# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 09:40:55 2023

@author: Arman
"""

#import matplotlib.pyplot as plt

from collections import Counter

def cal_mean(ds):
    return sum(ds)/len(ds)

def get_mode(ds):
    return [i for i,j in Counter(ds).items() if(j==max(Counter(ds).values()))]

def get_median(ds):
    if(len(ds) %2!=0):
        return ds[len(ds)//2]
    else:
        return (ds[len(ds)//2] + ds[(len(ds)//2) -1])/2
    

def get_quantile(ds,m):
    #print(ds)
    return [ds[int(m*len(ds))],int(m*len(ds))]
    
num_friends = [
    100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,
               13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,
               9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,
               7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,
               6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,
               4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,
               2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
               1,1,1,1,1,1,1,1
               ]
'''
f = Counter(num_friends)
plt.bar(f.keys(),f.values(),color='pink')
plt.show()
'''

mean = cal_mean(num_friends)
# median is the center of the dataset i.e divides it in 50-50 % 
median = get_median(sorted(num_friends[:]))
# mode is the elements having maximum repitations in a dataset
mode = get_mode(num_friends)
# Quantile(m) divides the dataset in m% and (100-m)%
# index of quantile --> m% of length of the dataset
quantile = get_quantile(sorted(num_friends[:]),0.1)
print("Mean : ",mean)
print("Median : ",median)
print("Mode : ",mode)
print("Quantile 10% : ",quantile)
