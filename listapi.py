import requests

url = "http://localhost:5000/listAllFiles"

params = {
    "token": "shahkhalid",
}


response = requests.post(url,params=params)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string


