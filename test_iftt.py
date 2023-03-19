import requests

url = "https://maker.ifttt.com/trigger/data_wybila/json/with/key/c_gqYRvJ5NVJxyD-PR4fpP"
body = { "message": "działa 🤑"}

response = requests.post(url, json=body)
print(response)
print(response.text)
