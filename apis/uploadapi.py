import requests

url = "http://ashshare.pythonanywhere.com/upload"

params = {
    "token": "APITOKENHERE",
    "filepath": r"FILEPATHHERE"
}

files = {
    "file": open(r"FILEPATHHERE", "rb")
}


response = requests.post(url,params=params,files=files)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string


