from flask import render_template, session, request, redirect, url_for
from app import app
import os
import AddUserToProjectv2 as K5User
import k5APIwrappersV1 as K5API
#from k5contractsettingsV1 import *
global adminUser
global adminPassword
global contract
global region

app.secret_key = os.urandom(24)

@app.route('/login', methods=['GET','POST'])
def index():


   if request.method == 'POST':
     session.pop('user',None)
     adminUser =  request.form.get('k5username',None)
     adminPassword = request.form.get('k5password',None)
     contract = request.form.get('k5contract',None)
     region = request.form.get('k5region',None)
     print region
     result = K5API.get_unscoped_token()
     print result
     session['user'] =  request.form['k5username']
     session['password'] = request.form['k5password']
     session['contract'] = request.form['k5contract']
     session['region'] = request.form['k5region']



     if session['password']  == 'password':
       return redirect(url_for('adduser'))
     else:
       return render_template('hello-flask-login.html',
                           title='K5 Admin Portal (Beta)')

   else:
     return render_template('hello-flask-login.html',
                           title='K5 Admin Portal (Beta)')


@app.route('/adduser',methods=['GET','POST'])
def adduser():
  if request.method == 'POST':
    if request.form.get('AddUser', None) == "Add User":
      return redirect(url_for('userstatus'))
    else:
      if request.form.get('Logout', None) == "Logout":
        return redirect(url_for('logout'))

  if request.method == 'GET':
    return render_template('hello-flask-adduser.html',
                           title='K5 Add User')

@app.route('/userstatus',methods=['GET','POST'])
def userstatus():
  if request.method == 'POST':
    if request.form.get('AddUser', None) == "Add Another User":
      return redirect(url_for('adduser'))
    else:
      if request.form.get('Logout', None) == "Logout":
        return redirect(url_for('logout'))

  if request.method == 'GET':
    return render_template('hello-flask-result.html',
                           title='K5 New User Details',
                           userstatus = 'Put Results From New User Here!')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
  session.pop('username', None)
  return redirect(url_for('index'))