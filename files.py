f1 = open("data.txt", mode="a")
f1.write("\nText is appended")
f1.writelines(["Added", "open"])
f1.close()

# output = f1.read()
# output = f1.readline()
f1 = open("data.txt")
output = f1.read()
f1.close()

with open("data.txt") as f:
    f.read()



name = input("Enter your name: ")

with open("names.txt", "a") as f:
    f.write(f"\n{name}")

try:
    with open("names2.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Please create the file first")