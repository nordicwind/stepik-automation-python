from selenium import webdriver
import math
import time

# Функция расчета calc(x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем кнопку
    button = browser.find_element_by_css_selector('button.btn-primary')
    button.click()

    #Работаем с Алертом
    alert = browser.switch_to.alert
    alert.accept()

    time.sleep(1)

    #Заполняем форму и отправляем
    x = browser.find_element_by_css_selector('#input_value').text
    input_field = browser.find_element_by_css_selector('#answer')
    answer = calc(x)
    input_field.send_keys(answer)

    time.sleep(1)
    submit_button = browser.find_element_by_css_selector('.btn-primary')
    submit_button.click()

    #Сохраняем текст из алерта и выводим его в консоль
    alert = browser.switch_to.alert
    alert_text = alert.text
    alert.accept()


finally:
    #Debug
    print(alert_text)
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()