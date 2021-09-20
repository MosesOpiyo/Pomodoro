from flask import Flask,jsonify
from flask_httpauth import HTTPBasicAuth
from flask import make_response
from . import app,tasks
auth = HTTPBasicAuth()



auth.get_password
def get_password(username,password):
    if username == username:
        return password
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})