import json

file = open("data.json", "r", encoding = "utf-8")

data = json.load(file)
file.close
print(data)

data["d"] = 4
print(data)

file2 = open("data.json", "w", encoding = "utf-8")
json.dump(data, file2)
file2.close