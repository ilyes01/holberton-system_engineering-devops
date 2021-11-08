#!/usr/bin/python3
""" Python script """
import requests
import json
from sys import argv


if __name__ == "__main__":
    employee_id = argv[1]
    user_response = requests.get('https://jsonplaceholder.typicode.com/users/\
' + employee_id).text
    user = json.loads(user_response)

    td_response = requests.get('https://jsonplaceholder.typicode.com/todos?\
userId=' + employee_id).text
    todos = json.loads(td_response)
    completed = 0
    tasks = []
    for a_dict in todos:
        if a_dict['completed'] is True:
            completed += 1
            tasks.append(a_dict['title'])

    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
                                                          completed,
                                                          len(todos)))
    for title in tasks:
        print("\t {}".format(title))
