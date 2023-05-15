from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os

app = Flask(__name__)


STORAGE_DIRECTORY=r'mysite/static/files'
apitoken="shahkhalid"

@app.route("/")
def Index():
    return ""


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        token = request.args.get("token")
        filepath = request.args.get("filepath")
        file = request.files["file"]

        if file  and token==apitoken:
            filename = secure_filename(file.filename)
            file.save(os.path.join(STORAGE_DIRECTORY, filename))
            return "File uploaded!"
        else:
            return "Invalid Token!"
    else:
        return "Error!"


@app.route('/download', methods=['GET', 'POST'])
def download():
    token = request.args.get("token")
    filepath = request.args.get("filepath")

    if token==apitoken:
        filepath=os.path.join(STORAGE_DIRECTORY, filepath)
        if os.path.isfile(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            return "File not found!"
    else:
        return "Invalid Token!"

@app.route('/listAllFiles', methods=['GET', 'POST'])
def listAllFiles():

    token = request.args.get("token")

    if token==apitoken:
        directory=STORAGE_DIRECTORY
        files=[]

        for filename in os.listdir(directory):
            filepath=os.path.join(directory, filename)

            file_info = {
                "name": filename,
                'path': filepath,
            }
            files.append(file_info)

        return jsonify(files)
    else:
        return "Invalid Token!"


@app.route('/search', methods=['GET', 'POST'])
def search():
    token = request.args.get("token")
    query=request.args.get("query")

    if token==apitoken:
        directory=STORAGE_DIRECTORY
        files=[]

        for filename in os.listdir(directory):
            filepath=os.path.join(directory, filename)
            if query in filename:
                file_info = {
                    "name": filename,
                    'path': filepath,
                }
                files.append(file_info)

        return jsonify(files)
    else:
        return "Invalid Token!"


if __name__ == "__main__":
    app.run()