from selenium import webdriver
import math
import time

# Функция расчета calc(x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим текст переменной Х
    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    #Debug print(x)
    
    # Расчитываем переменную calc(x) - Y
    y = calc(x)
    #Debug print(y)

    #Заполняем форму
    input_field = browser.find_element_by_css_selector('#answer')
    input_field.send_keys(y)

    # Чекаем чекбоксы и радиокноку
    robot_checkbox = browser.find_element_by_css_selector('label[for="robotCheckbox"]')
    robot_checkbox.click()

    radio_button = browser.find_element_by_css_selector('label[for="robotsRule"]')
    radio_button.click()

    # ждем загрузки страницы
    time.sleep(2)

    #Отправляем форму
    submit_button = browser.find_element_by_css_selector('button.btn-default')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()