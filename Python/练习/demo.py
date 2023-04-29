import requests

r = requests.get('https://www.douban.com/', headers={
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})

print(r.text)
