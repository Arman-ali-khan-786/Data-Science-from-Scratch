#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:56:36 2023

@author: student
"""
from collections import Counter as ctr
import matplotlib.pyplot as plt

male_age =[53,51,71,31,33,39,52,27,54,30,64,26,21,54,52,20,59,32]
female_age = [53,65,68,21,75,46,24,63,61,24,49,41,39,40,25,54,42,32,48,23,23]
male_histo = ctr([min((age//10) * 10,100) for age in male_age])
female_histo = ctr([min((age//10) * 10,100) for age in female_age])

plt.bar([i+5 for i in male_histo.keys()],
        male_histo.values(),color="yellow",width=10,edgecolor='black')
#plt.bar([i+6 for i in female_histo.keys()],female_histo.values(),color="violet",width=5)

plt.xlabel("age groups")
plt.ylabel(" male age fequency")
plt.title("Age for male")
plt.savefig("q10male.jpg", dpi=800)
