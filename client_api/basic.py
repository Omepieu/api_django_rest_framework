import requests

endpiont = 'http://127.0.0.1:8000/use_api/'
response = requests.get(endpiont)
print(response.text)
print(response.status_code)