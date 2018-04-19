# 一个带拖放动作的网站单元测试
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver import ActionChains
import unittest

class TestAddtion(unittest.TestCase):
    driver = None
    def setUp(self):
        global driver
        driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
        url = 'http://pythonscraping.com/pages/javascript/draggableDemo.html'
        driver.get(url)

    def tearDown(self):
        print("Tearing down the test")

    def test_drag(self):
        global driver
        element = driver.find_element_by_id("draggable")
        target = driver.find_element_by_id("div2")
        actions = ActionChains(driver)
        actions.drag_and_drop(element, target).perform()

        self.assertEquals("You are definitely not a bot!", driver.find_element_by_id("message").text)

if __name__ == '__main__':
    unittest.main()

