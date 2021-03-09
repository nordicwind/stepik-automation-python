from selenium import webdriver
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим текст переменной Х
    f_name = browser.find_element_by_css_selector('input[name="firstname"]')
    f_name.send_keys("Ivan")

    paste_value = calc(x_value)

    #Заполняем форму
    input_field = browser.find_element_by_css_selector('#answer')
    input_field.send_keys(paste_value)

    #Скроллим чтобы было видно остальные контролы
    submit_button = browser.find_element_by_css_selector('button.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)

    # Чекаем чекбоксы и радиокноку
    robot_checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    robot_checkbox.click()

    radio_button = browser.find_element_by_css_selector('#robotsRule')
    radio_button.click()

    # ждем загрузки страницы
    time.sleep(1)

    #Отправляем форму
    submit_button.click()

finally:
    #Debug
    print(x_value)
    print(paste_value)
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()