#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:17:18 2023

@author: student
"""

from collections import Counter as ctr
import matplotlib.pyplot as plt

female_age = [53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42,32,48,23,23]
female_histo = ctr([min((age//10) * 10,100) for age in female_age])
plt.bar([i+5 for i in female_histo.keys()],
        female_histo.values(),color="violet",width=10,edgecolor='black')

plt.xlabel("age groups")
plt.ylabel("female age fequency")
plt.title("Age for female")

plt.savefig("q10female.jpg", dpi=800)
