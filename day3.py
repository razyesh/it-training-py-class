fruits = ["apple", "banana", "orange"]

# for fruit in fruits:
#     print(fruit)

# [print(fruit) for fruit in fruits if fruit == "apple"]

# for fruit in fruits:
#     if fruit == "banana":
#         pass 
#     else:
#         print("")
#     print(fruit)
# for i in range(1, 10, 2):
#     print(i)

iteration = 1
for i in range(10, 16):
    print(f"Starting iteration {i}")
    if i == 12:
        continue
    elif i == 13:
        # TODO: send_email
        print("Iteration 13 reached")
    elif i == 14:
        break 
    else:
        print(i)

    print(f"Ending iteration {i}")

datas = [1, 100, 200, 500, 214, 234, "918", 00, "abcd", "88", 00]

for data in datas:
    if isinstance(data, int):
        print(data)
    elif data.isdigit():
        print("Digit detected")
        continue 
    else:
        print(f"Oops! {data} is not valid digit")
        break

    