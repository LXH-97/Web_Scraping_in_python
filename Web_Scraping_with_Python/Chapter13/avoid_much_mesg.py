from urllib.request import urlopen
from bs4 import BeautifulSoup
import unittest


class TestWikipedia(unittest.TestCase):
    bsObj = None
    url = None

    def test_PageProperties(self):
        global bsObj
        global url

        url = "http://en.wikipedia.org/wiki/Monty_Python"
        # 测试遇到的前100个页面
        for i in range(1, 100):
            bsObj = BeautifulSoup(urlopen(url))
            titles = self.titleMatchesURL()
            self.assertEquals(titles[0], titles[1])
            self.assertTrue(self.contentExits())
            url = self.getNextLink()
        print("Done!")

    def titleMatchesURl(self):
        global bsObj
        global url
        pageTitle = bsObj.find("h1").get_text()
        urlTitle = url[(url.index("/wiki/")+6):]
        urlTitle = unquote(urlTitle)
        return [pageTitle.lower(), urlTitle.lower()]

    def contentExists(self):
        global bsObj
        content = bsObj.find("div", {"id":"mw-content-text"})
        if content is not None:
            return True
        return False

    def getNextLink(self):
        pass

# 使用第五章介绍的方法返回随机链接

if __name__ == '__main__':
    unittest.main()

