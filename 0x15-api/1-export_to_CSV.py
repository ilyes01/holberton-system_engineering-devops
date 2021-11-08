#!/usr/bin/python3
"""Export data.
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    # Checks the argument
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    # Main formatted
    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.csv'.format(emp_id=emp_id)

    # User Response
    res = requests.get(user_uri).json()

    # Username of the employee
    username = res.get('username')

    # User TODO Response
    res = requests.get(todo_uri).json()

    # Create the new file
    # Filename example: `{user_id}.csv`
    with open(filename, 'w', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)

        for elem in res:
            # Completed or non-completed task
            status = elem.get('completed')

            # name of the task
            title = elem.get('title')

            # Writing results
            writer.writerow([emp_id, username, status, title])
