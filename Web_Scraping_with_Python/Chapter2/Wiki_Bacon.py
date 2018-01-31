# 运行代码，将会看到维基百科上凯文.贝肯词条里指向其他词条的连接

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://www.wikipedia.org/wiki/Kevin_Bacon")
    bsObj = BeautifulSoup(html, "html.parser")
    for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!).)*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])
links = getLinks("/wiki/Kenvin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
