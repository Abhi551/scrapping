## urllib module and parse


from  urllib.request import urlopen
from  urllib.request import Request
from  urllib.parse  import urlparse
from  urllib.parse  import urlencode
from  urllib.parse  import urljoin

#simple accessing a webpage 
url="http://pythonprogramming.net/?s=basic&submit=Search"
html=urlopen(url)
#print (html.read())



# general access to page with search queries and data

basic_url="http://pythonprogramming.net"
values={'s':'basic','submit':'Search'}

#encode values in format of url
encoded_values=urlencode(values)

#converting them to utf - 8 so that they can be used in url
print (type(encoded_values));
encoded_values=encoded_values.encode('utf-8')
print (type(encoded_values));

#make a request from python to get the data

url_req=Request(url,encoded_values)
print (url_req)

#opening the url with the added data

client=urlopen(url_req)
html=client.read()
#print (html)


# many times we may not get access through 
#python for example
url="https://www.google.co.in/search?q=test&oq=test&aqs=chrome..69i57j0l5.869j0j7&sourceid=chrome&ie=UTF-8"
try:
	req=Request(url)
	client=urlopen(req)
	client.read()
except Exception as e:
	print (e);


#avoiding the forbidden exception
#changing the header

headers={};
headers['User-Agent']="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
try:
	client=Request(url,headers=headers)
	html=urlopen(client)
	html.read()
except Exception as e:
	print (e)