#!/usr/bin/python3
"""
    Python script that, for a given employee ID, returns
    information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    id = sys.argv[1]
    usr_url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    tds_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    user = requests.get(usr_url).json()
    todo = requests.get(tds_url).json()

    completed_nb = 0
    total_nb = 0
    completed_tasks = []

    for task in todo:
        total_nb += 1
        if task.get("completed") is True:
            completed_nb += 1
            completed_tasks.append(task.get("title"))

    sentence = "Employee {} is done with tasks({}/{}):"
    print(sentence.format(user.get("name"), completed_nb, total_nb))
    for task in completed_tasks:
        print("\t {}".format(task))
