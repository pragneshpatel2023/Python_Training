# ============================================================================
#     Name        : Dictionaries_syntax.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   :
#     Description : Testing code for python
# ============================================================================

thisDict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,  # This value is overridden because Duplicates Not Allowed
  "year": 2020,
  "colors": ["red", "white", "blue"]
}

print("========================================================")

print(thisDict)
print(thisDict['brand'])
print(thisDict['model'])
print(thisDict['year'])
print(thisDict['colors'][0])
print(thisDict['colors'][1])
print(thisDict['colors'][2])

print("========================================================")

#  Change value

print(thisDict)

thisDict['year'] = 2021
thisDict['model'] = 'Suzuki'

print(thisDict)

print(thisDict['year'])
print(thisDict['model'])

print("========================================================")
