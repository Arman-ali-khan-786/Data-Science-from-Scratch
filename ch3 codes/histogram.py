#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 08:09:02 2023

@author: Arman
"""
from matplotlib import pyplot as plt
from collections import Counter
grades=[83,95,91,87,70,0,85,82,100,67,73,77,0]

histo = Counter([min((ele//10 )* 10,100) for ele in grades])
print(histo)

plt.bar([i+5 for i in histo.keys()], histo.values(),width=10,
        color=['purple','magenta','violet','black','orange','blue'])
plt.xlabel("grades range")
plt.ylabel("frequency")
plt.title("Histogram of Grade")
plt.savefig("Grades_and_frequencies.jpg",dpi=800)
#  plt.axis([x_start,x_end,y_start,y_end])
plt.axis([0,110,0,4])
plt.show()
