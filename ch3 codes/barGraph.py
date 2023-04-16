#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 10:07:21 2023

@author: student
"""

import matplotlib.pyplot as plt

def main():
    
    # for Bar graph use plt.bar() method
    # dta
    X=[1,2,3,4,5]
    X=[i-0.5 for i in X]
    Y=[5,6,4,7,1]
    plt.bar(X,Y,color=['red','blue','yellow','green','orange'], 
            width=1,linestyle='dotted', #bottom=-1,
            edgecolor="black")
    plt.savefig("barGraph.jpg")
    plt.show()
    
    
    
if __name__ == '__main__':
    main()
