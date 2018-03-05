from urllib.request import Request 
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup 
from urllib.error import URLError
from urllib.error import HTTPError
import re


## func to get all green coloured names on site
## BeautifulSoup in very powerful and findAll function finds all the 
## searched and matching queries and return it

def func(req):
	try :
		resp=urlopen(req)
		client=resp.read()
		html=soup(client,'lxml')
		names=html.findAll('span',{'class':'green'})
		if names==None:
			return (None)
		else :
			for name in names:
				(name.get_text())

	except URLError as e:
		print (e)
		return (e)
	except HTTPError as e:
		print (e)
		return(e)

req=Request("https://www.pythonscraping.com/pages/warandpeace.html")
func(req)

## findAll() and find_all() both are similar in BS4
## find()    and findAll()
## find()    matches the result and return the first match we obtain
## findAll() returns all the results obtained from the search



## kinds of filters used in find_all or findAll()

print ("\nThis is string filter\n")

## 1. string
## string filter used in findAll or find_all
## only works on tags used in html document
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story"></p>
"""

html=soup(html,'html.parser')

## finds all the tags with a tag
print (html.findAll('a'))
## finds all the tags with p tag
print (html.findAll('p'))

## 2. A list
## passing a list will allow a string match against any element 
## in the list
print ("\nthis is list filter \n")
print (html.find_all(['a','p']))

## 3. True 
print ('\n')
print ("this is True filter\n")
## matches amd returns all the tags in html document
for tag in html.findAll(True):
	print (tag.name)
print ('\n prints everything in the document\n')
print (html.findAll(True))


## 4. A function

print ('\n')

## if none of the above matches our tag then define a function 
## that takes an element as argument which returns True if matches else False

## this function returns all <p> tag in the html
## because only <p> and not <a> tags because
## <p> tags are defined with class only 
## <a> tags are definef with class and id as well 
print ("\nthis is fucntion filter \n")
def has_class(tag):
	return tag.has_attr('class') and not tag.has_attr('id')
print ("\nthis function is for <p> tag\n")
print (html.find_all(has_class))


## this is for all <a>
print ("Another function for <a> tag")
def has_a(tag):
	return tag.has_attr('class') and tag.has_attr('id')  and not re.search(r'lacie',str(tag))
print ("\nthis is for <a> tag\n")
tags=html.find_all(has_a)
print (tags)
## or the other way is to combine regex with
## functions
def has_a(tag):
	return tag.has_attr('class') and tag.has_attr('id')
print ("\nthis is for <a> tag\n")
tags=html.find_all(has_a)
print (tags)
for i in tags:
	if re.search(r'lacie',str(i)):
		pass
	else:
		print (i)


resp=urlopen(req)
html_doc=resp.read()
html_doc=soup(html_doc,'html.parser')
#print (html_doc.findAll('span')[0])



## above are some filters that can be used with find_all()
## find_all(name, attrs, recursive, string, limit, **kwargs)

## the find_all() looks through a tag's descendent and  retriives all 
## the descendent that matches our filter 



## 1. Name argument

## find_all() >>> name argument

## only searches through tags and ignores everything from text 
## to other tags which are not filtered

## this name is just the above discussed filters thus it can take 
## strings , list , functions , True ,a regex

print ("\nthis is name argument\n")
print (html.find_all('title'))



## 2. The keyword argument

## it searches and matches all id tags containing id with specified argument

print ("\nthis searches all id tags with 'link1' and 'link2' as the argument\n")
print (html.find_all(id='link1'))
print (html.find_all(id='link2'))

print ("\nprint all id tags\n")
print (html.find_all(id=True))

## using re.compile to match , as re.compile converts pattern into pattern objects
## thus we can use these objects as regex to search
print ('\nuse of regex in keyword argument\n')
print (html.find_all(href=re.compile('elsie')))

## important if there type of argument we can't directly pass the arguments as this
## so we need to change this in dictionary format and then work on it

data_soup = soup('<div data-foo="value">foo!</div>','html.parser')

#data_soup.find_all(data-foo='value'):


## this is the correct way to do it
print ("\nWe can't use keyword as in argument for keyword\n")
obj=data_soup.find_all(attrs={'data-foo':'value'}) 
print (obj)
## similaraly we can't give name element as keyword argument
## to use keyword as in argument use dictionary

name_soup = soup('<input name="email"/>','html.parser')
## print (name_soup.find_all(name='email'))
print ("\nAnother example\n")
print (name_soup.find_all(attrs={'name':'email'}))


## search by class name in CSS class 
## class is keyword in python so we use either 'class_'
## or pass it as a attrr={'class':'something'}
print ('\nthis is CSS class\n')
print (html.find_all(class_=True))
print ("\nThis is anothet method using attributes\n")
print (html.find_all(attrs={'class':True}))

## using tag and class both , i.e. searching a class inside a tag

print ("\nusing tag and class both \n")

print (html.find_all('p',class_="title"))
print ("\nanother exmaple\n")

## using regex to find

print (html.find_all(class_=re.compile('itle')))

css_soup = soup('<p class="body strikeout"></p>','html.parser')

## a single tag can have multiple values for its 'class' attributes
## multiple ways to find and search the class 

print ("\nThese are multiple ways to give class = body strikeout \n")
print (css_soup.find_all(class_='body strikeout'))
print (css_soup.find_all(class_='body'))
print (css_soup.find_all(class_='strikeout'))

## none is the output when the reverse string is passed

print (css_soup.find_all(class_="strikeout body"))


## passsing string argument as keyword
## In string argument we can use  a string , a regex ,  a list , a True value for string or f a function

print ("\nthis is a string\n",html.find_all(string='Elsie'))
print ("\nthis is regex\n",html.find_all(string =re.compile("[ETL][a-z]*")))
print ("\nthis is list\n",html.find_all(string =['Elsie','Tillie','Lacie']))

## combining string argument with tags

print ("\ncombining the tags with string argument\n")
print (html.find_all('a',string="Elsie"))

## setting the limit through limit argument
## if we don't need all the results of find_all() we can set the limit
## by passing limit argument inside the find_all(limit=)
print ("\nthis is limit\n")
print (html.find_all(id=True,limit=2))

## this is The recursive argument
## if we use find_all() it searches through the html
## going through children of each tag to find a particular tag or search

## In order to find the direct children use recursive =False

## find() is same as find_all()
## find returns only 1 search result or the first result it encounters

## find_all(limit=1)==find()

## returns the first a it encounters
print (html.find('a'))

## returns the first among them in the list
print (html.find(['a','b']))

## using True values 
print ("\nTrue\n",html.find(class_=True))

print ("\nusing class_\n",html.find(class_="sister"))
print ("\nusing regex \n",html.find(class_=re.compile('.*')))


## using find_parents and find_all_parents
## all these arguments can also be written as html.find().find_parents() or html.find().find_parent()

a=html.find('a')
print (a)
## without any arguments it will print list of all parents 
print ("\nprinting all the parents of <a>\n",a.find_parents())
print ('\n',a.find_parents('p'))

## find first parent of the tag
print ("\nprint the parent of a in <p>\n\n",a.find_parent('p'))
## both are same
print ("\nprints the same result as the above\n\n",a.find_parent())
## different
print ("\nthis is different due to the argumnent\n\n",a.find_parent('body'))



## find_next_siblings and find_next_sibling
## returns all the next and previous siblings

print ("\n\n",html.find('a').find_next_siblings())
print ("",html.find('a').find_next_sibling())
print ("",html.find('a',id='link3').find_previous_siblings())
print ("",html.find('a',id='link3').find_previous_sibling())

