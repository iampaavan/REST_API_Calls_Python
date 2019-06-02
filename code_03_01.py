from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://www.google.com'

driver = webdriver.Chrome()
driver.get(url)

element = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div/div[1]/div/div[1]/input')
print(f"FIND ELEMENT BY NAME: {element}")
element.clear()

element.send_keys('Accenture')
element.send_keys(Keys.RETURN)

time.sleep(1)

driver.close()
