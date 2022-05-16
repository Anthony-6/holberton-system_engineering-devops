#!/usr/bin/python3
"""
Python script that all employees data information in json file
"""

import json
import requests

if __name__ == "__main__":

    user = requests.get("https://jsonplaceholder.typicode.com/users")
    todolist = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasksL = []
    tasksD = {}

    for u in user.json():
        for t in todolist.json():
            if t.get("userId") == u.get("id"):
                tasktodict = {"username": u.get("username"),
                              "task": t.get("title"),
                              "completed": t.get("completed")}
                tasksL.append(tasktodict)
        tasksD[u.get("id")] = tasksL
    with open("todo_all_employees.json", mode="w") as myfile:
        json.dump(tasksD, myfile)
