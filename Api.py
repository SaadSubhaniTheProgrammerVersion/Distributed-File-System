import requests

def upload(token,path,filename,author,time):
    #link of backup server
    url = "http://ashshare.pythonanywhere.com/upload"

    params = {
        "token": token,
        "filepath": path,
        "filename": filename,
        "author":author,
        "time":time
    }

    files = {
        "file": open(path, "rb")
    }

    response = requests.post(url,params=params,files=files)
    return response.status_code, response.text