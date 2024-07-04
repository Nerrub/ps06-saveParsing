import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By


# class DivannewparsSpider(scrapy.Spider):
#     name = "divannewpars"
#     allowed_domains = ["https://divan.ru"]
#     start_urls = ["https://www.divan.ru/category/svet"]
#
#     def parse(self, response):
#         divans = response.css('div._Ud0k')
#         for divan in divans:
#             yield {
#                 'name' : divan.css('div.wYUX2 span::text').get(),
#                 'price' : divan.css('div.pY3d2 span::text').get(),
#                 'url': divan.css('a').attrib['href']
#             }

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/svet"

driver.get(url)

time.sleep(3)

svets = driver.find_elements(By.CLASS_NAME, 'WdR1o')

parsed_data = []

for svet in svets:
    try:
        name = svet.find_element(By.CSS_SELECTOR, 'span.ui-GPFV8 qUioe ProductName ActiveProduct').text
        price = svet.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU KIkOH').text
        link = svet.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8 qUioe ProductName ActiveProduct').get_attribute('href')
    except:
        print('Произошла ошибка при парсинге')
        continue

    parsed_data.append([name, price, link])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Название','Цена','Ссылка на товар'])
    writer.writerows(parsed_data)
