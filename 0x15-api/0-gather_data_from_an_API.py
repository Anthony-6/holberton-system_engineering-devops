#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""


import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
    todolist = requests.get(f'https://jsonplaceholder.typicode.com/todos')

    name = user.json().get('name')
    doneTask = 0
    totalTask = 0

    for t in todolist.json():
        if t.get('userId') == int(userId):
            totalTask += 1
            if t.get('completed'):
                doneTask += 1

    print(f'Employee {name} is done with tasks({doneTask}/{totalTask}):')
    for t in todolist.json():
        if t.get('userId') == int(userId) and t.get('completed'):
            print("\t {}".format(t.get('title')))
