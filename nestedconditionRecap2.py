'''
Author: Ms Rya
Version: 3.10
'''
score = int(input("Enter your score: "))
extra_credit = int(input("Enter extra credit points: "))

total_score = score + extra_credit

if total_score >= 90:
    print("Grade: A")
    if total_score == 100:
        print("Perfect Score!")
elif total_score >= 80:
    print("Grade: B")
elif total_score >= 70:
    print("Grade: C")
elif total_score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

if extra_credit > 0:
    print(f"Extra credit applied: {extra_credit} points")
    print(f'Total score is:{total_score}')
