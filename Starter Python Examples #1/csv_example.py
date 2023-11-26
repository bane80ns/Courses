import csv

file = open("bane.csv", "r", encoding = "utf-8")

reader = csv.reader(file)
#print(list(reader))

for i in reader:
    print(i)

file.close