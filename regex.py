import re
from urllib.request import urlopen


## they are used to define a language family 
## with certain characteristics, the so-called 
## regular languages.

# a simple regular expression

r=r'abhishek'
print (r)

## re.search() in regular expression
## gives whether the sub-string is present in string or not
## searching a particular word in string

string="At mat cat and a rat can't be friends."
print (string)
sub_string=input("Enter the string to match : ")
if re.search(sub_string,sub_string):
	print ((" %s is present ")%sub_string)
	print (re.search(sub_string,string))
else:http://www.summet.com/dmsi/html/codesamples/addresses.html
	print ("No match")

## re.compile()
## what does it do??
## it converts pattern into pattern object
## searching a speacial word such that it ends with "at"
name="Abhishek"
check=re.compile("[A-Za-z]")
print (check.search(name))

sub_string=r'.at'
print (re.search(sub_string,string))


## matching and searching set of strings
## [] >> means set of strings 
## the possible combination such as aat,aas,aad,mat..............,cad will be searched in string
sub_string=r'[amc]a[tsd]'
string=["my name is mad aas","go home cat ","I am batman"]

## in this first case 2 search results occur 
## but "mad " is searched before "aas" i.e. every possible sub_string is matched with every word in the string 

for i in string:
	if re.search(sub_string,i):
		print("Found")
		print (re.search(sub_string,i))
	else:
		print ("None")

## searching multiple lines at once i.e. lines containing new line character
## getting all line or names that are starting with J

with urlopen('https://www.python-course.eu/simpsons_phone_book.txt') as f:
	for line in f:
		line=line.decode('utf-8')
		if re.search(r'J.*',line):
			print (line)

## we can match by using "search" operation which will find
## substring anywhere but what if we only want to search in end and begining only
## re.match() matches at the begining of the string only

s1="Mayer is very common"
s2="He is called the Meyer in German"

## searching anywhere in the string
print (re.search(r'M[ae]y[ei]r',s1))
print (re.search(r'M[ae]y[ei]r',s2))

## matching only in the begining

print (re.match(r'M[ae]y[ei]r',s1))
print (re.match(r'M[ae]y[ei]r',s2))

## but re.match(substring,string) fails when many lines are used
## as it avoids newline character thus it checks only begining of string not in
## the begining of everyline

print (re.match(r'M[ae]y[ei]r',s2+'\n'+s1,re.M))
## to check in the begining of every line use caret operation i.e. ^
print (re.search(r'M[ae]y[ei]r',s2+'\n'+s1,re.M))

## use re.MULTILINE or re.M for reading more than one lines

## matching in end only in contrast to ^ we have $ to read in 
## end just before the new line character

print (re.search(r'Python\.$',"i love Python."))
print (re.search(r'[Pp]ython\.$',"i love Python and Perl."))
print (re.search(r'[pP]ython\.$','I love Python.\n  But some not.',re.M))


## optional character matching in string 
## we can specify some characters as optional by sign '?'
## eg. r'M[ae]y?er'
## here 'y' is optinal 
## for a sub-string in the string to be optional
## r'feb(ruary)?' where 'ruary' is optional 

print (re.search('[Ff]eb(ruary)?',"This is the month of febr"))


## A quantifier after a token, which can be a single character or group in brackets, 
## specifies how often that preceding element is allowed to occur. The most common quantifiers are
## the question mark ?
##  * ,which is derived from the Kleene star
## and the plus sign +, derived from the Kleene cross

## re.group == used for grouping  a part of regex using paranthesis so that we can apply operation on whole group
## instead of single character

mo=re.search("[0-9]+", "Customer number: 232454, Date: February 12, 2011")
print (mo)
## returns pattern that has been completely matched
print (mo.group())
## returns starting and ending position of match
print (mo.span())
print (mo.start())
print (mo.end())


## important example

mo=re.search("([0-9]+).*:(.*)", "Customer number: 232454, Date: February 12, 2011")
print (mo.group())
print (mo.group(2))
print (mo.group(1))

## another example
## grouping and name back references

txt=["<composer>Wolfgang Amadeus Mozart</composer>",
"<author>Samuel Beckett</author>",
"<city>London</city>"]
for i in txt:
	mo=re.search(r'<([A-Za-z]*)>.*</\1>',i)
	#mo=re.search(r"<(.*)>[A-Za-z]*.*[A-Za-z]*</\1>",i)
	print (mo)


list = ["555-8396 Neu, Allison", 
     "Burns, C. Montgomery", 
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]


for line in list:
	mo=re.search(r'([0-9-]+)\s([A-Za-z]*),\s([A-Za-z]*)',line)
	if mo:
		print (mo.group(3),mo.group(1),mo.group(2))


##different functions used in regex

## re.findall()
## matches all the patterns in the string returns them

example_string="""Jessica is 15 year old , and Daniel is 27 year old .
Edward is 97 , and his grand father , Oscar , is 102.

"""
print (re.findall(r'[A-Z][a-z]*',example_string))
print (re.findall(r'[0-9]+',example_string))

example_string="we need this info for information"
print (re.findall(r'info',example_string))

## finditer : returns an iterator yielding a match object for each match

for i in re.finditer("info",example_string):
	print (i)

## match or search a single character in string
## any digit that is repeated 5 to 7 times in example_string

example_string="123456 34567 56778 9 567 "

print (re.findall('\d{5,7}',example_string))



## example of phone number verification
## eg :- any phone number is of form 132-456-7891
## then it must have r'\d{3}-\d{3}-\d{4}'
## or r'[0-9]*-[0-9]*-[0-9]*'

phone_number="132-456-7875"
print (re.search(r'[0-9]*-[0-9]*-[0-9]*',phone_number))
## or 
print (re.findall(r'\d{3}-\d{3}-\d{4}',phone_number))

## finding a full name i.e. Abhishek Chauhan
## re.search(r'[A-Z][a-z]*\s[A-Z][a-z]')
## or re.findall(r'\w{2,25}\s\w{2,25}')
name="Abhishek Chauhan"
print (re.findall(r'\w{2,25}\s\w{2,25}',name))
## or
print (re.search(r'[A-Z][a-z]*\s[A-Z][a-z]*',name))

## combining regex and urllib
## using regex with urllib module

from urllib.request import urlopen;
import re

url="http://www.summet.com/dmsi/html/codesamples/addresses.html"
client=urlopen(url)
html=client.read()
html=html.decode('utf-8')
number= (re.findall(r'.\d{3}. \d{3}-\d{4}',html))
for no in number:
	print(no)

