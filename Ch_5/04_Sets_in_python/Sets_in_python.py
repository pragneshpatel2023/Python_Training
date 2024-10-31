# ============================================================================
#     Name        : Sets_in_python.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   :
#     Description : Testing code for python
# ============================================================================

print("========================================================")

# Creating a set
a = {1, 3, 4, 5, 1}
print(type(a))
print(a)

print("========================================================")

# Impotent : this syntax creates an empty dictionary not an empty set.
a = {}
print(type(a))
print("========================================================")

print("========================================================")

# Created an empty set
b = set()
print(type(b))

b.add(1)
b.add(3)
b.add(5)
b.add(5)
b.add(5)
print(b)
print("========================================================")