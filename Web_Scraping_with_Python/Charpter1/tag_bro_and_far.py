#The deal of brother tag and father tag

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html)
print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)