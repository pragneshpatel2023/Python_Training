# ============================================================================
#     Name        : Sets_Methods.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   :
#     Description : Testing code for python
# ============================================================================

print("========================================================")

# Creating a set
a = {1, 3, 4, 5, 1, 6, 7, 8, 9}
print(type(a))
print(a)

# len method in set.
b = len(a)
print(b)
print("========================================================")

# remove method in set.
a.remove(4)
print(a)
print("========================================================")

# pop method in set.
a.pop()
print(a)
print("========================================================")

# union method in set.
c = {8, 10, 11}
c = a.union(c)
print('a =', a)
print('C =', c)
print("========================================================")

# intersection method in set.
c = a.intersection({3, 5, 6})
print('a =', a)
print('C =', c)
print("========================================================")

# clear method in set.
a.clear()
print(a)
print("========================================================")