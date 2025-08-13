#Python flask RESTful Web API
import json
from flask import Flask, url_for, request, json, Response, jsonify
from functools import wraps

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome to the landing page'

@app.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<article_id>')
def api_article(article_id):
    return 'You are reading article: ' + article_id

@app.route('/hello')
def hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'

@app.route('/echo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def api_echo():
    try:
        if request.method == 'GET':
            return 'echo: GET\n'
        elif request.method == 'POST':
            return 'echo: POST\n'
        else:
            return 'echo: other HTTP method'
    except:
        print('ERROR')
    
@app.post("/messages")
def messages():
    try: 
        ctype = (request.content_type or "").lower()
        if ctype.startswith("text/plain"): #clients and curl often sends 'text/plain; charset=utf-8'
            return "Text Message: " + request.get_data(as_text=True)
        if request.is_json:
            return "JSON Message: " + json.dumps(request.get_json())
        if ctype.startswith("application/octet-stream"):
            with open("binary", "wb") as f:
                f.write(request.get_data())
            return "Binary message written!"
        return "415 Unsupported Media Type ;)", 415
    except:
        print('ERROR')

@app.get("/hello")
def api_hello():
    data = {
        'name': 'Shayan',
        'major': 'CS'
    }
    resp = jsonify(data)
    # js = json.dumps(data) #convert dictionary to JSON
    # resp = Response(js, status=200, mimetype='application/json')
    resp.status_code = 200
    resp.headers['Link'] = 'http://127.0.0.1:5000/hello'
    return resp

@app.errorhandler(404)
def not_found(error=None):
    msg = {
        'error': 404,
        'msg': 'Not found' + request.url
    }
    resp = jsonify(msg)
    resp.status_code = 404
    return resp

@app.route('/users/<user_id>')
def api_user(user_id):
    users = {'1':'john', '2':'steve', '3':'bill'}
    if user_id in users:
        return jsonify({user_id:users[user_id]})
    else:
        return not_found()

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    message = {'message': "Authentication required."}
    resp = jsonify(message)
    resp.status_code = 401 #401 Unauthorized - credentials missing or wrong
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return resp

if __name__ == "__main__":
    app.run(debug=True) # this will prevent the need to restart server after every change.