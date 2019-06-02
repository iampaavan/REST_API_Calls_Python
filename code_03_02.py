from selenium import webdriver
import time

url = 'https://www.seleniumhq.org'

driver = webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(10)

element = driver.find_element_by_xpath('//*[@id="choice"]/tbody/tr/td[1]/center/a[1]/img')
element.click()

driver.back()

search_bar = driver.find_element_by_id('q')
search_bar.clear()

search_bar.send_keys('webdriver')
go_button = driver.find_element_by_id('submit')
go_button.click()

time.sleep(3)

driver.close()