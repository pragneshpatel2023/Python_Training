# ============================================================================
#     Name        : List_Method.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   : Your copyright notice
#     Description : Testing code for python
# ===========list1 = ["abc", 34, True, 40, "male"]

'''============================================================================
    Method	    Description
    append()    Adds an element at the end of the list
    clear()	    Removes all the elements from the list
    copy()      Returns a copy of the list
    count()     Returns the number of elements with the specified value
    extend()    Add the elements of a list (or any iterable), to the end of the current list
    index()	    Returns the index of the first element with the specified value
    insert()    Adds an element at the specified position
    pop()       Removes the element at the specified position
    remove()    Removes the first item with the specified value
    reverse()   Reverses the order of the list
    sort()      Sorts the list
============================================================================'''


print("========================================================")
print("List short explanation ")

cars = ['Ford', 'BMW', 'Volvo']
print(cars)
print("--------------------------------------------------------")

cars.sort()
print("ascending  = ", cars)

cars.sort(reverse=True)
print("Descending  = ",cars)

print("--------------------------------------------------------")



cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
print(cars)
print("--------------------------------------------------------")

def myFunc(e):
  return e['year']

cars.sort(key=myFunc)
print("Key : year = ", cars)


def myFunc2(e):
  return e['car']

cars.sort(key=myFunc2)
print("Key : car = ", cars)

print("========================================================")
print("List reverse explanation ")

fruits = ['apple', 'banana', 'cherry']
print(fruits)

fruits.reverse()
print("Reverse = ", fruits)


print("========================================================")
print("List append explanation ")

fruits = ['apple', 'banana', 'cherry']
print(fruits)

fruits.append("orange")

print("Append 'orang' ",fruits)

print("--------------------------------------------------------")

a = ["apple", "banana", "cherry"]
print("a = ",a)
b = ["Ford", "BMW", "Volvo"]
print("b = ",b)

a.append(b)

print("a Append with B ",a)

print("========================================================")
print("List insert explanation ")

fruits = ['apple', 'banana', 'cherry']
print(fruits)

fruits.insert(1, "orange")
print(fruits)

fruits.insert(3, "Kiwi")
print(fruits)

print("========================================================")
print("List pop explanation ")

fruits = ['apple', 'banana', 'cherry']
print(fruits)

x = fruits.pop(1)
print("fruits =" ,fruits)
print("x =", x)

print("========================================================")
print("List remove explanation ")

fruits = ['apple', 'banana', 'cherry']
print(fruits)

fruits.remove("banana")
print("'banana' Removed = ", fruits)

print("========================================================")