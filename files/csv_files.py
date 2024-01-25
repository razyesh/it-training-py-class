import csv 

def write_header():
    with open("files/names.csv", "a") as f:
        csv_writer = csv.writer(f, delimiter=",")
        csv_writer.writerow(["name", "email"])

def save_to_csv_file(name, email):
    with open("files/names.csv", "a") as f:
        csv_writer = csv.writer(f, delimiter=",")
        csv_writer.writerow([name, email])

def ask_user_input():
    name = input("Enter name: ")
    email = input("Enter email: ")
    return name, email

# write_header()
# for i in range(5):
#     name, email = ask_user_input()
#     save_to_csv_file(name, email)


def read_csv():
    with open("files/names.csv") as f:
        csv_reader = csv.reader(f, delimiter=",")
        for data in csv_reader:
            print(data)

read_csv()