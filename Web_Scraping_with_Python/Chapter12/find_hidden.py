# 查找隐含链接和隐含输入字段

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

driver = webdriver.PhantomJS(executable_path='')
driver.get("http://pythonscraping.com/pages/itstrap.html")
links = driver.find_element_by_tag_name("a")
for link in links:
    if not link.is_dispayed():
        print("The link "+link.get_attribute("href")+" is a trap")

fields = driver.find_element_by_tag_name("input")
for field in fields:
    if not field.is_displayed():
        print("Do not change value of "+field.get_attribute("name"))

