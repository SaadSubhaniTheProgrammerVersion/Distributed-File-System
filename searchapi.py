import requests

url = "http://localhost:5000/search"

params = {
    "token": "shahkhalid",
    "query": "Isb"
}

response = requests.post(url,params=params)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string


