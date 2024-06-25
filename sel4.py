#Попробуем брать контент с сайта.

#Импортируем библиотеки и настраиваем браузер:
from selenium import webdriver
from selenium.webdriver import Keys #Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By #Библиотека с поиском элементов на сайте
import time
import random


#Если работаем в Firefox
#browser = webdriver.Firefox()

#Если работаем в Chrome
browser = webdriver.Chrome()

#Далее одинаково для всех браузеров
#Сразу заходим на страницу солнечной системы
browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

#2. Исследуем код параграфов на странице. Находим тег.
#3. Пишем новый код:

paragraphs = browser.find_elements(By.TAG_NAME, "p")
#Для перебора пишем цикл
#for paragraph in paragraphs:
#    print(paragraph.text)
#    input()

#4. Запускаем программу. Каждый раз, нажимая на клавишу Enter, мы будем получать последующий параграф (абзац) текста статьи.


#5. Удаляем код для параграфов и пишем новый код:
hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    cl = element.get_attribute("class") #Чтобы искать атрибут класса
    if cl == "hatnote navigation-not-searchable":
        hatnotes.append(element)

print(hatnotes)
hatnote = random.choice(hatnotes)

#Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
#print(link)
browser.get(link)
time.sleep(5)

#6. Запускаем программу несколько раз, чтобы проверить переход на рандомные статьи.