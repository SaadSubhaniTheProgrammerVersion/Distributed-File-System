from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os

app = Flask(__name__)


STORAGE_DIRECTORY=r'C:\Users\saads\Downloads\DC Project\Distributed-File-System\static\files'
apitoken="shahkhalid"

@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/uploadfiles")
def UploadFiles():
    file_names = []

    for filename in os.listdir(STORAGE_DIRECTORY):
        filepath=os.path.join(STORAGE_DIRECTORY, filename)
        file_info = {
            "name": filename,
            'path': filepath,
        }
        file_names.append(file_info)

    return render_template('uploadfiles.html', file_names=file_names)


@app.route('/download/<path:file_path>')
def download(file_path):
    return send_file(file_path, as_attachment=True)

# @app.route("/upload", methods=['GET', 'POST'])
# def upload():
#     try:
#         if request.method == 'POST':
#             token = request.args.get("token")
#             filepath = request.args.get("filepath")
#             file = request.files["file"]

#             if file  and token==apitoken:
#                 filename = secure_filename(file.filename)
#                 file.save(os.path.join(STORAGE_DIRECTORY, filename))
#                 return "File uploaded!"
#             else:
#                 return "Invalid Token!"
#         else:
#             return "Error!"
#     except:
#         return "Error!"

@app.route('/upload', methods = ['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        if f :
            filename = secure_filename(f.filename)
            f.save(os.path.join(r'C:\Users\saads\Downloads\DC Project\Distributed-File-System\static\files', filename))
            #session['imagepath'] = os.path.join(r'\static\input\diabeticretinopathy', filename)


            return redirect(url_for('UploadFiles'))
        else:
            return redirect(url_for('UploadFiles'))


# @app.route('/download', methods=['GET', 'POST'])
# def download():
#     try:
#         token = request.args.get("token")
#         filepath = request.args.get("filepath")

#         if token==apitoken:
#             filepath=os.path.join(STORAGE_DIRECTORY, filepath)
#             if os.path.isfile(filepath):
#                 filename=os.path.splitext(os.path.basename(filepath))[0]
#                 return send_file(filepath, as_attachment=True)
#             else:
#                 return "File not found!"
#         else:
#             return "Invalid Token!"
#     except:
#         return "Error!"

@app.route('/listAllFiles', methods=['GET', 'POST'])
def listAllFiles():
    file_names = ['example_file.pdf', 'another_file.txt', 'some_file.doc']

    return render_template('uploadfiles.html', file_names=file_names)


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
