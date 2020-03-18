# https://medium.com/@NorthBei/%E5%9C%A8windows%E4%B8%8A%E5%AE%89%E8%A3%9Dpython-selenium-%E7%B0%A1%E6%98%93%E6%95%99%E5%AD%B8-eade1cd2d12d
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.google.com")

element = driver.find_element_by_name("q")
element.send_keys("hello world")
element.submit()

# driver.close()