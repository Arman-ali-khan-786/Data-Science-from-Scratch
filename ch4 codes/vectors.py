#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 10:49:25 2023

@author: student
"""
def vectorAdd(v1,v2):
    assert(len(v1)==len(v2))
    v3=[]
    for i,j in zip(v1,v2):
        v3.append(i+j)
    return v3
def vectorSubtract(v1,v2):
    assert(len(v1)==len(v2))
    v3=[]
    for i,j in zip(v1,v2):
        v3.append(i-j)
    return v3
def main():
    v1= [3,9,7]
    v2= [2,1,6]
    print("Vector Addition : ", vectorAdd(v1,v2))
    print("Vecor Subtraction : ", vectorSubtract(v1,v2))
    
    
if __name__ == '__main__':
    main()
