from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_stealth import stealth
from time import sleep
import math
from bs4 import BeautifulSoup
import os
import requests
import re
import xlsxwriter
vacantion_search_url = 'https://trudvsem.ru/vacancy/search'
num_pages = 0
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

book = xlsxwriter.Workbook(r"./data/parced_data.xlsx")
page = book.add_worksheet("данные")

page.set_column("A:A", 20)
page.set_column("B:B", 50)
page.set_column("C:C", 20)
page.set_column("D:D", 20)
page.set_column("E:E", 20)
page.set_column("F:F", 20)
page.set_column("G:G", 20)
page.set_column("H:H", 20)
page.set_column("I:I", 20)
page.set_column("J:J", 20)


# options.add_argument("--headless")

#options.add_experimental_option("excludeSwitches", ["enable-automation"])
#options.add_experimental_option('useAutomationExtension', False)

driver = webdriver.Chrome(options=options)  #

stealth(driver,
        languages=["ru", "ru-RU"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

driver.get(vacantion_search_url)
start_button = driver.find_element(By.XPATH, "//button[@class='search-content__button']")
start_button.click()
sleep(3)
if num_pages == 0:
    try:
        num_vacancy_text = driver.find_element(By.CLASS_NAME, 'ib-filter__result-counter').text
        num_vacancy = int(''.join(num_vacancy_text[:num_vacancy_text.rfind(' ')].split()))
        print(num_vacancy_text)
        for _ in range(math.ceil(num_vacancy / 10)):
            sleep(1)
            element = driver.find_elements(By.CLASS_NAME, 'button_secondary')
            for e in element:
                if e.text == 'Загрузить ещё':
                    driver.execute_script("arguments[0].click();", e)
        for i in range(num_vacancy):
            elem = driver.find_element(By.XPATH, '//div[@class="search-results-simple-card mb-1"]')
            info_div = elem.find_elements(By.XPATH,
                                          '//div[@class="search-results-simple-card__wrapper search-results-simple-card__wrapper_column"]')

            soup_vacancy_info = BeautifulSoup(info_div[i].get_attribute('innerHTML'), 'lxml')
            employer, region = list(
                map(lambda x: x.text, soup_vacancy_info.find_all('div', {'class': 'content_small content_clip'})))

            driver.execute_script("arguments[0].click();", elem)
            soup = BeautifulSoup(driver.page_source, "lxml")
            vacancy_name_html = soup.find('a', {'class': "link link_title"})
            if not vacancy_name_html:
                while not vacancy_name_html:
                    soup = BeautifulSoup(driver.page_source, "lxml")

            vacancy_name = vacancy_name_html.text
            print(vacancy_name)
            salary = soup.find('span', {'class': 'content__section-subtitle search-results-full-card__salary'}).text.strip()
            print(salary)
            date = soup.find('span', {'class': 'content_small content_pale'}).text
            date = date[date.find(' ') + 1:]
            print(date)
            print(region)
            print(employer)
            vacancy_descr = soup.find('div', {'class': "tabs__content tabs_active", 'id': "vacancy-details"}).text.split()
            vacancy_descr = ' '.join(list(map(lambda x: x.strip(), vacancy_descr)))
            print(vacancy_descr)
            requirements = vacancy_descr[
                           vacancy_descr.find('Требования к кандидату'):vacancy_descr.find('Данные по вакансии')]
            print('requirements:')
            print(requirements)
            print('\n')
            if 'Опыт работы' in requirements:
                print('experience:')
                experience = requirements[requirements.find('Опыт работы'):]
                experience = experience[:[m.start() for m in re.finditer(' ', experience)][4]]
                print(experience)
            else:
                experience = ''
                print(experience)

            if 'График работы' in vacancy_descr:
                print('schedule:')
                schedule = vacancy_descr[vacancy_descr.find('График работы'):]
                schedule = schedule[:[m.start() for m in re.finditer(' ', schedule)][2]]
                print(schedule)
            else:
                schedule = ''
                print(schedule)

            data = [vacancy_name, vacancy_descr, salary, date, region, employer, requirements, experience, schedule]
            column_num = 0
            for col in data:
                page.write(i, column_num, col)
                column_num += 1

            print(i)
    except:
        print('Завершено')
    book.close()