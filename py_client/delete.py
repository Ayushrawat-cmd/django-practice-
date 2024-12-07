import requests
data = {
    "title":"required field ",
    "price":32.99
}
response = requests.delete("http://127.0.0.1:8000/product/2/delete/")

print(response.status_code)