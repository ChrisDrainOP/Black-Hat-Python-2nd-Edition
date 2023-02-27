import requests

# testing on bWAPP VM http://www.itsecgames.com/
url = 'http://172.24.172.109/bWAPP'
response = requests.get(url) # GET

print(response.text)

data = {'user': 'bee', 'passwd':'bug'}
response = requests.post(url, data=data) # POST

print(response.text) # response.text = string; response.content = bytestring