import json
"""
file = open("podaci2.json", "w", encoding = "utf-8")

recnik = {"nikola":"pancevo", "milos":"aleksinac"}
json.dump(recnik, file)

file.close
"""
file2 = open("podaci2.json", "r", encoding = "utf-8")

podaci = json.load(file2)
print(podaci["nikola"])

file2.close