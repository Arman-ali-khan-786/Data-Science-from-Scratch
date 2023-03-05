# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:54:31 2023

@author: Arman
"""

from collections import defaultdict

def main():
    salaries_and_tenures = [
        (83000, 8.7), (88000, 8.1),
        (48000, 0.7), (76000, 6),
        (69000, 6.5), (76000, 7.5),
        (60000, 2.5), (83000, 10),
        (48000, 1.9), (63000, 4.2)
        ]
    
    # to bucket the tenures
    
    def tenure_bucket(tenure):
        if tenure < 2 :
            return "less than 2"
        elif tenure < 5 :
            return "between 2 and  5"
        else : 
            return "more than five"
    # to group the salaries corresponding to each bucket
    
    salary_by_tenure_bucket = defaultdict(list)
    
    for sal,ten in salaries_and_tenures:
        bucket = tenure_bucket(ten)
        salary_by_tenure_bucket[bucket].append(sal)
    print("List of salary corresponding to tenure : ",salary_by_tenure_bucket)
    print()
    
    # find average salary for that bucket
    
    average_salary_by_bucket = {
        tenure_bucket: sum(sal)/len(sal)
        for tenure_bucket,sal in salary_by_tenure_bucket.items()
        }
    print("Average salary corresponding to that bucket tenure : ",average_salary_by_bucket)
    print()
    
if __name__ == '__main__':
    main()
