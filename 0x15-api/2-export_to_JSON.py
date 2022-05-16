#!/usr/bin/python3
''' Python script that export employee data information in json file '''
if __name__ == "__main__":

    import requests
    import sys
    import json

    userId = sys.argv[1]
    user = requests.get(f'https://jsonplaceholder.typicode.com/users/{userId}')
    todolist = requests.get(f'https://jsonplaceholder.typicode.com/todos')
    name = user.json().get('name')
    filename = userId + '.json'
    tasks = []
    tasksD = {}

    for t in todolist.json():
        if t.get('userId') == int(userId):
            tasktodict = {"task": t.get('title'),
                          "completed": t.get('completed'),
                          "username": user.json().get('username')}
            tasks.append(tasktodict)
    tasksD[userId] = tasks
    with open(filename, mode='w') as myfile:
        json.dump(tasksD, myfile)
