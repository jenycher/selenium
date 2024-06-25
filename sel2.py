from selenium import webdriver
import time

#С помощью time мы можем делать задержки в программе
# Создаём объект браузера, через который мы будем действовать.

#Если мы работаем с Chrome
browser = webdriver.Chrome()
#Если мы работаем с Firefox
#browser = webdriver.Firefox()

#Настраиваем возможность зайти на сайт.
browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
#В кавычках указываем URL сайта, на который нам нужно зайти
browser.save_screenshot("dom.png") #делаем снимок экрана
time.sleep(5)   #Задержка в 5 секунд

browser.get("https://ru.wikipedia.org/wiki/Selenium")
browser.save_screenshot("selenium.png") #делаем снимок экрана
time.sleep(3)   #Задержка в 3 секунд
browser.refresh()   #перезагрузка страницы

