# -*- coding: utf-8 -*-
''' Mi proyecto en python usando Bottle
'''
import bottle
from bottle import route, template

app = bottle.Bottle()

@app.route('/', template='index')
def index():
    return template('index', valor='Nuxpy')

app.run(host='0.0.0.0', port='8082', debug=True)
