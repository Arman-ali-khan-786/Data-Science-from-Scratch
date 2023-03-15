
"""
Created on Wed Mar 15 10:08:22 2023

@author: Arman
"""

# ---------------------- List Comprehension

l1 = [x for x in range(11)]
print(l1)
print()

l2 = [x for x in range(11) if(x%2==0)] 
print(l2)
print()


op = [(i,j) for i in range(1,7) for j in range(1,7)]
print(op)
print()


l3= [ "Even" if(i%2==0) else "Odd" for i in range(11)]
print(l3)
print()
'''
d1={ for j in ["Aman","Himan","Bhatka"]}
print(d1)
print()
'''