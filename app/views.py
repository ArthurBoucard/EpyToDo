from app import app
from flask import render_template
import functools
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from app.db import get_db

active_user = "anonymous"

@app.route('/', methods = ['GET'])

def route_home():
    global active_user
    active_user = session['User_username']
    return render_template("index.html", title = "EpyToDo", user = active_user)

@app.route ('/register', methods = ('GET', 'POST'))

def register():
    global active_user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = 'USER {} is already registered.'.format(username)

        if error is None:
            db.execute(
                'INSERT INTO user (username, password) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('signin'))

        flash(error)

    return render_template('register.html', title = "Register", user = active_user)

@app.route ('/signin', methods = ('GET', 'POST'))

def signin():
    global active_user
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['User_id'] = user['id']
            session['User_username'] = user['username']
            return redirect(url_for('route_home'))

        flash(error)

    return render_template('signin.html', title = "Sign in", user = active_user)

@app.route ('/signout', methods = ['GET'])

def signout():
    global active_user
    session.clear()
    #active_user = "anonymous"
    session['User_username'] = "anonymous"
    return redirect(url_for('route_home'))

@app.route ('/user', methods = ['GET'])

@app.route ('/user/task', methods = ['GET'])

@app.route ('/user/task/id', methods = ['GET'])

@app.route ('/user/task/id', methods = ['POST'])

@app.route ('/user/task/add', methods = ['POST'])

@app.route ('/user/task/del/id', methods = ['POST'])

@app.route('/account', methods = ['GET'])

def route_account():
    global active_user
    if session['User_username'] == "anonymous":
        return render_template("account_ano.html", title = "Account", user = active_user)
    else:
        return render_template("account.html", title = "Account", user = active_user)
