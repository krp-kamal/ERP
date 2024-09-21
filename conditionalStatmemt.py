'''
Author: Ms Rya
Version: 3.10
'''
def check_special_character(S, special_character):
    if special_character in S:
        return "Special character exists in the string."
    else:
        return "Special character does not exist in the string."

S = '45-=itemA:50$,city1-city2'

special_character = input("Enter a special character: ")

print(check_special_character(S, special_character))
