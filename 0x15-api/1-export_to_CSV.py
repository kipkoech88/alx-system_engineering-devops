#!/usr/bin/python3
"""
export data in csv
The tasks"""

from requests import get
from sys import argv

headers = {
    "Content-Type": "application/json"
    }
base_url = "https://jsonplaceholder.typicode.com/users/"


def export_to_csv(user_id: str) -> None:
    """
    Get the task status for a certain user and save 'em
    Args:
        user_id (str): The user id of the user
    """
    # lets first get the name of Employee
    emp_name = get("{}{}".format(base_url, user_id)).json().get("username")
    full_url = "{}{}/todos/".format(base_url, user_id)
    response = get(full_url, headers=headers).json()
    # save the tasks that belong to this user to a csv file
    file_name = "{}.csv".format(user_id)
    with open(file_name, "w", encoding="utf-8") as csv_file:
        for resp in response:
            csv_file.write('"{}","{}","{}","{}"\n'
                           .format(resp.get("userId"),
                                   emp_name, resp.get("completed"),
                                   resp.get("title")))


if __name__ == "__main__":
    export_to_csv(argv[1])
