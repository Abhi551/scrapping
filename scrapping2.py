#scrapping flipkart in python 2
from bs4 import BeautifulSoup as soup 
from urllib2 import urlopen

url="https://www.flipkart.com/search?q=iphone%206&otracker=start&as-show=on&as=off"

client=urlopen(url)
html=client.read()
client.close()

html_page=soup(html,'html.parser')

containers=html_page.findAll('div',{'class':"col _2-gKeQ"})
print len(containers)

filename="scrapping.csv"
f=open(filename,'w')
headers="product_name , product_price ,product_rating"

f.write(headers)

for container in containers:
	#print container.div.img['alt']
	name_container=container.div.a.findAll("div",{"class":"_3BTv9X"})[0]
	product_name=name_container.img['alt']
	product_price=container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})[0].text
	product_price=product_price[1:]
	rating_container=container.div.findAll("div",{"class":"hGSR34 _2beYZw"})[0].text
	rating_container=rating_container[:3]
	print "name of the product \t",product_name
	print "price of the product \t",product_price
	print  "rating of the product \t",rating_container
	f.write(product_name.replace(',',"|")+","+product_price.replace(",",'|')+","+rating_container.replace(',',"|")+"\n")

f.close()


