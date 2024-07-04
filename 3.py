from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
#
# for svet in svets:
#     try:
#         name = svet.find_element(By.CSS_SELECTOR, 'div.wYUX2').text
#         price = svet.find_element(By.CSS_SELECTOR, 'div.pY3d2').text
#         link = svet.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
#     except:
#         print('Произошла ошибка при парсинге')
#         continue
#
#     parsed_data.append([name, price, link])
#
# driver.quit()
#
# with open("svet.csv", 'w', newline='', encoding='utf-8-sig') as file:
#     writer = csv.writer(file)
#     writer.writerow(['Название','Цена','Ссылка на товар'])
#     writer.writerows(parsed_data)

# Ожидание появления элемента на странице
try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.pY3d2')))
    print("Элементы на странице найдены")
except:
    print("Элементы не были найдены в течение 10 секунд")
