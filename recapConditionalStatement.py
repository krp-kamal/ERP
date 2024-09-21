'''
Author: Ms Rya
Version: 3.10
'''
def check_discount_eligibility(age, is_member):
    if age > 60 or is_member.lower() == "yes":
        return "You are eligible for a discount."
    else:
        return "You are not eligible for a discount."

age = int(input("Enter your age: "))
is_member = input("Are you a member? (yes/no): ")

result = check_discount_eligibility(age, is_member)
print(result)
