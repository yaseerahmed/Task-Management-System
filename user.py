from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from central_db import * # Import the SQLAlchemy instance and User model from your previous app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'  # Use the same database as your previous app
db.init_app(app)  # Initialize the database for this app


@app.route('/update_password', methods=['POST'])
def update_password():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        update_user_password(username,password)
        return jsonify({"message": "task has been update"})
    return jsonify({"message": "Invalid data"})

# Define routes to add/update data in the database (you can add more routes as needed)
@app.route('/login', methods=['POST'])
def user_login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        user_logins(username,password)
        return jsonify({"message": "Login Successfull"})
    return jsonify({"message": "Please verify your credentials"})

@app.route('/update_tasks', methods=['POST'])
def update_tasks():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    assigned_to = data.get('assigned_to')
    status = data.get('status')
    due_days = data.get('due_days')
    if title and description:
        update_task(title,description,status,due_days)
        return jsonify({"message": "task has been update"})
    return jsonify({"message": "Invalid data"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True,port=5002)