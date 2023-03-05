# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 20:01:12 2023

@author: alikh
"""
from collections import defaultdict
from collections import Counter

def main():
    interests = [
(0,"Hadoop"),(0,"Big Data"),(0,"HBase"),(0,"Java"),(0,"Spark"),(0,"Storm"),(0,"Cassandra"),
(1,"NoSQL"),(1,"Cassandra"),(1,"HBase"),(1,"MongoDB"),(1,"Postgres"),
(2, "Python"), (2, "scikit-learn"), (2, "scipy"),(2, "numpy"), (2, "statsmodels"), (2, "pandas"), 
(3, "R"), (3, "Python"),(3, "statistics"), (3, "regression"), (3, "probability"),
(4, "machine learning"), (4, "regression"), (4, "decision trees"),(4, "libsvm"),
(5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),(5, "Haskell"), (5, "programming languages"),
(6, "statistics"),(6, "probability"), (6, "mathematics"), (6, "theory"),
(7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),(7, "neural networks"),
(8, "neural networks"), (8, "deep learning"),(8, "Big Data"), (8, "artificial intelligence"),
(9, "Hadoop"),(9, "Java"), (9, "MapReduce"), (9, "Big Data")

       ]
    
   
    
    # to find list of user_ids for that interest
    '''
    def data_scientists_who_like(target_interest):
        return [
            user_id
            for user_id,user_interest in interests 
            if user_interest == target_interest
            ]
    
    user_ids_by_interest = {
        interest:data_scientists_who_like(interest) 
        for user,interest in interests
        }
    '''
    #>>> or 
    user_ids_by_interest = defaultdict(list)
    for user_id,interest in interests:
        user_ids_by_interest[interest].append(user_id)
    
    print("List of user ids have similar interests : ",user_ids_by_interest)
    print()
    
    # to find the list of interests with that user_id
    
    interests_by_user_id = defaultdict(list)
    for user_id,interest in interests:
        interests_by_user_id[user_id].append(interest)
    print("List of interests of that User_id : ",interests_by_user_id)
    print()
    
    # to find who has most interests in common with a given user
    
    def most_common_interests_with(user):
        return Counter(
            interest_user_id 
            for interest in interests_by_user_id[user]
            for interest_user_id in user_ids_by_interest[interest]
            if interest_user_id!=user
            )
    common_interests_user_id = {
        user: most_common_interests_with(user) for user,interest in interests
        }
    print("User ids of common interests of that user : ",common_interests_user_id)
    print()

if __name__ == '__main__':
    main()