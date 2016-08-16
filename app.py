# coding: utf-8

from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)
api_key = '19ffb04654b0f50d003e0a58abf2c50b'

@app.route('/<name>')
def user(name):
    # flask.jsonify() 可以返回 JSON 字符串
    return jsonify(code=200, message='Hello, {0}~'.format(name))

@app.route('/history-today/<month>/<day>', methods=['GET'])
def historytoday(month, day):
    # 请求历史上的今天接口
    url = 'http://apis.baidu.com/avatardata/historytoday/lookup?yue={0}&ri={1}&type=1&page=1&rows=20&dtype=JSON&format=true'.format(month, day)
    headers = {'apikey': api_key}
    r = requests.get(url, headers=headers)
    if r.status_code == requests.codes.ok:
        if r.json()['error_code'] == 0:
            return jsonify(code=0, results=r.json()['result'])
        else:
            return jsonify(code=r.json()['error_code'], message=r.json()['reason'])
    else:
        return jsonify(code=r.status_code, message='服务器错误')
