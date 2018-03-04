from bs4 import BeautifulSoup as soup 
from urllib2 import urlopen
import re

url="https://www.bloombergquint.com/stock/901145/indian-oil-corp"

client=urlopen(url)
html_page=client.read()
client.close()
containers=soup(html_page,"html.parser")
container=containers.findAll("div",{"class":"stocktile-bse-nse-container"})[0]
stock_price=container.findAll("div",{"class":"stock-body"})
stock_price=stock_price[0]

print stock_price

x1=stock_price.findAll("span",{'class':"stock-type"})
x2=stock_price.findAll("span",{'class':"stock-price"})
new_x=str(x1[0])
print x2[0]
y=re.sub("<.*?>","",new_x)
print y

