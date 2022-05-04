import requests

server = 'http://127.0.0.1:5000'
url = '{s}/api/v1/retrain'.format(server)
params = {'tv': 325.5, 'radio': 54, 'newspaper': 2393}
r = requests.get(url, params=params)
r.encoding = 'utf-8'
print(r.text)