import time
import csv

from selenium import webdriver
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()


url = "https://tomsk.hh.ru/vacancies/programmist"

driver.get(url)


time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--z_UXteNo7bRGzxWVcL7y')

parsed_data = []

for vacancy in vacancies:
    try:
       title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--c1Lay3KouCl7XasYakLk serp-item__title-link').text
       company = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-serp__vacancy-employer').text
       salary = vacancy.find_element(By.CSS_SELECTOR, 'span.fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2').text
       link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except:
       print("произошла ошибка при парсинге")
       continue
    parsed_data.append([title, company, salary, link])

driver.quit()

with open("hh.csv", 'w',newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'название компании', 'зарплата', 'ссылка на вакансию'])
    writer.writerows(parsed_data)