#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:40:36 2023

@author: student
"""

import matplotlib.pyplot as plt
import math

x =[x for x in range(-10,11)]
xsinx= [(i*math.sin(i)) for i in x]
x2sinx = [((math.pow(i, 2))*math.sin(i)) for i in x]
x3sinx = [(math.pow(i, 3)*math.sin(i)) for i in x]
x4sinx = [(math.pow(i, 4)*math.sin(i)) for i in x]
print(x,x2sinx)

# for xsin(x)
plt.plot(x,xsinx,color="red")
plt.plot(x,x2sinx,color="blue")
plt.plot(x,x3sinx,color="orange")
plt.plot(x,x4sinx,color="green")
plt.xlabel("x values")
plt.ylabel("value's")
plt.title("xsinx ,x^3sinx & x^4sinx plot")
plt.legend(xsinx, loc = 8)
plt.savefig("q9.jpg", dpi=800)
plt.show()