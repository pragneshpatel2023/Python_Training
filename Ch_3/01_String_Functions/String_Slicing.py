# ============================================================================
#     Name        : String_Slicing.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   : Your copyright notice
#     Description : Testing code for python
# ============================================================================

str1 = " My mane "
str2 = "Pragnesh"

print("========================================================")
print("Add two strings")
print (str1)
print (str2)
print (str1 + str2)  # Attached two string together.
print (str2 + str1)  # Attached two string together.


String1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabc"

print("========================================================")
# Printing 3rd to 12th character
print("Slicing characters from 3-12: ")
print(String1)
print(String1[3:12])

print("========================================================")
# Printing characters between
# 3rd and 2nd last character
print("Slicing characters between " +
      "3rd and 2nd last character: ")
print(String1)
print(String1[3:-2])

print("========================================================")
print("Print every second character start form 2 ")
print(String1)
print(String1[2::2])

print("========================================================")

