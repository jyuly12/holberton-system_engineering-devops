#!/usr/bin/python3
"""
Retrieve the user and the corresponding done tasks
"""

from requests import get
from sys import argv
import csv

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    user = get(url + "users/{}".format(argv[1])).json()
    todo = get(url + "todos", params={"userId": argv[1]}).json()

    with open('{}.csv'.format(argv[1]), 'w+') as file:
        for todo in todo:
            info = '"{}","{}","{}","{}"\n'.format(
                argv[1], user.get('username'), todo.get('completed'),
                todo.get('title'))
            file.write(info)
