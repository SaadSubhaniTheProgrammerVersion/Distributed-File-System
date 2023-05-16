import requests

url = "http://ashshare.pythonanywhere.com/upload"

params = {
    "token": "shahkhalid",
    "filepath": r"C:\Users\huzai\Documents\GitHub\Distributed-File-System\hello.txt"
}

files = {
    "file": open(r"C:\Users\huzai\Documents\GitHub\Distributed-File-System\hello.txt", "rb")
}


response = requests.post(url,params=params,files=files)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string


