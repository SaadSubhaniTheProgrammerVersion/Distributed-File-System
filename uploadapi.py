import requests

url = "http://localhost:5000/upload"

params = {
    "token": "shahkhalid",
    "filepath": r"C:\Users\huzai\Pictures\Files\Lecture-1.pdf"
}

files = {
    "file": open(r"C:\Users\huzai\Pictures\Files\Lecture-1.pdf", "rb")
}


response = requests.post(url,params=params,files=files)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string


