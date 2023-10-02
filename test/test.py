import requests

resp = requests.post("http://localhost:8080/predict", files = {'file': open('four.png', 'rb')} )

print(resp.text)