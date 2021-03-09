from selenium import webdriver
import math
import time

# Функция расчета calc(x)
def calc(z):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим текст переменной Х
    num1 = browser.find_element_by_css_selector("#num1")
    num1_value = secret_element.text
    print(num1_value)
    
    # Расчитываем переменную calc(x) - secret_value
    x = secret_value
    y = calc(x)

    #Заполняем форму
    input_field = browser.find_element_by_css_selector('#answer')
    input_field.send_keys(y)

    # Чекаем чекбоксы и радиокноку
    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    robot_checkbox.click()

    radio_button = browser.find_element_by_css_selector('#robotsRule')
    radio_button.click()

    # ждем загрузки страницы
    time.sleep(1)

    #Отправляем форму
    submit_button = browser.find_element_by_css_selector('button.btn-default')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()