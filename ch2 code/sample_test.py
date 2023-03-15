
"""
Created on Wed Mar 15 08:17:29 2023

@author: Arman
"""

l1 = ['python',50,'idsup',30,'idb',40,'dbms',70] # to make a list of dictionaries as [{"Subject":subject_name, "Marks":marks},{.....},...] of l1
l2=[]
for i in range(0,len(l1),2):
    lst={}
    lst['subject'] = l1[i]
    lst['marks'] = l1[i+1]
    l2.append(lst)
print(l2)
