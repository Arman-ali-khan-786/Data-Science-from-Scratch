#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 09:22:29 2023

@author: student
"""

import matplotlib.pyplot as plt

# temperature data
max  = [17,19,21,28,33,38,37,37,31,23,19,18]
min = [-62,-59,-56,-46,-32,-18,-9,-13,-25,-46,-52,-58]

# months data
month =['Jan','Feb','Mar','Apr','May','Jun',
        'Jul','Aug','Sept','Oct','Nov','Dec']

# line plot for minimum temperature data
plt.plot(month,min,label="min temp.",marker=">",color='green',
         linestyle='dotted',markerfacecolor="green",markersize=14)

# line plot for maximum temperature data
plt.plot(month,max,label="max temp.",marker="^",color='red',
         linestyle='dashdot',markerfacecolor="red",markersize=14)

# x-axis label
plt.xlabel("Month")

# y-axis label
plt.ylabel("temp(in degree celsius)")

# title of the Plot
plt.title("Min-Max Temp. throughout a year")

plt.legend()

# to save the plot as .jpg
plt.savefig("Min-Max_temp.jpg",dpi=1500)

# to plot the graph
plt.show()