# if else 
# list_of_student = ["Ram", "Shyam"]

# if isinstance(list_of_student, list):
#     print("The type is lists")
# elif isinstance(list_of_student, tuple):
#     print("The type is tuple")
# else:
#     print("I dont know")


# # append new student 
# list_of_student.append("Hari") if len(list_of_student) < 3 else print("Length of student did not match")
# print(list_of_student)


# take string as an input from user and get the number of vowel letter from it
a = input("Enter a character: ")
# if a in <vowels> print(True) else False
vowels = ["a", "e", "i", "o", "u"]

counts = vowels.count(a)
if counts > 0:
    print(True)
else:
    print(False)

vowel_count = 0 
non_vowel_count = 0
if a in vowels:
    vowel_count = vowel_count + 1
else:
    non_vowel_count = non_vowel_count + 1

if a not in vowels:
    print(False)
else:
    print(True)

print(True) if a in vowels else False 


# 
