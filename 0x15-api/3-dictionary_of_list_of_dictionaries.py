#!/usr/bin/python3
"""
Python script that all employees data information in json file
"""

import json
import requests

if __name__ == "__main__":

    user = requests.get("https://jsonplaceholder.typicode.com/users")
    todolist = requests.get("https://jsonplaceholder.typicode.com/todos")
    filename = "todo_all_employees.json"
    tasks = []
    tasksD = {}

    for u in user.json():
        for t in todolist.json():
            if t.get("userId") == u.get("id"):
                tasktodict = {"username": u.get("username"),
                              "task": t.get("title"),
                              "completed": t.get("completed")}
                tasks.append(tasktodict)
        tasksD[u.get("id")] = tasks
    with open(filename, mode="w") as myfile:
        json.dump(tasksD, myfile)
