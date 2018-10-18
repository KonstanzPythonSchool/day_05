#!/usr/bin/env python
"""
REST API with Python
"""

# ToDo: License
# source: https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
# gist : https://gist.github.com/leon-sleepinglion/97bfd34132394e23ca5905ec730f776a

from flask import Flask
from flask_restful  import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

users = [
    {
        'name' : 'Nicholas',
        'age' : 42,
        'occupation' : 'Network Engineer'
    },
    {
        'name' : "Elvin",
        'age' : 32,
        'occupation' : 'Doctor'
    },
    {
        'name' : "Jass",
        'age' : 22,
        'occupation' : 'Web Developer'
    },
]

class User(Resource):

    def get(self, name):
        """
        The `get` method is used to retrieve a particular user details by specifying the name.

        We will traverse through our users list to search for the user,
        if the name specified matched with one of the user in users list,
        we will return the user,
        along with `200` OK, else return a user not found message with `404` Not Found.
        Another characteristic of a well designed REST API is that it uses standard HTTP response
        status code to indicate whether a request is being processed successfully or not.

        Parameters
        ----------
        name : str
            name of the User to search for.

        Returns
        -------
        user : dict or str
            returns `user` or "User not found"
        response_status : int
            HTTP response status code. `200` if found and ok. `404` if not found
        """

        for user in users:
            if name == user['name']:
                return user, 200
        return "User not found", 404

    def post(self, name):
        """
        The `post` method is used to create a new user.

        We will create a parser by using reqparse we imported earlier,
        add the age and occupation arguments to the parser,
        then store the parsed arguments in a variable,
        args (the arguments will come from request body in the form of form-data, JSON or XML).
        If a user with same name already exists,
        the API will return a message along with `400` Bad Request,
        else we will create the user by appending it to users list
        and return the user along with `201` Created.

        Parameters
        ----------
        name : str
             name of the User to search for.

        Returns
        -------
        user : dict or str
            returns `user` or "User with name `name` already exists."
        response_status : int
            HTTP response status code.
                `201` if created.
                `400` if user already exists.
        """

        # create a parser for the request
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')
        args = parser.parse_args()

        # check if user exists
        for user in users:
            if name == user['name']:
                return "User with name {} already exists".format(name), 400

        # create a new user
        user = {
            'name' : name,
            'age' : args['age'],
            'occupation' : args['occupation']
        }

        # add it to the list
        users.append(user)
        return user, 201

    def put(self, name):
        """
        The `put` method is used to update details of user, or create a new one if it is not existed yet.

        If the user already exist,
        we will update his/her details with the parsed arguments
        and return the user along with `200` OK,
        else we will create and return the user along with `201` Created.

        Parameters
        ----------
        name : str
             name of the User to search for.

        Returns
        -------
        user : dict
            returns `user`
        response_status : int
            HTTP response status code.
                `200` if OK.
                `201` if created.
        """

        # create a parser for the request
        parser = reqparse.RequestParser()
        parser.add_argument('age')
        parser.add_argument('occupation')
        args = parser.parse_args()

        # check if user exists then update it
        for user in users:
            if name == user['name']:
                user['age'] = args['age']
                user['occupation'] = args['occupation']
                return user, 200

        # create a new user
        user = {
            'name': name,
            'age': args['age'],
            'occupation': args['occupation']
        }

        # add it to the list
        users.append(user)
        return user, 201

    def delete(self, name):
        """
        The `delete` method is used to delete user that is no longer relevant.

        By specifying users as a variable in global scope,
        we update the users list using list comprehension to create
        a list without the name specified (simulating delete),
        then return a message along with `200` OK.

        Parameters
        ----------
        name

        Returns
        -------
        message : str
            Deletion message: "`name` is deleted."
        response_status : int
            HTTP response status code. `200`
        """
        global users
        users = [users for user in users if user['name'] != name]
        return "{} is deleted.".format(name), 200


api.add_resource(User, '/user/<string:name>')

class Users(Resource):
    def get(self):
        """
        Get all user names.

        Returns
        -------
        users : list
            Get a list of all user
        """

        return json.dumps(sorted([user['name'] for user in users])), 200

    def delete(self):
        """
        Delete all users
        Returns
        -------

        """
        global users
        users = []

        return "All users are deleted.", 200

api.add_resource(Users, '/user/')

app.run(debug=True)

###################################################################
# Expose it to the outside word (will use your ip)
# That is a security issue for development servers !
# Checkout 'deploying' if you want to do it in a proper way!
#
# app.run(debug=True, host='0.0.0.0')
