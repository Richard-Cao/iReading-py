# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import render_template
from flask_sockets import Sockets
from flask import jsonify

app = Flask(__name__)
sockets = Sockets(app)

@app.route('/<name>')
def user(name):
    # flask.jsonify() 可以返回 JSON 字符串
    return jsonify(code=200, message='Hello, {0}~'.format(name))
