# ============================================================================
#     Name        : Tuple_Methodss.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   : Your copyright notice
#     Description : Testing code for python
# ============================================================================

'''============================================================================
  Method	  Description
  count()	  Returns the number of times a specified value occurs in a tuple
  index()	  Searches the tuple for a specified value and returns the position of where it was found
============================================================================'''

print("========================================================")
print("Tuple .count example ")
thisTuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thisTuple)

x = thisTuple.count(5)
print(x)

print("========================================================")
print("Tuple .index example ")

thisTuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(thisTuple)

x = thisTuple.index(8)
print("index of 8 = ", x)
print("========================================================")