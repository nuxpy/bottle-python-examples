# -*- coding: utf-8 -*-
''' Mi proyecto en python usando Bottle
'''
import bottle
from bottle import route, template, request

app = bottle.Bottle()

@app.get('/')
def index():
    return template('index', valor='Nuxpy')

@app.post('/envia_contacto', template='index')
def index():
    contacto = request.forms.get('mi_contacto')
    return 'Contacto es %s' % contacto

app.run(host='0.0.0.0', port='8082', debug=True)
