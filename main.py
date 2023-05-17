from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import Database
import time

app = Flask(__name__)


STORAGE_DIRECTORY=r'C:\Users\huzai\Documents\GitHub\Distributed-File-System\static\files'
app.secret_key = 'shahkhalid'
APITOKEN="shahkhalid"

users={
    "shahkhalid":"shahkhalid",
}



@app.route("/")
def Index():
    return render_template("Index.html")

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
    elif session['lastpage']=="Signup":
        if username!="" and password!="" and (username not in users ):
            users.update({username:password})
            session['username'] = username
            session['logined']="True"
            return redirect(url_for('Files'))
        else:
            session['logined']="False"
            return redirect(url_for('Signup'))



@app.route("/Files")
def Files():
    if session['logined']=="True":
        file_names = []

        files=Database.readFiles()

        for file in files:
            file_info = {
                "name": file.get('name'),
                'path': file.get('path'),
                'time':file.get('time'),
                'author':file.get('author'),
                'size': str(round(os.path.getsize(file.get('path'))/ (1024 * 1024),1))+" MB" ,
            }
            file_names.append(file_info)

        return render_template('Files.html', file_names=file_names)
    else:
        return redirect(url_for('Login'))

@app.route('/View/<path:file_path>')
def View(file_path):
    if session['logined']=="True":
        if os.path.exists(file_path):
            return send_file(file_path)
        else:
            return redirect(url_for('Files'))
    else:
        return redirect(url_for('Login'))


@app.route('/Download/<path:file_path>')
def Download(file_path):
    if session['logined']=="True":
        return send_file(file_path, as_attachment=True)
    else:
        return redirect(url_for('Login'))

@app.route('/Delete/<path:file_name>')
def Delete(file_name):
    if session['logined']=="True":
        if os.path.exists(os.path.join(STORAGE_DIRECTORY, file_name)):
            os.remove(os.path.join(STORAGE_DIRECTORY, file_name))
            Database.deleteFile(file_name)
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
            if f :
                filename = secure_filename(f.filename)
                f.save(os.path.join(STORAGE_DIRECTORY, filename))
                Database.addFile(filename,os.path.join(STORAGE_DIRECTORY, filename),session['username'])
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
    session['logined']="False"
