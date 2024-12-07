import requests

response = requests.post("http://127.0.0.1:8000/product/", json={"title":"hello world"},params={"abc":123})

print(response.json())