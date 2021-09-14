#!/usr/bin/python3
"""
Retrieve the user and the corresponding done tasks
"""

import requests
from sys import argv
import csv

if __name__ == '__main__':
    task_titel = []
    data = ''
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todo = requests.get(url + "todos", params={"userId": argv[1]}).json()

    completed = []

    for i in todo:
        completed.append([argv[1], user.get('username'), i['completed'], i['title']])
    file = open('{}.csv'.format(argv[1]), 'w')
    with file:
        writer = csv.writer(file)
        writer.writerows(completed)
