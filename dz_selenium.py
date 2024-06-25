from selenium import webdriver
from selenium.webdriver import Keys #Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By #Библиотека с поиском элементов на сайте
import time
import random

# 1 Запрос пользователя
search_query = input("Введите запрос для поиска на Википедии: ")

# Инициализация драйвера браузера Chrome
browser = webdriver.Chrome()

# 2 Поиск информации на Википедии
browser.get("https://ru.wikipedia.org/")
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)
time.sleep(10)


# Получение результатов поиска
#results = browser.find_elements("mw-parser-output")
#for result in results:
 #   print(result.text)

# Закрытие браузера
#browser.quit()


# Цикл для взаимодействия с пользователем
while True:
    print("Выберите действие:")
    print("1. Листать параграфы текущей статьи")
    print("2. Перейти на одну из связанных страниц")
    choice = input("Введите номер действия (1/2): ")

    if choice == '1':
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print(paragraph.text)
    elif choice == '2':
        related_pages = browser.find_elements(By.CLASS_NAME, "mw-search-result")[0].find_elements(By.TAG_NAME, "a")
        random_page = random.choice(related_pages)
        random_page_url = random_page.get_attribute("href")
        browser.get(random_page_url)
        time.sleep(5)
    else:
        print("Некорректный ввод. Попробуйте еще раз.")

# Закрытие браузера
#browser.quit()