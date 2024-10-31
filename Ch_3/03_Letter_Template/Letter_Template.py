# ============================================================================
#     Name        : Letter_Template.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   :
#     Description : Testing code for python
# ============================================================================

letterTemplate = '''Dear  <|NAME|>
You are selected
<|DATE|>'''

print(letterTemplate)

Name = input('Enter Name ')
Date = input('Enter Date ')

letterTemplate = letterTemplate.replace('<|NAME|>', Name)
letterTemplate = letterTemplate.replace('<|DATE|>', Date)

print("************************************************")

print(letterTemplate)

print("************************************************")