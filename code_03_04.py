from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

url = 'http://automationpractice.com/index.php?id_category=3&controller=category'

driver = webdriver.Chrome()
driver.get(url)
driver.fullscreen_window()

product_containers = driver.find_elements_by_class_name('product-container')

for index, product_container in enumerate(product_containers):
	hover = ActionChains(driver).move_to_element(product_container)
	hover.perform()
	driver.implicitly_wait(5)
	driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span'%(index+1)).click()
	time.sleep(2)
	driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span/span').click()
	time.sleep(2)
	
driver.find_element_by_xpath('//*[@id="header"]/div[3]/div/div/div[3]/div/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="order"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="center_column"]/p[2]/a[1]/span').click()

time.sleep(5)
driver.close()