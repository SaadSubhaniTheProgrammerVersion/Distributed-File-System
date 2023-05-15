from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import requests


app = Flask(__name__)

apitoken="shahkhalid"

@app.route("/")
def Index():
    return render_template("Index.html")


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == 'POST':
        token = request.args.get("token")
        imagepath = request.args.get("imagepath")
        image_file = request.files["image"]

        if image_file  and token==apitoken:
            filename = secure_filename(image_file.filename)
            image_file.save(os.path.join(r'C:\Users\huzai\Documents\GitHub\Distributed-File-System\static\files', filename))
            return "File uploaded!"
        else:
            return "Invalid Token!"



@app.route('/download', methods=['GET', 'POST'])
def download():
    token = request.args.get("token")
    imagepath = request.args.get("filepath")

    if token==apitoken:
        filepath=os.path.join(r'C:\Users\huzai\Documents\GitHub\Distributed-File-System\static\files', imagepath)
        if os.path.isfile(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            return "File not found!"
    else:
        return "Invalid Token!"

@app.route('/search', methods=['GET', 'POST'])
def search():
    return

app.run()