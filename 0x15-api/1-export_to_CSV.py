#!/usr/bin/python3
"""
Python script that export employee data information in csv file
"""

import requests
import sys
import csv
if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
    todolist = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    name = user.json().get('name')
    filename = userId + '.csv'

    with open(filename, mode="w", newline='') as myfile:
        writer = csv.writer(myfile, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for t in todolist.json():
            if t.get('userId') == int(userId):
                writer.writerow([userId, name, t.get('completed'),
                                 t.get('title')])
