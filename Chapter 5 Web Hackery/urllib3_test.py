import urllib3
url = 'https://www.nostarch.com'
http = urllib3.PoolManager()
response = http.request('GET', url)
print(response.data.decode('utf-8'))
response.release_conn()