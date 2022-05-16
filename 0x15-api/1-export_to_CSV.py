#!/usr/bin/python3
"""
Python script that export employee data information in csv file
"""


import csv
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    todolist = requests.get("https://jsonplaceholder.typicode.com/todos")
    name = user.json().get("username")
    filename = "{}.csv".format(sys.argv[1])

    with open(filename, mode="w") as myfile:
        writer = csv.writer(myfile, delimiter=",", quotechar="'",
                            quoting=csv.QUOTE_ALL, lineterminator="\n")
        for t in todolist.json():
            if t.get("userId") == int(userId):
                writer.writerow([userId, name, str(t.get("completed")),
                                 t.get("title")])
