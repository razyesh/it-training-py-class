import csv 

with open("files/stock_data.csv", "r") as mero_file:
    reader = csv.DictReader(mero_file)
    companies = []
    for row in reader:
        if float(row["Percent Change"].split("%")[0]) > 0:
            companies.append(row["Symbol"])


with open("files/names.csv", "a") as mero_file:
    fieldnames = ["name", "email"]
    reader = csv.DictWriter(mero_file, fieldnames=fieldnames)
    # reader.writerow({"name": "hari", "email": "hari@gmail.com"})

