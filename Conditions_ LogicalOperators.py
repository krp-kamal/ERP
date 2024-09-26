'''
Author: Ms Rya
Version: 3.10
'''

def my_sleep():
    sleep = int(input("Enter hours of sleep last night: "))
    score = int(input("Enter your productivity score (1-10): "))

    if sleep >= 8 and score >= 5:
        result = "You are well rested and productive."
    elif sleep < 8 and score >= 5:
        result = "You are not well rested, but still productive."
    elif sleep >= 8 and score < 5:
        result = "You are well-rested but not very productive."
    else:
        result = "You are neither well rested nor productive."
    
    print(result)
    return result
    
my_sleep()


