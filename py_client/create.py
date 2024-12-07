import requests
data = {
    "title":"required field ",
    "price":32.99
}
response = requests.post("http://127.0.0.1:8000/product/", json=data)

print(response.json())