#Python flask RESTful Web API
from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def landing_page():
    return 'Welcome to the landing page'
