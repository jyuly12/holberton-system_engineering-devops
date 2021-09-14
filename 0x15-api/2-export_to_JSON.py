#!/usr/bin/python3
"""
This module returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv
import json

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(argv[1])).json()
    todo = get(url + "todos", params={"userId": argv[1]}).json()
    data = []
    with open('{}.json'.format(argv[1]), 'w+') as file:
        for item in todo:
            task = {"task": item.get("title"),
                    "completed": item.get("completed"), "username": user}
            data.append(task)
        info = {argv[1]: data}
        file.write(json.dumps(info))
