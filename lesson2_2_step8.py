from selenium import webdriver
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Заполняем форму
    f_name = browser.find_element_by_css_selector('input[name="firstname"]')
    f_name.send_keys("Ivan")

    l_name = browser.find_element_by_css_selector('input[name="lastname"]')
    l_name.send_keys("Sokolov")

    email = browser.find_element_by_css_selector('input[name="email"]')
    email.send_keys("email@asdawdeqwdqwd.com")

    #Выбираем файл
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.py')

    select_file_button = browser.find_element_by_css_selector('#file')
    select_file_button.send_keys(file_path)

    #Отправляем форму
    submit_button = browser.find_element_by_css_selector('button.btn-primary')
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