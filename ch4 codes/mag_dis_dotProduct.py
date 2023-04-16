#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 08:10:43 2023

@author: student
"""
import math
def dot_product(v1,v2):
    assert(len(v1) == len(v2))
    return sum([x*y for x,y in zip(v1,v2)])

def get_magnitude(v):
    return int(math.sqrt(dot_product(v,v)))

def sub(v1,v2):
    return [j-i for i,j in zip(v1,v2)]

def get_distance(v1,v2):
    assert(len(v1) == len(v2))
    return round(math.sqrt(dot_product(sub(v1,v2), sub(v1,v2))),2)

def main():
    v1=[2,3,7]
    v2=[5,7,1]
    dotProduct = dot_product(v1, v2)
    print(dotProduct)
    v1_mag = get_magnitude(v1)
    v2_mag = get_magnitude(v2)
    print("Magnitude of v1 : ",v1_mag)
    print("Magnitude of v2 : ",v2_mag)
    distance = get_distance(v1, v2)
    print("Distance between vectors are : ",distance)
    
if __name__ == '__main__':
    main()