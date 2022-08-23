from flask import Flask, request
from datetime import datetime
import json
from db_connector import post_value, get_value, delete_value, put_value
import os
import signal

app = Flask(__name__)
users = {}

#REST API Methods and GW definition
@app.route('/users/<user_id>', methods=['POST', 'GET', 'DELETE', 'PUT'])
#Meta function containing the API methods
def users(user_id):
    if request.method == 'GET':         #Get Method to get the user information by ID
        try:
            get_value(user_id)
            user = get_value(user_id)   #Calling to the function from DB module and and passing the relevant argument
            return {'user_id': user_id, 'user_name': user}, 200
        except:
            return {'status': 'error', 'reason': 'ID already exist'}, 500

    elif request.method == 'POST':      #POST method to create data.
        try:
                                        #getting the json data payload from request
            request_data = request.json
            creation_date = current_time()
                                        #treating request_data as a dictionary to get a specific value from key
            user_name = request_data["user_name"]
            user_id = request_data["user_id"]
            post_value(user_id, user_name, creation_date)   #Required data passed to POST method including timestamp creation
            return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, 200 # status code
        except:
            return {'status': 'error', 'reason': 'ID already exist'}, 500  # status code

    elif request.method == 'PUT':       #PUT method to update Data
        try:
            request_data = request.json
            user_name = request_data["user_id"]
            user_id = request_data["user_id"]
            put_value()                 #Put function in DB module passing permanent variable
            return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, 200  # status code
        except:
            return {'status': 'error', 'reason': 'no such ID'}, 500

    elif request.method == 'DELETE':    # Delete method for value deletion
        try:
            request_data = request.json
            user_name = request_data["user_id"]
            delete_value(user_id)
            return {'user id': user_id, 'user name': user_name, 'status': 'saved'}, 200  # status code
        except:
            return {'status': 'error', 'reason': 'no such ID'}, 500

#Function for timestamp creation
def current_time():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server Stopped'

app.run(host='127.0.0.1', debug=True, port=5000)


