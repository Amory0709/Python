import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

url = 'http://py4e-data.dr-chuck.net/comments_166446.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
# use an XPath selector string to look through the entire tree of XML for
# any tag named 'count' with the following line of code
counts = tree.findall('.//count')
sum = 0
for count in counts:
    sum += int(count.text)
print("Sum of counts equals to ", sum)
