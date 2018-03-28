from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org"+articleUrl)
    bsObj = BeautifulSoup(html)
    return bsObj.find("div", {"id":"bodyContent"}).findAll("a",
                      href=re.compile("^(/wiki/)((?!:).)*$"))

def getHistoryIPs(pageUrl):
    # 编辑历史页面URL链接格式
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    pageUrl = pageUrl.replace("/wiki/", "")
    historyUrl = "http://wikipedia.org/w/index.php?title="+pageUrl+"&action=history"
    print("history url is :"+historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html)
    # 找出class属性是“mw-anonuserlink”的链接
    # 它们用IP地址代替用户名
    ipAddresses = bsObj.findAll("a", {"class":"mw-anonuserlink"})
    addressList = set()
    for ipAddressList in ipAddresses:
        addressList.add(ipAddresses.get_text())
    return addressList

links = getLinks("wiki/Python_(programming_language)")

while(len(links)>0):
    for link in links:
        print("------------")
        historyIPs = getHistoryIPs(links.attrs["href"])
        for historyIP in historyIPs:
            print(historyIP)
