# ============================================================================
#     Name        : Tuples.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   :
#     Description : Testing code for python
# ============================================================================



print("========================================================")
print("Tuple Simple example ")
thisTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thisTuple)

print("========================================================")
print("Tuple Create Tuple With One Item ")

thisTuple = ("apple",)
print(type(thisTuple))

#NOT a tuple
thisTuple = ("apple")
print(type(thisTuple))

print("========================================================")
print("Tuple with multiple data types ")

tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)

print("========================================================")
print("Tuple Access ")

thisTuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thisTuple)

print(thisTuple[2:])

print("========================================================")
print("Tuple Check if Item Exists ")

thisTuple = ("apple", "banana", "cherry")
print(thisTuple)

if "apple" in thisTuple:
  print("Yes, 'apple' is in the fruits tuple")

print("========================================================")
print("Change Tuple Values ")

x = ("apple", "banana", "cherry")
print(x)

y = list(x)
y[1] = "kiwi"

x = tuple(y)
print(x)

print("========================================================")
print("Unpacking a Tuple ")

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
print(fruits)

(*green, tropic, red) = fruits

print(green)
print(tropic)
print(red)
print("========================================================")