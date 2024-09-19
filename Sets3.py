'''
Author: Ms Rya
Version: 3.10
'''

def copy_set(original_set):
    copied_set = original_set.copy()
    return copied_set

def main():
    original_set = {1, 2, 3}
    print("Original set:", original_set)
    
    copied_set = copy_set(original_set)
    print("Copied set:", copied_set)

main()
