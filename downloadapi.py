import requests

url = "http://localhost:5000/download"

params = {
    "token": "shahkhalid",
    "filepath": r"path/to/your/upload/file"
}

response = requests.post(url,params=params)

print(response.status_code)   # prints the HTTP status code


with open("path/to/your/downlaod/file/nameofile", "wb") as f:
    f.write(response.content)