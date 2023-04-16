#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:53:01 2023

@author: student
"""
from matplotlib import pyplot as plt

friends = [70,65,72,63,71,64,60,64,67]
minutes = [175,170,205,120,220,130,105,145,190]
labels = ['a','b','c','d','e','f','g','h','i']

plt.scatter(friends, minutes, color="red", marker=".")
plt.xlabel("friends")
plt.ylabel("no of minutes spend")
plt.title("Time spend with friends")
for label,x,y in list(zip(labels,friends,minutes)):
    plt.annotate(label, xy=(x,y), xytext=(8,-6), textcoords="offset points")
plt.show()
