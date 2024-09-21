'''
Author: Ms Rya
Version: 3.10
'''
def f1_friends():
    friends = {'Alice', 'Bob', 'Charlie'}
    print("Initial friends list:", friends)

    friends.add('Diana')
    print("Friends list after adding Diana:", friends)

    friends.update({'Eve', 'Frank', 'Grace'})
    print("Friends list after updating with more friends:", friends)

    friends.remove('Charlie')
    print("Friends list after removing Charlie:", friends)

f1_friends()
