# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 11:09:25 2023

@author: Arman
"""
from collections import defaultdict
from collections import Counter


def main():
    users = [
        {"id": 0, "name": "Hero"},
        {"id": 1, "name": "Dunn"},
        {"id": 2, "name": "Sue"},
        {"id": 3, "name": "Chi"},
        {"id": 4, "name": "Thor"},
        {"id": 5, "name": "Clive"},
        {"id": 6, "name": "Hicks"},
        {"id": 7, "name": "Devin"},
        {"id": 8, "name": "Kate"},
        {"id": 9, "name": "Klein"}
    ]
    
    friendship_pairs = [
        (0, 1),
            (0, 2),
            (1, 2),
            (1, 3),
            (2, 3),
            (3, 4),
            (4, 5),
            (5, 6),
            (5, 7),
            (6, 8),
            (7, 8),
            (8, 9)
    ]
    
    
    
    # dictionary to create list of all friends of a particular person
    
    friendships = defaultdict(list)
    
    for i, j in friendship_pairs:
            friendships[i].append(j)
            friendships[j].append(i)
    
    print("Friendship List : ", friendships)
    print()
    
    
    
    
    # to find total no of connections
    
    def no_of_friends(user):
        list_friends = friendships[user["id"]]
        return len(list_friends)
    
    
    total_connections = sum(no_of_friends(user) for user in users)
    print("Total Connections : ", total_connections)
    print()
    
    # to create list of pairs --> (user_id, no_of_friends)
    
    
    num_friends_by_id = [
         (user['id'], no_of_friends(user)) for user in users
    ]
    num_friends_by_id.sort(  # to arrange in descending order of no of friends
      key=lambda id_friends: id_friends[1], reverse=True
    )
    print("No of Freinds List : ", num_friends_by_id)
    print()
    
    # to create a dictionary  of friends of a friends
    
    def foaf_ids_bad(user):
        user_id = user["id"]
        return [j for i in friendships[user_id] for j in friendships[i]]
        
    foaf = {user['id']: foaf_ids_bad(user) for user in users}
    print("Friend of a Friends : ", foaf)
    print()
    
    # to create a dictionary of count of mutual friends
    
    def friends_of_friends(user):
        return Counter(
                j 
                for i in friendships[user['id']] 
                for j in friendships[i] 
                if j!=user['id'] and j not in friendships[user['id']]
            )
        
    mutual_friend_count = {
        user['id']: friends_of_friends(user) for user in users
        }
    print("Mutual friend count : ",mutual_friend_count)
    print()

if __name__ == '__main__':
    main()
