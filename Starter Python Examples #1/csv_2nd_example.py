import csv

file = open("data.csv", "w", encoding = "utf-8", newline ="")

writer = csv.writer(file)

writer.writerow(["mesto", "broj"])
writer.writerow(["Begec", "21411"])
writer.writerow(["Novi Sad", "21000"])

file.close