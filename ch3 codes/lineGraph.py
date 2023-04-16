#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 08:10:01 2023

@author: student
"""
import matplotlib.pyplot as plt


X=[0,1,2,5,4]
Y = [1,1,3,1,5]
X1 = [0.5,1,1.5,2,2.5]
Y1 = [1,2,3,4,5]
'''
plt.plot(X,Y)
plt.show()


plt.plot(X,Y,color="red")  # to change the color of the line to Red

plt.plot(X,Y,color="orange",marker="^") # to make a upper triangle at points
plt.plot(X,Y,color="green",marker=".") # to make a upper triangle at points
'''
# .plot(X,Y) -> to mark the coordinates for ploting a graph
# .show() -> to show the plot or draw the graph
# color='' -> to change the color of line in the plot 
# markersize -> to change the size of the marker
# makeredgecolor -> to chnage the marker edge color
# makerfacecolor -> to change the color of the marker excluding the edge color
#linestyle -> to change the line style i.e dotted,dashdot etc....
#label -> inside plt.plot() to label the different line graphs

plt.plot(X,Y,color="orange",marker="^", markersize=10,markeredgecolor="red",
         markerfacecolor="blue",linestyle="dotted",
         label='stock1') # also linestyle="dashdot"

plt.xlabel("X-axis") # to label x-axis
plt.ylabel("Y-axis") # to label y-axis
plt.title("Visualization through Line Graph") # to add title to graph plotted


plt.plot(X1,Y1, color="red",linestyle="dashdot",label="Stock2") 

# using this command it will show the labels of the lines plotted
plt.legend(loc=8) # loc -> to change the location of the line label i.e legend
# dpi = value  --> to increase or decrease the quality of the saved plot 
# format : .savefig("filename.format") --> format can be jpg,jpeg,pdf
plt.savefig("lineGraph.jpg",dpi=500)  # to save the graph plotted as jpg 
plt.show()


