# ============================================================================
#     Name        : Input.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   :
#     Description : Testing code for python
# ============================================================================


# Taking string input from keyboard

print("========================================================")
name = input("Enter your name - ")
city = input("Enter city name - ")

print ("Hello My name is", name)
print ("I am from ", city)


# Taking Numeric input

print("========================================================")
w = input("Enter width : ")
width = int(w)

h = input("Enter height : ")
height = int(h)

w = int(w)

h = int(h)

area = w*h

print ("Area of rectangle = ", area)

# Convert Numeric input for float values

print("========================================================")
amount = float(input("Enter Amount : "))
rate = float(input("Enter rate of interest : "))

interest = amount*rate/100
print ("Amount: ", amount, "Interest: ", interest)
