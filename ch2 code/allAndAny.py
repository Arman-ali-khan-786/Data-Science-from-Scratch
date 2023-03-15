
"""
Created on Wed Mar 15 09:30:46 2023

@author: Arman
"""


'''
-> all : it works on logical 'and', if any of the element is false it will return 
False

'''
print(all([1,2,4]))  #true
print(all([1,'a',3])) # true
print(all([{},2,3]))  #false 
print(all([]))  # returns true

print()

'''
-> any : it works on logical 'or', if any of the element is true it will return 
False

'''

print(any([1,2,4])) # true
print(any([1,'a',3])) # true
print(any([{},2,3])) # true
print(any([]))  # return false