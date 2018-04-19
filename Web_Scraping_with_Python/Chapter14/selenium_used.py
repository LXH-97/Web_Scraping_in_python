# 在Tor中使用Selenium和PhantomJS
# 增加service_args参数设置代理端口，让Selenium通过端口9150连接网站

from selenium import webdriver
service_args = [ '--proxy=localhost:9150', '--proxy-type=socks5', ]
driver = webdriver.PhantomJS(executable_path='<Path to Phantom JS>',
                             service_args=service_args)

driver.get("http://icanhazip.com")
print(driver.page_source)
driver.close()

