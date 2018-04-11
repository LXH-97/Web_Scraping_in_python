import time
from urllib.request import urlretrieve
import subprocess
from selenium import webdriver

# 创建新的Selenium driver
driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>')
# PhantomJS查找元素有是时候会有问题而Firefox不会
# 去掉下行注释，用selenium打开firefox
# driver = webdriver.Firefox()

driver.get(
    "http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
time.sleep(2)

# 单击图书预览按钮
driver.find_element_by_id("sitbLogoImg").click()
imageList = set()

# 等待页面加载完成
time.sleep(5)
# 当向右箭头可以点击时，开始翻页
while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner")\
        .get_attribute("style"):
    driver.find_element_by_id("sitReaderRightPageTurner").click()
    time.sleep(2)
    # 获取已经加载的新页面（一次可加载多个页面，但是重复的页面不能加载到集合中）
    pages = driver.find_element_by_xpath("//div[@class='pageImage']/div/img")
    for page in pages:
        image = page.get_attribute("src")
        imageList.add(image)

driver.quit()

# 用Tesseract处理我们收到的图片URL链接
for image in sorted(imageList):
    urlretrieve(image, "page.jpg")
    p = subprocess.Popen(["tesseract", "page.jpg", "page"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    p.wait()
    f = open("page.txt", "r")
    print(f.read())

