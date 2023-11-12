from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
###this is a centralized db, which is used for all apps, user,payment and also for admin
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'  # SQLite database
db = SQLAlchemy(app)

class users(db.Model):
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))

class Task(db.Model):
    title = db.Column(db.String(100), nullable=False, primary_key=True)
    description = db.Column(db.String(200))
    #assigned_to = db.Column(db.String(50))
    status = db.Column(db.String)
    due_days = db.Column(db.Integer)

class pay(db.Model):
    task = db.Column(db.String(50), primary_key=True)
    amount = db.Column(db.String(50))
    status = db.Column(db.String(50))

# Function to initiate a payment
def initiate_pay(task,amount):
    pay1 = pay(task=task, amount=amount)
    db.session.add(pay1)
    db.session.commit()
    return pay.task

# Function to insert a new user
def insert_user(username, password):
    user = users(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return user.username

# Function to update a user's password
def update_user_password(username, new_password):
    user = user.query.get(username)
    if user:
        user.password = new_password
        db.session.commit()
        return True
    return False

# Function to delete a user
def delete_user(username):
    user = users.query.get(username)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False


# Function to insert a new task
def insert_task(title, description, status, due_days):
    task = Task(title=title, description=description, status=status, due_days=due_days)
    db.session.add(task)
    db.session.commit()
    return task.title

# Function to update a task's information
def update_task(title, new_description,new_status, new_due_days):
    task = Task.query.get(title)
    if task:
        task.description = new_description
        #task.assigned_to = assigned_to
        task.status = new_status
        task.due_days = new_due_days
        db.session.commit()
        return True
    return False

# Function to delete a task
def delete_task(title):
    task = Task.query.get(title)
    if task:
        db.session.delete(task)
        db.session.commit()
        return True
    return False

def get_all_users():
    all_users = users.query.all()
    user_list = [{"username": user.username, "password": user.password} for user in all_users]
    print(user_list)
    return jsonify(user_list)

def get_all_tasks():
    all_tasks = Task.query.all()
    task_list = [{"title": task.title, "Description": task.description,"status": task.status, "due-days": task.due_days} for task in all_tasks]
    print(task_list)
    return jsonify(task_list)

def get_all_payments():
    all_tasks = pay.query.all()
    pay_list = [{"task": pay.task, "amount": pay.amount,"status" : pay.status} for pay in all_tasks]
    print(pay_list)
    return jsonify(pay_list)

def user_logins(username,password):
    all_users = users.query.get(username)
    if all_users:
        return True
    return False


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)  # You can remove this line if you don't want to run the Flask app
