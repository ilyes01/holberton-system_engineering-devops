#!/usr/bin/python3
"""
script thatreturn information about the employee's todo list progress
"""
import requests
import sys


def fetch_api():
    """ extract data from api """
    user_i = int(sys.argv[1])
    url_info = "https://jsonplaceholder.typicode.com/users/{}/".format(
        user_i)
    response = requests.get(url_info).json()
    user_name = response.get("name")
    url_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_i)
    todos = requests.get(url_todo).json()
    number_completed_todos = 0
    number_of_todos = 0
    # completed_todos = []
    task_list = ""
    for todo in todos:
        number_of_todos += 1
        if todo.get("completed") is True:
            number_completed_todos += 1
            # completed_todos.append(todo["title"])
            task_list += "\t " + todo.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(
        user_name,
        number_completed_todos,
        number_of_todos
        ))
    print(task_list[:-1])

if __name__ == "__main__":
    fetch_api()
