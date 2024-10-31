# ============================================================================
#     Name        : Dictionaries_Methods.py
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
  "colors": ["red", "white", "blue"],
  1:2
}

print("========================================================")

print(thisDict)
print(thisDict['brand'])
print(thisDict['model'])
print(thisDict['year'])
print(thisDict['colors'][0])
print(thisDict['colors'][1])
print(thisDict['colors'][2])
print(thisDict[1])

print("========================================================")

print(thisDict.keys())
print(list(thisDict.keys()))
print(list(thisDict.values()))
print(thisDict.items())  # print key value pairs

UpdateDict = {
  "ownBy" : "Pragnesh Patel",
  "price" : 250000
}

thisDict.update(UpdateDict)
print(thisDict)
print("========================================================")

print(thisDict["ownBy"])
print(thisDict.get("ownBy"))

# This return the error message because "ownBy2" is not present in the dictionary
# print(thisDict["ownBy2"])

# This return the None message because "ownBy2" is not present in the dictionary
# in case of you find the key from the dictionary that is not present in
# the dictionary this ".get" is helpful
print(thisDict.get("ownBy2"))