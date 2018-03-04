import re
from urllib.request import urlopen
from urllib.parse import urlparse
from urllib.parse import urlencode
from urllib.parse import urljoin
import urllib.request
from bs4 import BeautifulSoup as soup

url="http://pythonprogramming.net"
values={'s':'basic','submit':'search'}
values=urlencode(values)
print (values)
values=values.encode('utf-8')
print (type(values))
req=urllib.request.Request(url,values)
print (req)
client=urlopen(req)
html=client.read()
html=soup(html,'html.parser')

data=re.findall(r'<p>.*</p>',str(html))
for line in data:
	print (line)