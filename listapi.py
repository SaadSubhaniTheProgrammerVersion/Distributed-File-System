import requests

url = "http://ashshare.pythonanywhere.com/listAllFiles"

params = {
    "token": "shahkhalid",
}


response = requests.post(url,params=params)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string


