a = 1

a = "its"

# to get the unique roll numbers


list_of_students = [
    {"name": "Ab", "roll_no": 1, "age": 12}, 
    {"name": "Cd", "roll_no": 1, "age": 12}, 
    {"name": "Ef", "roll_no": 1, "age": 12}, 
    {"name": "Ab", "roll_no": 1, "age": 12}
]

one_student = {"name": "Ab", "roll_no": 1, "age": 12}

roll_numbers = set()

# for student in list_of_students:
#     for key, value in student.items():
#         if key == "roll_no":
#             roll_numbers.add(value)

print(len(roll_numbers))
print(len(list_of_students))




