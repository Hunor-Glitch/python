import requests

username = "postman"
password = "password"
valasz  = requests.get("https://postman-echo.com/basic-auth", auth=(username, password))
print(valasz.status_code)
print(valasz.headers)
print(valasz.text)
