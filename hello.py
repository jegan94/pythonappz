from flask import Flask, jsonify, request

app = Flask(__name__)

login_res = [
    {'status': '200', 'message': 'Login successfully', 'username': 'Test', 'mobile': 9876543210,
     'email': 'test@gmail.com'}
]


@app.route("/")
def hello_world():
    return "Hello world"


@app.route("/login")
def login():
    return login_res

@app.route('/newlogin', methods=['POST'])
def newlogin():
    login_res.append(request.get_json())
    return 'Registration successfully', 200
