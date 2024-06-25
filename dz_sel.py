from selenium import webdriver
from selenium.webdriver import Keys  # Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By  # Библиотека с поиском элементов на сайте
import time
import random

def list_paragraphs(browser):
    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    for paragraph in paragraphs:
        print(paragraph.text)

def go_to_related_page(browser):
    related_links = browser.find_elements(By.CSS_SELECTOR, "#bodyContent a")
    related_links = [link for link in related_links if link.get_attribute("href") and "wikipedia.org/wiki/" in link.get_attribute("href")]
    if related_links:
        random_page = random.choice(related_links)
        random_page_url = random_page.get_attribute("href")
        browser.get(random_page_url)
        time.sleep(3)
    else:
        print("Нет связанных страниц.")

def main():
    # 1 Запрос пользователя
    search_query = input("Введите запрос для поиска на Википедии: ")

    # Инициализация драйвера браузера Chrome
    browser = webdriver.Chrome()

    try:
        # 2 Поиск информации на Википедии
        browser.get("https://ru.wikipedia.org/")
        search_box = browser.find_element(By.ID, "searchInput")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)

        # Цикл для взаимодействия с пользователем
        while True:
            print("\nВыберите действие:")
            print("1. Листать параграфы текущей статьи")
            print("2. Перейти на одну из связанных страниц")
            print("3. Выйти из программы")
            choice = input("Введите номер действия (1/2/3): ")

            if choice == '1':
                list_paragraphs(browser)
            elif choice == '2':
                go_to_related_page(browser)
            elif choice == '3':
                print("Выход из программы.")
                break
            else:
                print("Некорректный ввод. Попробуйте еще раз.")

    finally:
        # Закрытие браузера
        browser.quit()

if __name__ == "__main__":
    main()
