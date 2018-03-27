from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import Spider
from wikiSpider import Spider, Article

class ArticleSpider(Spider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://en.wikipedia.org/wiki/Main_Page",
                  "http://en.wikipedia.org/wiki/Python_%28programming_languge%29"]
    rules = [Rule(SgmlLinkExtractor(allow=('(/wiki/)((?!:).)*$'),),
                                        callback="parse_item", follow=True)]


    def parse(self, response):
        item = Article()
        title = response.xpath('//h1/text()')[0].extract()
        print("Tittle is: " + title)
        item['title'] = title
        return item