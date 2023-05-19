import requests

url = "http://ashshare.pythonanywhere.com/download"

params = {
    "token": "APITOKENHERE",
    "filepath": r"FILEPATHHERE"
}

response = requests.post(url,params=params)

print(response.status_code)   # prints the HTTP status code
print(response.text)     
