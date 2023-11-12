from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from central_db import * # Import the SQLAlchemy instance and User model from your previous app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'  # Use the same database as your previous app
db.init_app(app)  # Initialize the database for this app

# Define routes to add/update data in the database (you can add more routes as needed)
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username and password:
        insert_user(username=username, password=password)
        return jsonify({"message": "User added"})
    return jsonify({"message": "Invalid data"})

@app.route('/delete_users', methods=['POST'])
def delete_users():
    data = request.get_json()
    username = data.get('username')
    if username:
        delete_user(username=username)
        return jsonify({"message": "User has been deleted"})
    return jsonify({"message": "Invalid data"})

@app.route('/get_users', methods=['GET'])
def get_users():
    return get_all_users()


#task related functionalities
@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.get_json()
    print(data)
    title = data.get('title')
    description = data.get('description')
    #assigned_to = data.get('assigned_to')
    status = data.get('status')
    due_days = data.get('due_days')
    if title and description:
        insert_task(title=title, description=description,status=status,due_days=due_days)
        return jsonify({"message": "task got added to the que"})
    return jsonify({"message": "Invalid data"})

@app.route('/update_tasks', methods=['POST'])
def update_tasks():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    #assigned_to = data.get('assigned_to')
    status = data.get('status')
    due_days = data.get('due_days')
    if title and description:
        update_task(title,description,status,due_days)
        return jsonify({"message": "task has been update"})
    return jsonify({"message": "Invalid data"})

@app.route('/delete_tasks', methods=['POST'])
def delete_tasks():
    data = request.get_json()
    title = data.get('title')
    if title:
        delete_task(title)
        return jsonify({"message": "task has been DELETED"})
    return jsonify({"message": "Invalid data"})

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    return get_all_tasks()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True,port=5001)
