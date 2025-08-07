#Python flask RESTful Web API
from flask import Flask, url_for
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

if __name__ == 'main':
    app.run()