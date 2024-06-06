#!/usr/bin/python3
"""
fetch data from
a REST api endpoint"""
import sys
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    param = int(sys.argv[1])
    if type(param) is not int:
        print("error fetching APi")
    else:
        user = requests.get(url + "users/{}".format(param)).json()
        todos = requests.get(url + "todos", params={"UserId": param}).json()

        completed = [t.get("title") for t in todos if t.get("completed")
                     is True]
        print("Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todos)))
        [print("\t {}".format(c)) for c in completed]
