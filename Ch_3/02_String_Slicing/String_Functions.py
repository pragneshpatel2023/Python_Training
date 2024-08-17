# ============================================================================
#     Name        : String_Functions.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   : Your copyright notice
#     Description : Testing code for python
# ============================================================================


'''============================================================================
Method            Description
capitalize()      Converts the first character to upper case
casefold()        Converts string into lower case
center()          Returns a centered string
count()           Returns the number of times a specified value occurs in a string
encode()          Returns an encoded version of the string
endswith()        Returns true if the string ends with the specified value
expandtabs()      Sets the tab size of the string
find()            Searches the string for a specified value and returns the position of where it was found
format()          Formats specified values in a string
format_map()      Formats specified values in a string
index()           Searches the string for a specified value and returns the position of where it was found
isalnum()         Returns True if all characters in the string are alphanumeric
isalpha()         Returns True if all characters in the string are in the alphabet
isascii()         Returns True if all characters in the string are ascii characters
isdecimal()       Returns True if all characters in the string are decimals
isdigit()         Returns True if all characters in the string are digits
isidentifier()    Returns True if the string is an identifier
islower()         Returns True if all characters in the string are lower case
isnumeric()       Returns True if all characters in the string are numeric
isprintable()     Returns True if all characters in the string are printable
isspace()         Returns True if all characters in the string are whitespaces
istitle()         Returns True if the string follows the rules of a title
isupper()         Returns True if all characters in the string are upper case
join()            Converts the elements of an iterable into a string
ljust()           Returns a left justified version of the string
lower()           Converts a string into lower case
lstrip()          Returns a left trim version of the string
maketrans()       Returns a translation table to be used in translations
partition()       Returns a tuple where the string is parted into three parts
replace()         Returns a string where a specified value is replaced with a specified value
rfind()           Searches the string for a specified value and returns the last position of where it was found
rindex()          Searches the string for a specified value and returns the last position of where it was found
rjust()           Returns a right justified version of the string
rpartition()      Returns a tuple where the string is parted into three parts
rsplit()          Splits the string at the specified separator, and returns a list
rstrip()          Returns a right trim version of the string
split()           Splits the string at the specified separator, and returns a list
splitlines()      Splits the string at line breaks and returns a list
startswith()      Returns true if the string starts with the specified value
strip()           Returns a trimmed version of the string
swapcase()        Swaps cases, lower case becomes upper case and vice versa
title()           Converts the first character of each word to upper case
translate()       Returns a translated string
upper()           Converts a string into upper case
zfill()           Fills the string with a specified number of 0 values at the beginning

============================================================================'''
str1 = " My mane "
str2 = "Pragnesh"

print("========================================================")
print("Get string length")
print (str1)
print (str2)
print (len(str1))  # Calculate string length.
print (len(str2))  # Calculate string length.

print("========================================================")
print('Check ".endswith"')
txt = "Hello, welcome to my world."

x = txt.endswith("my world.")
print(x)

x = txt.endswith("Hello", 0, 5)
print(x)

x = txt.endswith("my world")
print(x)

print("========================================================")
print('Check ".count"')

txt = "I love apples, apple are my favorite fruit"
print(txt)

x = txt.count("apple")
print("'apple' word in string ", x)

x = txt.count("apple", 0, 15)
print("'apple' word 0 to 15 characters of the string ", x)

x = txt.count("a")
print("'a' character in string", x)

x = txt.count("f")
print("'f' character in string", x)

print("========================================================")
print('Check ".capitalize"')

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)

print("========================================================")
print('Check ".find"')

txt = "Hello, welcome to my world."
print(txt)

x = txt.find("e")
print("Finds 'e' in string ", x)

x = txt.find("e", 5, 10)
print("Finds 'e' between 5 to 10 characters in string", x)

x = txt.find("welcome")
print("Finds 'welcome' in ths string ", x)

print("Finds 'q' in string ", txt.find("q"))

print("========================================================")
print('Check ".replace"')

txt = "one one was a race horse, two two was one too."
print(txt)

x = txt.replace("one", "three")
print('replace "one" with "three" = ', x)

x = txt.replace("one", "three", 2)
print('replace "one" with "three" with two times = ', x)

print("========================================================")