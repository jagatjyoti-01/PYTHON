import requests
from bs4 import BeautifulSoup
url="https://suravi.org.in/"

r=requests.get(url)
htmlcontaint=r.content
#print(htmlcontaint)


soup=BeautifulSoup(htmlcontaint,'html.parser')
# print(soup)
# print(soup.prettify)

var=soup.find(id="activity")
#print(var.parents)
#print(var)
#print(var.contents)
#for item in var.parents:
    #print(item)
    #print(item.name)
print(var.next_sibling)
