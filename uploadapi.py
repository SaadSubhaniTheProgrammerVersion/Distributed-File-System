import requests

url = "http://localhost:5000/upload"

params = {
    "token": "naseerbajwa",
    "filepath": r"path/to/your/upload/file"
}

files = {
    "image": open(r"path/to/your/upload/file", "rb")
}

response = requests.post(url,params=params,files=files)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string


