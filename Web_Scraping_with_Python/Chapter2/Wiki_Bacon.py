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

"""
空行隔开的两行代码是后者调用前者
有一段时间的分别阅读，才理解了这段代码
getLinks打开连接并打印文本
while循环带开一个个链接
也就是两段代码会打印出所有的文本
"""