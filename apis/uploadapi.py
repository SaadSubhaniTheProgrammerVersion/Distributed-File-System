import requests

url = "http://ashshare.pythonanywhere.com/upload"

params = {
    "token": "shahkhalid",
    "filepath": r"C:\Users\saads\Downloads\PE Presentation.pdf"
}

files = {
    "file": open(r"C:\Users\saads\Downloads\PE Presentation.pdf", "rb")
}


response = requests.post(url,params=params,files=files)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string


