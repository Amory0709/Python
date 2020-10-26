import urllib.request, urllib.parse, urllib.error
import json
import ssl

url = ' http://py4e-data.dr-chuck.net/comments_166447.json'
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

c_data = json.loads(data)
sum = 0
for c in c_data['comments']:
    sum += c['count']
print("Sum of the comments equals to ", sum)
