from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from central_db import *
from adimin_user import *
from user import *
from payment_module import *
import requests


# Initialize the database for this app
app = Flask(__name__)
'''
All user, admin, payment applications will run on diffferent ports.
All the above mentioned application willl be communicated from main, 'App' function, 
thus creating a soc based application following a microservice architecture

ports used:
    App : 5000
    Admin: 5001
    user : 5002
    Payment: 5003
'''

password_update_url = 'http://127.0.0.1:5002/update_password'
initiate_payment_url = 'http://127.0.0.1:5003/initiate_payment'
user_login_url = 'http://127.0.0.1:5002/login'
create_user_url = 'http://127.0.0.1:5001/add_user'
delete_users_url = 'http://127.0.0.1:5001/delete_users'
get_users_url = 'http://127.0.0.1:5001/get_users'
add_task_url = 'http://127.0.0.1:5001/add_task'
update_tasks_url = 'http://127.0.0.1:5001/update_tasks'
delete_tasks_url = 'http://127.0.0.1:5001/delete_tasks'
get_tasks_url = 'http://127.0.0.1:5001/get_tasks'
track_payments_url = 'http://127.0.0.1:5003/track_payments'
update_payment_url = 'http://127.0.0.1:5003/update_payment'

@app.route('/create_user', methods=['POST'])
def create_user():
    # we will get the data from the request sent by Postman
    data = request.get_json()
    # Forward the data to the /add_user route of the other Flask app
    response = requests.post(create_user_url, json=data)
    # Return the response from the other Flask app
    return jsonify(response.json())
# Route to get all users
@app.route('/get_users', methods=['GET'])
def get_users():
    response = requests.get(get_users_url)
    return jsonify(response.json())
# Route to delete users
@app.route('/delete_users', methods=['POST'])
def delete_users():
    data = request.get_json()
    response = requests.post(delete_users_url, json=data)
    return jsonify(response.json())

# Route to add a task
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    response = requests.post(add_task_url, json=data)
    return jsonify(response.json())

# Route to update tasks
@app.route('/update_tasks', methods=['POST'])
def update_tasks():
    data = request.get_json()
    response = requests.post(update_tasks_url, json=data)
    return jsonify(response.json())

# Route to delete tasks
@app.route('/delete_tasks', methods=['POST'])
def delete_tasks():
    data = request.get_json()
    response = requests.post(delete_tasks_url, json=data)
    return jsonify(response.json())

# Route to get all tasks
@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    response = requests.get(get_tasks_url)
    return jsonify(response.json())

##user related urI
@app.route('/update_password', methods=['POST'])
def update_password():
    data = request.get_json()
    response = requests.post(password_update_url, json=data)
    return jsonify(response.json())

@app.route('/user_login', methods=['POST'])
def user_login():
    data = request.get_json()
    response = requests.post(user_login_url, json=data)
    return jsonify(response.json())

@app.route('/get_task', methods=['GET'])
def get_task():
    response = requests.get(get_tasks_url)
    return jsonify(response.json())

##payment related
@app.route('/initiate_payment', methods=['POST'])
def initiate_payment():
    data = request.get_json()
    response = requests.post(initiate_payment_url, json=data)
    return jsonify(response.json())

@app.route('/track_payments', methods=['GET'])
def track_payments():
    response = requests.get(track_payments_url)
    return jsonify(response.json())

@app.route('/update_payment', methods=['POST'])
def update_payment():
    data = request.get_json()
    response = requests.post(update_payment_url, json=data)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True,port=5000)
