import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/svet"

driver.get(url)

time.sleep(10)

svets = driver.find_elements(By.CLASS_NAME, '_Ud0k U4KZV')

parsed_data = []

for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'span.ui-GPFV8 qUioe ProductName ActiveProduct').text
        price = svet.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU KIkOH').text
        link = svet.find_element(By.CSS_SELECTOR, 'a.class=ui-GPFV8 qUioe ProductName ActiveProduct').get_attribute('href')
    except:
        print('Произошла ошибка при парсинге')
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("svet.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Название','Цена','Ссылка на товар'])
    writer.writerows(parsed_data)
