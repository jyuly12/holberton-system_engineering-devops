#!/usr/bin/python3
"""
This module returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": argv[1]}).json()
    completed = []

    for task in todos:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed), len(todos)))
    print("\n".join("\t {}".format(task) for task in completed))