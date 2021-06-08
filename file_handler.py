# import json, os, csv
import csv

# data = open("data.txt","w")

# # print(data.read())

# data_txt = data.write("name = afista \nhobbies = coding")

# print(data_txt)

# print(data.readlines())

# data.close()

data = open("data.json", 'a')

# json_view = json.load(data)

new_json = {
    "name" : "afista",
    "age" : 20,
    "address" : "jember",
    "hobbies" : "coding",
    "class" : "impact byte"
}

# # print(json_view)

# print(json_view['age'])
# print(type(json_view['age']))

# json.dump(new_json, data)

data.close()

# os.remove("data2.txt")

users = open("user.csv", "a")

header = ['first_name', 'last_name', 'age']

data_csv = csv.DictWriter(users, fieldnames=header)

# data_csv = csv.reader(users, delimiter=",")

new_data = {
    "first_name" : "agus",
    "last_name" : "udin",
    "age" : 40,
}

# print(data_csv)

data_csv.writerow(new_data)

# for row in data_csv:
#     print(row)

users.close()