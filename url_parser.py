## parsing the url in urllib.parse

#parse == spliting the url
from collections import namedtuple
from urllib.parse import urlparse;

url = 'http://netloc/path;param?query=arg#frag'
parsed_url=urlparse(url)

print (parsed_url)
#parsed_url is a named tuple of length 6

#no username or password in url
print (parsed_url.username,parsed_url.password)

#named tuple can also be accessed by indexes
for i in range(len(parsed_url)):
	print (parsed_url[i])

url = 'http://user:pwd@NetLoc:80/path;param?query=arg#frag'

parsed_url=urlparse(url)
print (parsed_url)

##username and password in the  url are given 
## by default they are None if not provided

print (parsed_url.username)
print (parsed_url.password)





## urlsplit is similar to urlparse but there are differences
from urllib.parse import urlsplit
print (urlsplit(url))	#split doesn't  split the parameters from url
print (urlparse(url))	





## fragments in url
## they are short string present in the end of url marked by '#''
## these strings refers to a resource that is subordinate to primary document
from urllib.parse import urldefrag
## urldefrag splits the fragments in url 
url = 'http://netloc/path;param?query=arg#frag'
print ("\nurl defrag : ",urldefrag(url))
print ("url: ",url)
print ("\n")





## unparsing in url
## there are 2 ways geturl or urlunparse
from urllib.parse import urlunparse

url= 'http://netloc/path;param?query=arg#frag'
parsed_url=urlparse(url)

print ("original url :- \n",url ,"\n")
print (parsed_url,"\n")

#parsed url can be unparsed using geturl()
print (parsed_url.geturl(),'\n')

#parsed url can be unparsed using urlunparse
print (urlunparse(parsed_url))
print ("\n")

## urlunparse can remove superflous part from url while unparsing
original = 'http://netloc/path;?#'
parsed_url=urlparse(original)
url=urlunparse(parsed_url)
print ("original ", original,"\n")
print ("parsed_url ",parsed_url,"\n")
print ("unparsed url ",url,"\n")





##constructing absolute url from relative fragments 
## urljoin

from urllib.parse import urljoin

print ("urljoin : ",urljoin("http://www.example.com/path/file.html",
              "anotherfile.html"))
print ("'urljon : ",urljoin("http://www.example.com/path/file.html",
              "../anotherfile.html"))





## encoding query arguments 
## used for encoding i.e. converting into url readable format

from urllib.parse import urlencode

a={'x':"BAhishdklf",'y':"shduib  sdld;f"}
print (urlencode(a))

print ("\n")
# for a list of several values
# ie for a given sequence of values
a={'x':["ABhishek","Chauhan"]}
print ("without doseq : ",urlencode(a))
print ("wiht doseq : ",urlencode(a,doseq=True))



#decoding the encoded characters 
#using parse_qs and parse_qsl

#parse_qs for  dictionary
#parse_qsl for list of tuples
from urllib.parse import parse_qs,parse_qsl
from urllib.parse import urlencode

encode={'a':['ABhishek','Chauhan'],'b':"HOme"}
encoded=urlencode(encode,doseq=True)
print ("encoded: ",encoded)

#to decode 
decode=parse_qs(encoded)
print (decode)
decode1=parse_qsl(encoded)
print (decode1)




#encoding for special characters
#urlencode can encode for simpple characters but for 
#special charaters we need to use 


from urllib.parse import quote,quote_plus,urlencode

url = 'http://localhost:8080/~hellmann/'

#encoding using quote,quote_plus , urlencode

print ('urlencode : ',urlencode({'url':url}))
print ('url quote : ',quote(url))
print ('url quote_plus : ',quote_plus(url))
