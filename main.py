from flask import Flask, render_template, request, redirect, url_for, session, flash, send_file, jsonify
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os

app = Flask(__name__)


STORAGE_DIRECTORY=r'C:\Users\huzai\Documents\GitHub\Distributed-File-System\static\files'
apitoken="shahkhalid"

@app.route("/")
def Index():
    return render_template("Index.html")

@app.route("/Files")
def Files():
    file_names = []

    for filename in os.listdir(STORAGE_DIRECTORY):
        filepath=os.path.join(STORAGE_DIRECTORY, filename)
        file_info = {
            "name": filename,
            'path': filepath,
            'size':str(round(os.path.getsize(filepath)/ (1024 * 1024),1))+" MB" ,
        }
        file_names.append(file_info)

    return render_template('Files.html', file_names=file_names)

@app.route('/View/<path:file_path>')
def View(file_path):
    if os.path.exists(file_path):
        return send_file(file_path)
    else:
        return redirect(url_for('Files'))


@app.route('/Download/<path:file_path>')
def Download(file_path):
    return send_file(file_path, as_attachment=True)

@app.route('/Delete/<path:file_path>')
def Delete(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        return redirect(url_for('Files'))
    else:
        return redirect(url_for('Files'))

@app.route('/Upload', methods = ['GET', 'POST'])
def Upload():
    if request.method == 'POST':
        f = request.files['file']
        if f :
            filename = secure_filename(f.filename)
            f.save(os.path.join(STORAGE_DIRECTORY, filename))
            return redirect(url_for('Files'))
        else:
            return redirect(url_for('Files'))
    else:
        return redirect(url_for('Files'))



if __name__ == "__main__":
    app.run()
