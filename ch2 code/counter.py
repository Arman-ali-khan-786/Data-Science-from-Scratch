
"""
Created on Wed Mar 15 09:13:49 2023

@author: Arman
"""
from collections import Counter as ct # Counter is a class in collections


 
    # Values that are by default False
''' 
    False
    None
    -0
    0
    0.0
    ""
    []
    {}
    set()
    tuple()
'''

def main():
    s = "ababcdeeda"
    d1 = ct(s)   # keys can be of any type but values are of integer type
    print(d1)   # sorts in descending order a/c to the values
    print(type(d1)) # it is of collections.Counter Class
    for i,j in d1.items():
        print(i,j)
        
    print()
    l1 = [1,2,1,2,3,4,6,1,7,2,3,7,8,5,2,4]
    d2 = ct(l1)
    print(d2)    
   

if __name__ == '__main__':
    main()