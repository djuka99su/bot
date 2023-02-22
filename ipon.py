from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os
import time
import threading
#Change


ipon = os.chdir('C:/Users/ndjur/OneDrive/Desktop/ipon')
ipon_folders = os.listdir(ipon)


def task(num):

	driver = webdriver.Chrome('C:/chromedriver')
	driver.get('https://iponcomp.com/shop/group/mobile-tablet-photo-watch-drone/9')
	driver.maximize_window()
	driver.implicitly_wait(5)
	categories = driver.find_elements(By.CLASS_NAME, 'shop-categories--subcategory__item')
	category_name = categories[num].find_element(By.CLASS_NAME, 'shop-category-card--subcategory__title').text.replace('/', '-')
	print(category_name)
	categories[num].find_element(By.TAG_NAME, 'a').click()
	time.sleep(1)
	try:
		page_num = driver.find_element(By.CLASS_NAME, 'forum-pagination__pages-all')
		for i in range(int(page_num.text)-1):
			show_more = driver.find_element(By.CLASS_NAME, 'product-list__show-more-button-wrapper')
			button = WebDriverWait(show_more, 10).until(EC.element_to_be_clickable((By.TAG_NAME, 'button')))
			driver.execute_script("arguments[0].click();", button)
	except NoSuchElementException:
		pass

	time.sleep(3)
	items = driver.find_elements(By.CLASS_NAME, 'product-list__grid--cards__item')
	for i, item in enumerate(items, start=1):
		img = item.find_element(By.CLASS_NAME, 'shop-card__image-block')
		img = img.find_element(By.TAG_NAME, 'img')
		img_url = img.get_attribute('data-src')
		item_name = item.find_element(By.CLASS_NAME, 'shop-card__title').text
		item_price = item.find_element(By.CLASS_NAME, 'shop-card__price').text.replace(' ', '').replace('Ft', '')
		with open(f'C:/Users/ndjur/OneDrive/Desktop/ipon/ipon_dir/Mobile, tablet, photo, watch, drone/{category_name}/{category_name}.txt', 'a+', errors='ignore') as f:
			f.write(f'{i}.\n')
			f.write(item_name + '\n')
			f.write(item_price + '\n')
			f.write(img_url + '\n')
	print(f'Process with {category_name} has been finished!')


def threads(num1, num2):

	threads = []

	for i in range(num1, num2):
		t = threading.Thread(target=task, args = (i,))
		threads.append(t)


	for t in threads:
	    t.start()

	# Wait for all threads to finish
	for t in threads:
		t.join()

threads(0, 6)
threads(6, 12)
threads(12, 15)
# task()

	
