#Python flask RESTful Web API
from flask import Flask, url_for, request, json
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
    if request.method == 'GET':
        return 'echo: GET\n'
    elif request.method == 'POST':
        return 'echo: POST\n'
    else:
        return 'echo: other HTTP method'
    
@app.route('/messages', methods=['POST'])
def api_messages():
    if request.headers['Content-Type'].startswith('text/plain') == 'test/plain':
        return 'Test Message: ' + request.data
    elif request.headers['Content-Type'] == 'application/json':
        return 'JSON Message: ' + json.dumps(request.json)
    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"
    else:
        return "415 Unsupported Media Type ;)"


if __name__ == '__main__':
    app.run()