#!/usr/bin/python3
''' Python script that all employees data information in json file '''
if __name__ == "__main__":

    import requests
    import sys
    import json

    user = requests.get(f'https://jsonplaceholder.typicode.com/users')
    todolist = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    filename = 'todo_all_employees.json'
    tasks = []
    tasksD = {}

    for u in user.json():
        for t in todolist.json():
            if t.get('userId') == u.get('id'):
                tasktodict = {"task": t.get('title'),
                              "completed": t.get('completed'),
                              "username": u.get('username')}
                tasks.append(tasktodict)
        tasksD[u.get('id')] = tasks
    with open(filename, mode='w') as myfile:
        json.dump(tasksD, myfile)
