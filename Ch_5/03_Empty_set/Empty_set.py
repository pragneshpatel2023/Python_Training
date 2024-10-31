# ============================================================================
#     Name        : Empty_set.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   :
#     Description : Testing code for python
# ============================================================================

print("========================================================")
a = {}
print(type(a))

# An empty set can be created using below syntax.
b = set()
print(type(b))

b.add(4)
b.add(5)
b.add(5)
b.add(5)
b.add(5)
b.add('Pragnesh')
b.add((4, 5, 6)) # Added a tuple


print(b)

print("========================================================")

