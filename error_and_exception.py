from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError
from urllib.error import URLError
##Errors and Exceptions handling
url="http://www.pythonscraping.com/pages/page1.html"
req=Request(url)
try:
    resp=urlopen(req)
    client=resp.read()
    print('yes')
except HTTPError as e:
    print (e)
except URLError as e:
    print (e)

## exceptions also occurs when we try to access 
## non existing tags in html data or files

html=soup(client,'html.parser')
html=html.prettify()


## psuedo code for error and exceptions in accessing the tags of
## html document

## obj=html.tag (it runs whether it exist or not)
## obj.sometag  (gives error as operation is done on some non existing tag)

## 
'''
try : 
    content=html.nonexistingtag.sometag
except AttributeError as e:
    print (e)
else :                  >>>>>>>>> if nonexistingtag exists but sometag doesn't
    if content==None:          
        print (Not found)
    else :
        print (Found)
'''

## genreally defining the errors and exceptions handling
print (url)
def func(url):
    req=Request(url)
    try:
        resp=urlopen(req)
        client=soup(resp.read(),'html.parser')
        html=client.prettify()
        head=client.body
        if head==None:
            print ("None")
            return (None)
        else:
            try :
                head_1=head.h1 
            except ValueError as e:
                print (e)
                return (e)
            return (head_1)

    except URLError as e:
        print ("this is URLError :%s "%e)
        return (e)
    except HTTPError as e:
        print ("This is HTTPError :%s"%e)
        return (e)



url="http://www.pythonscraping.com/pages/page1.html"
x=func(url)
print (x)


