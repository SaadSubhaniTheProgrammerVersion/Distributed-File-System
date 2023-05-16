import requests

url = "http://ashshare.pythonanywhere.com/download"

params = {
    "token": "shahkhalid",
    "filepath": r"hello.txt"
}

response = requests.post(url,params=params)

print(response.status_code)   # prints the HTTP status code
print(response.text)     

# with open("helo.txt", "wb") as f:
#     f.write(response.content)