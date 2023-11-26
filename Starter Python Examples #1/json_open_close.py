import json

file = open("data.json", "r", encoding = "utf-8")

data = json.load(file)
print(data.keys())
print(data["a"])

file.close