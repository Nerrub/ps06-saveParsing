import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/divany-i-kresla"

driver.get(url)

time.sleep(5)

divans = driver.find_elements(By.CLASS_NAME, 'LlPhw')

parsed_data = []

for divan in divans:
    try:
        name = divan.find_element(By.CSS_SELECTOR, '.lsooF').text
        price = divan.find_element(By.CSS_SELECTOR, '.pY3d2').text
        link = divan.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
    except:
        print('Произошла ошибка при парсинге')
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("divan.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Название','Цена','Ссылка на товар'])
    writer.writerows(parsed_data)
