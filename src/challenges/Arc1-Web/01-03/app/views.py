# -*- encoding: utf-8 -*-

# Flask modules
from flask   import make_response, redirect, render_template, request, session
from jinja2  import TemplateNotFound

# App modules
from app import app
import os
import subprocess
from sys import platform

cwd = os.getcwd()

# This password is not intended to be guessed or otherwise known to the CTF player.
user = { 
    "username": "admin", 
    "password": "422FC13B7AD4489C2759A1BAD3BBBAE864DC5053D3D8F998698FC7C4FEC28F9B"
}

# Helper functions
def get_segment( request ): 
    try:
        segment = request.path.split('/')[-1]
        if segment == '':
            segment = 'index'
        return segment    
    except:
        return None

# Create routes
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user_level = request.cookies.get('user_level')
        authed = request.cookies.get('authed')
        if ('username' in session and session['username'] == username) and  ('password' in session and session['password'] == password):
            # players should not be authenticating like this, if they do, they know information they shouldn't!
            return render_template('/home/web1-flag-e6d64a54dcc2845bd45a1ae3dd90d4b9.html')
        elif user_level == "admin" and authed == '1':
            # this is the expected way to authenticate (client-side authentication)
            return render_template('/home/web1-flag-e6d64a54dcc2845bd45a1ae3dd90d4b9.html')
        else:
            return render_template('/home/incorrect.html')
    return render_template("/home/sign-in.html")

@app.route('/log-out.html')
def logout():
    resp = make_response(render_template('/home/sign-in.html'))
    resp.set_cookie('user_level', 'guest')
    resp.set_cookie('authed', '0')
    resp.delete_cookie('access_token')
    return resp

@app.route('/records.html')
def records():
    user_level = request.cookies.get('user_level')
    authed = request.cookies.get('authed')
    if user_level != "admin" and authed != '1':
        return render_template('/home/sign-in.html')
    resp = make_response(render_template('/home/records.html'))
    resp.set_cookie('access_token', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJOZXh4dXMiLCJpYXQiOjE2MzUxMjI3OTUsImV4cCI6MTY2NjY1ODc5NSwiYXVkIjoiTkRSIGFkbWlucyIsInN1YiI6IkFjY2VzcyBjb2RlIGZvciBzZW5zaXRpdmUgZGF0YSIsIkFjY2Vzc0NvZGUiOiI2MjYwIn0.CjORA2THjMe71itx26iQ12xEPVXeI0nMPdGL3qNLUOA')
    return resp

@app.route('/check_access_code.html', methods = ['POST', 'GET'])
def check_access_code():
    user_level = request.cookies.get('user_level')
    authed = request.cookies.get('authed')
    if user_level != "admin" and authed != '1':
        return render_template('/home/sign-in.html')
    if request.method == 'POST':
        accesscode = request.form.get('accesscode')
        if (accesscode == "6260" or accesscode == 6260):
            return render_template('/home/web2-flag-82200e3de63ecd2bdd453855dd7aca52.html')
        else:
            return render_template('/home/records.html')
    return render_template("/home/records.html")

@app.route('/logviewer.html', methods = ['POST', 'GET'])
def logviewer():
    user_level = request.cookies.get('user_level')
    authed = request.cookies.get('authed')
    if user_level != "admin" and authed != '1':
        return render_template('/home/sign-in.html')
    os.chdir(cwd)
    if request.method == 'POST':
        logfile = request.form.get('logfile').strip()
        if (logfile == "flag.txt" or logfile == "./flag.txt"):
           return render_template('/home/hackerdetected.html')
        if (".html" in logfile or ".." in logfile or "/" in logfile):
            return render_template('/home/hackerdetected.html')
        else:
            os.chdir(os.path.join(cwd, "static"))
            try:
                output = "error"
                command = None
                if platform == "win32":
                    command = f"type {logfile}".split(" ")
                    output = subprocess.check_output(command, shell=True, timeout=1)
                else:
                    #command = f"cat {logfile}".split(" ")
                    #output = subprocess.check_output(command, timeout=1)
                    command = f"cat {logfile}"
                    output = subprocess.check_output(command, shell=True, timeout=1)
                return output
            except subprocess.CalledProcessError as err:
                return f"Error in command {' '.join(command)}\n{err}"
    if request.method == 'GET':
        return render_template("/home/logviewer.html")
    return render_template("/home/logviewer.html")

@app.route('/', defaults={'path': 'sign-in.html'})
@app.route('/<path>')
def index(path):
    # Check if user is authed
    try:
        user_level = request.cookies.get('user_level')
        authed = request.cookies.get('authed')
        segment = get_segment(request)
        resp = make_response(render_template('home/' + path, segment=segment))
        resp.delete_cookie('access_token')
        if not user_level or not authed:
            resp.set_cookie('user_level', 'guest')
            resp.set_cookie('authed', '0')
        if path != "sign-in.html" and user_level != "admin" and authed != '1':
            return redirect('sign-in.html')
        return resp
    except TemplateNotFound:
        return render_template('home/page-404.html'), 404
    except Exception as e:
        return redirect('sign-in.html')

