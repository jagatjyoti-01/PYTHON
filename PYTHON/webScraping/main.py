#step-0: install all the requerment
#pip install request
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
url="https://www.codewithharry.com/"

#step 1:get the html
r=requests.get(url)   #request is module in py by which we caan use get,post method
htmlcontaint=r.content
# print(htmlcontaint

#step 1:parse the html
soup=BeautifulSoup(htmlcontaint,'html.parser')
# print(soup)
# print(soup.prettify)

#step3: html tree traversial
#get tittle of html
title=soup.title
# print(title)   
# print(type(title))  # 1.tag

# print(type(soup)) # 3.BeautifulSoup
# print(type(title.string))# 2.navigableString

#commonly used  object
# 1.tag
# 2.navigableString
# 3.BeautifulSoup
# 4.comennt

# get all the paragraph
paras=soup.find_all('p')
# print(paras)

# get all the anchor tag
anchar=soup.find_all('a')
#print(anchar)

#get classes of any elment of HTMl page
# print(soup.find('p')['class'])
# print(soup.find('p')['id'])  

#find the element with class name let lead
#print(soup.find_all('p',class_="hidden"))

#print(soup.find('p').get_text())
#find method used to 
#print(soup.get_text())

#get all the link on the page
# anchor=soup.find_all('a')
# all_links=set()
# for link in anchor:
#     if(link.get('href')!='#'):
#         linktext="https://www.codewithharry.com/" +link.get('href')
#         print(linktext)
    # print(link.get('href'))
        
#comment
# markup="<p><!--this is comment  --></p>"
# soup2=BeautifulSoup(markup)
# print(soup2.p.string)

var=soup.find(id='__next')
#print(var)
#print(var.contents)
for item in var:
    print(item)




