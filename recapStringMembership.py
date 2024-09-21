'''
Author: Ms Rya
Version: 3.10
'''
def check_membership(text):
    python_present = "Python" in text
    java_present = "Java" in text
    fun_not_present = "fun" not in text

    return python_present, java_present, fun_not_present

text = "string membership operator"

python, java, fun = check_membership(text)

print("Is 'Python' present in text?", python)
print("Is 'Java' present in text?", java)
print("Is 'fun' not present in text?", fun)
