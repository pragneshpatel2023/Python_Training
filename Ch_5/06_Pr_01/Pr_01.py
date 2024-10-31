# ============================================================================
#     Name        : Pr_01.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   :
#     Description : Testing code for python
# ============================================================================

print("========================================================")

thisDict = {
  "papa": "Father",
  "vastu": "Item",
  "thala": "Bag",
  "hitman": "Rohit Sharma"
}

print("Options are ", thisDict.keys())
a = input("Enter your word : \n")
print("Mending of your word is :", thisDict.get(a))
print("========================================================")