import requests

url = "http://ashshare.pythonanywhere.com/search"

params = {
    "token": "APITOKENHERE",
    "query": "QUERYHERE"
}

response = requests.post(url,params=params)

print(response.status_code)   # prints the HTTP status code
print(response.text)          # prints the response body as a string


