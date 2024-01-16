# While Loop 

num = 31

i = 1
while i <= 20:
    print(f"{num} x {i} = {num * i}")
    i += 1
    # if i == 10:
    #     break
else:
    print("Loop Terminated")

""" Ask the user name and email 
    only if user want to give them like (y/n)
"""

user_detail = []
user_input = input("Do you want to give us your detail(y/n): ")

while user_input == "y":
    name = input("Enter: ")
    user_detail.append(name)
    user_input = input("Do you want to give us your email: ")
else:
    print(user_detail)