from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


try: 
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим текст переменной Х
    num1 = browser.find_element_by_css_selector("#num1")
    num1_value = num1.text

    # Находим текст переменной Y
    num2 = browser.find_element_by_css_selector("#num2")
    num2_value = num2.text

    #Складываем 2 переменные
    answer = int(num1_value) + int(num2_value)

    # Ищем значение в дропдауне и отправляем форму
    answer_dropdown = Select(browser.find_element_by_css_selector('#dropdown'))
    answer_dropdown.select_by_visible_text(str(answer))
   
    # ждем загрузки страницы
    time.sleep(1)

    #Отправляем форму
    submit_button = browser.find_element_by_css_selector('button.btn-default')
    submit_button.click()

finally:
    print(num1_value)
    print(num2_value)
    print(answer)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()