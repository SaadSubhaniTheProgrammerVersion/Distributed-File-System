from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import os
import requests


app = Flask(__name__)

@app.route("/")
def Index():
    return render_template("Index.html")


@app.route('/upload', methods = ['POST'])
def upload():
    return

@app.route('/download', methods = ['GET'])
def download():
    return

def search():
    return

app.run()