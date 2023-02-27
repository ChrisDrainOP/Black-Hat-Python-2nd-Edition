import urllib.parse
import urllib.request

url = 'https://www.google.com'
with urllib.request.urlopen(url) as response: # GET
    content = response.read()
print(content)