'''
Author: Ms Rya
Version: 3.10
'''

def find_colour_index(colours, colour):
    index_number = colours.index(colour)
    return index_number
  
colours = ["red", "blue", "green", "yellow"]
index_number = find_colour_index(colours, "blue")
print(colours)
print(f"The first 'blue' is at index: {index_number}")
