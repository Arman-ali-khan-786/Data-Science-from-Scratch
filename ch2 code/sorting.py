"""
Created on Wed Mar 15 09:59:09 2023

@author: Arman
"""

# ------------------------------ Sorting

'''
 -> obj.sort() : it changes the original object on which it is applied
 syntax : object.sort()

'''

l1 = [ 5,1,3,2,0,-1]
l1.sort()
print(l1)
print()


'''
 -> sorted(obj) : it does not changes the original object on which
                 it is applied
 syntax : sorted(obj)
         var = sorted(obj)

'''

l2 = [ 5,1,3,2,0,-1]
y = sorted(l2)
print(y) 
print(l2)


