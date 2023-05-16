from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os

app = Flask(__name__)


STORAGE_DIRECTORY=r'C:\Users\huzai\Documents\GitHub\Distributed-File-System\static\files'
apitoken="shahkhalid"

@app.route("/")
def Index():
    return ""


@app.route("/upload", methods=['GET', 'POST'])
def upload():
    try:
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
    except:
        return "Error!"



@app.route('/download', methods=['GET', 'POST'])
def download():
    try:
        token = request.args.get("token")
        filepath = request.args.get("filepath")

        if token==apitoken:
            filepath=os.path.join(STORAGE_DIRECTORY, filepath)
            if os.path.isfile(filepath):
                filename=os.path.splitext(os.path.basename(filepath))[0]
                return send_file(filepath, as_attachment=True)
            else:
                return "File not found!"
        else:
            return "Invalid Token!"
    except:
        return "Error!"

@app.route('/listAllFiles', methods=['GET', 'POST'])
def listAllFiles():
    try:
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
    except:
        return "Error!"


@app.route('/search', methods=['GET', 'POST'])
def search():
    try:
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
    except:
        return "Error!"

if __name__ == "__main__":
    app.run()
>>>>>>> 07fd70ce1262412f53f5302ba520233ee818c5cb
