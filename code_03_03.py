from selenium import webdriver
import time

url = 'http://www.phptravels.net/offers'

driver = webdriver.Chrome()
driver.get(url)

b_tags = driver.find_elements_by_tag_name('b')

b_tags_prices = []

for price in b_tags:
	if not price:
		continue
	b_tags_prices.append(price.text)
	
print(b_tags_prices)

clean_price = []

for p in b_tags_prices:
	if p.startswith('USD'):
		price_list = p[5:]
		integer_price_list = int(price_list.replace(",", ''))
		clean_price.append(integer_price_list)
		
print(sorted(clean_price))

time.sleep(1)
driver.close()

