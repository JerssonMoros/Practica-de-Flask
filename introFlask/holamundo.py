from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'hola mundo'

# @app.route('/post/<type>', methods=['GET'])
# def get(type):
#     return 'Este es el metodo GET'

# @app.route('/post/<type>', methods=['POST'])
# def post(type):
#     return 'Este es el metodo POST'

@app.route('/post/<type>', methods=['GET','POST'])
def get_post(type):
    if request.method == 'GET':
        return 'Es un GET'
    if request.method == 'POST':
        return 'es un POST'

# @app.route('/request')
# def funrequest():
#     print(request.form)
#     return 'hola mundo'
