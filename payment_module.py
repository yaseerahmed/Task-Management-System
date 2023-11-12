from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from central_db import * # Import the SQLAlchemy instance and User model from your previous app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'  # Use the same database as your previous app
db.init_app(app)  # Initialize the database for this app


@app.route('/initiate_payment', methods=['POST'])
def initiate_payment():
    data = request.get_json()
    task = data.get('task')
    amount = data.get('amount')
    if task:
        initiate_pay(task,amount)
        return jsonify({"message": "Pay has been initiated"})
    return jsonify({"message": "Invalid task id"})

@app.route('/track_payments', methods=['GET'])
def track_payments():
    return get_all_payments()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True,port=5003)