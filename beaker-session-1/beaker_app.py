# -*- coding: utf-8 -*-
import uuid
import bottle
from bottle import route, get, post, run, default_app, error, template, redirect, request, response
from beaker.middleware import SessionMiddleware


def check_session(function):
    def wrapper(*args, **kwargs):
        session = request.environ.get('beaker.session')
        username = session.get('user', None)
        if username and function.__name__ == 'logout':
            session.delete()
            return function(*args, **kwargs)
        elif username:
            return function(*args, **kwargs)
        return redirect('/')
    return wrapper

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 3600,
    'session.data_dir': 'db/sessions',
    'session.auto': True
}
app = default_app()
app = SessionMiddleware(app, session_opts)
token = str(uuid.uuid4())

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@get('/logout', template='logout')
@check_session
def logout():
    return redirect('/')

@get('/', template='index')
def index():
    return template('index', token=token)

@post('/login', template='index')
def login():
    username = request.forms.get('username').strip()
    password = request.forms.get('password').strip()
    if username == 'nuxpy' and password == 'nuxpy':
        session = request.environ.get('beaker.session')
        session['user'] = username
        session.save()
        return redirect('/system')
    return template('index', token=token)


@get('/system')
@check_session
def system():
    return template('system')

@get('/myaccount')
@check_session
def myaccount():
    return template('myaccount')


if __name__ == '__main__':
    run(app=app, host='0.0.0.0', port='8010', debug=True)

