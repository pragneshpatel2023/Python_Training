# ============================================================================
#     Name        : Student_Number.py
#     Author      : Pragnesh Patel
#     Version     :
#     Copyright   : Your copyright notice
#     Description : Testing code for python
# ============================================================================


SF1 = int(input("Enter Numbers of student 1 "))
SF2 = int(input("Enter Numbers of student 2 "))
SF3 = int(input("Enter Numbers of student 3 "))
SF4 = int(input("Enter Numbers of student 4 "))
SF5 = int(input("Enter Numbers of student 5 "))

StudentNumberList = [SF1, SF2, SF3, SF4, SF5]

print(StudentNumberList)

StudentNumberList.sort()

print("Student Numbers in ascending Order: ", StudentNumberList)
