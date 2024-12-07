import requests
data = {
    "title":"Helllo world its updated now ",
    "price":3
}
response = requests.put("http://127.0.0.1:8000/product/5/update/", json=data)

print(response.json())