#!/usr/bin/python3
"""
This module returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    task_titel = []
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(argv[1])).json()
    todo = get(url + "todos", params={"userId": argv[1]}).json()

    for task in todo:
        if task.get('completed') is True:
            task_titel.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(task_titel), len(todo)))
    for i in task_titel:
        print("\t {}".format(i))
