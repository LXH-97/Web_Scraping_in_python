from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path='/path/to/download/phantomjs-1.9.8-macosx/bin/phantomjs')
driver.get("http://pythonscraping.com/pages/javascripts/ajaxDemo.html")
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()

