from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import Database
import time
from datetime import datetime

app = Flask(__name__)


STORAGE_DIRECTORY=r'static\files'
app.secret_key = 'distributedcomputingproject'
APITOKEN="distributedcomputingproject"

users={
    "huzaifa":"huzaifa",
    "saad":"saad",
}


GLOBAL_FILE_DATA=[]

@app.route("/")
def Index():
    session['lastpage']=""
    return render_template("index.html")

@app.route("/Login")
def Login():
    session['logined']="False"
    session['lastpage']="Login"
    return render_template("Login.html")


@app.route("/Signup")
def Signup():
    session['logined']="False"
    session['lastpage']="Signup"
    return render_template("Signup.html")


@app.route("/Forgot")
def Forgot():
    return render_template("Forgot.html")





@app.route("/Authenticate", methods=['POST'])
def Authenticate():
    username = request.form.get('username')
    password = request.form.get('password')

    if session['lastpage']=="Login":
        if username in users and password == users[username]:
            session['username'] = username
            session['logined']="True"
            return redirect(url_for('Files'))
        else:
            session['logined']="False"
            return redirect(url_for('Login'))
    elif session['lastpage'] == "Signup":
        if username != "" and password != "" and (username not in users):
            users.update({username: password})
            success_message = "User successfully added!"
            return render_template('Success.html', message=success_message)
        else:
            session['logined'] = "False"
            return redirect(url_for('Signup'))



@app.route("/Files")
def Files():
    if session['logined']=="True":
        file_names = []

        #files=GLOBAL_FILE_DATA
        files=Database.readFiles()

        for file in files:
            file_info = {
                "name": file.get('name'),
                'path': file.get('path'),
                'time':file.get('time'),
                'author':file.get('author'),
                'size': str(round(os.path.getsize(os.path.join('static/files', file.get('name')))/ (1024 * 1024),1))+" MB" ,
            }
            file_names.append(file_info)


        session['lastpage']="Files"
        return render_template('Files.html', file_names=file_names)
    else:
        return redirect(url_for('Login'))

@app.route('/View/<path:file_name>')
def View(file_name):
    if session['logined']=="True":
        if os.path.exists(os.path.join(STORAGE_DIRECTORY, file_name)):
            return send_file(os.path.join('static/files', file_name))
        else:
            return redirect(url_for('Files'))
    else:
        return redirect(url_for('Login'))


@app.route('/Download/<path:file_name>')
def Download(file_name):
    if session['logined']=="True":
        if os.path.exists(os.path.join(STORAGE_DIRECTORY, file_name)):
            return send_file(os.path.join('static/files', file_name), as_attachment=True)
        else:
            return redirect(url_for('Files'))
    else:
        return redirect(url_for('Login'))

@app.route('/Delete/<path:file_name>')
def Delete(file_name):
    if session['logined']=="True":
        if os.path.exists(os.path.join(STORAGE_DIRECTORY, file_name)):

            Database.deleteFile(file_name)
            os.remove(os.path.join(STORAGE_DIRECTORY, file_name))

            if len(GLOBAL_FILE_DATA)>0:
                i=0
                for file in GLOBAL_FILE_DATA:
                    if file.get('name')==file_name:
                        break
                    i=i+1


                GLOBAL_FILE_DATA.remove(GLOBAL_FILE_DATA[i])

            return redirect(url_for('Files'))
        else:
            return redirect(url_for('Files'))
    else:
        return redirect(url_for('Login'))

@app.route('/Upload', methods = ['GET', 'POST'])
def Upload():
    if session['logined']=="True":
        if request.method == 'POST':
            f = request.files['file']


            if f:
                filename = secure_filename(f.filename)
                Database.deleteFile(filename)
                f.save(os.path.join(STORAGE_DIRECTORY, filename))
                Database.addFile(filename,os.path.join('static/files', filename),session['username'])
                #Api.upload(APITOKEN,os.path.join(STORAGE_DIRECTORY, filename),filename,session['username'],str(datetime.now().date()))

                filedata={
                    "name":filename,
                    "path":os.path.join('static/files', filename),
                    "time":str(datetime.now().date()),
                    "author":session['username'],
                }

                GLOBAL_FILE_DATA.append(filedata)
                return redirect(url_for('Files'))
            else:
                return redirect(url_for('Files'))
        else:
            return redirect(url_for('Files'))
    else:
        return redirect(url_for('Login'))


if __name__ == "__main__":
    Database.createtable()
    app.run()
    session['lastpage']="Files"
    session['logined']="False"