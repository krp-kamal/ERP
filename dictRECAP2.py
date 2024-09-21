'''
Author: Ms Rya
Version: 3.10
'''
def student_score(scores, student_name):
    if student_name in scores:
        print(f"{student_name}'s score is:", scores[student_name])

student_scores = {'John': 85, 'Emma': 92, 'Sam': 78}

student_score(student_scores, 'Emma')
