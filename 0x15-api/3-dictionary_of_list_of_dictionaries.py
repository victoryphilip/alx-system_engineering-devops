#!/usr/bin/python3
"""
    Python script that, exports data in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":
    usr_url = "https://jsonplaceholder.typicode.com/users/"
    users = requests.get(usr_url).json()

    data = {}

    for user in users:
        id = user.get("id")
        url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
        todos = requests.get(url).json()

        tasks = []
        for t in todos:
            tasks.append({"task": t.get("title"),
                          "completed": t.get("completed"),
                          "username": user.get("username")})
        data["{}".format(id)] = tasks

    with open('todo_all_employees.json', 'w') as f:
        json.dump({int(x): data[x] for x in data.keys()}, f, sort_keys=True)
