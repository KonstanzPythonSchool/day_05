#!/usr/bin/env python
"""
Test the REST API
"""

import requests
import json

# server address
server = 'http://127.0.0.1:5000'


class ApiError(Exception):
    """An API Error Exception"""

    def __init__(self, status):
        self.status = status

    def __str__(self):
        return self.status


def get_user(name):
    # type: (str) -> dict
    """
    Function to get the user

    Parameters
    ----------
    name : str
        Username

    Returns
    -------
    user : dict
        Returns the requested user.

    Examples
    --------
    >>> get_user("Elvin")
    {'age': 32, 'name': 'Elvin', 'occupation': 'Doctor'}
    """

    resp = requests.get("{}/user/{}".format(server,name))

    # check response
    if resp.status_code != 200:
        # This means something went wrong.
        raise ApiError('GET /user/ {}'.format(resp.status_code))

    return resp.json()


def create_user(name, age, occupation):
    """
    Function to post a new user.

    Parameters
    ----------
    name : str
        Name of the user.
    age : int
        Age of the user.
    occupation : str
        Occupation of the user.

    Returns
    -------
    message : str

    request_status : int
         HTTP response status code.
            `400` "User already exists"
            `201` "Created User `name`"

    Examples
    --------
    >>> create_user(name = "micha", age= 28, occupation = 'PhD Student')
    "Created User micha", 201
    """

    # create a user
    user = dict(
        name = name,
        age = age,
        occupation = occupation,
    )

    # post it (as shortcut)
    resp = requests.post("{}/user/{}".format(server,name), json=user)

    if resp.status_code == 400:
        return "User already exists", resp.status_code
    elif resp.status_code == 201:
        return "Created User {}".format(name), resp.status_code
    else:
        raise ApiError("Some unexpected ERROR code: {}".format(resp.status_code))

# def update_user(name, age, occupation):

if __name__ == '__main__':
    create_user("micha",27,'PhD Student')