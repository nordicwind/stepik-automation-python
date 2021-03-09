from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import math
import time

# Функция расчета calc(x)
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем кнопку
    button = browser.find_element_by_css_selector('button.trollface.btn-primary')
    button.click()

    #Переходим на другую вкладку
    redirect_window = browser.window_handles[1]
    browser.switch_to.window(redirect_window)

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
    #time.sleep(15)
    # закрываем браузер после всех манипуляций, по Явному ожиданию
    wait = WebDriverWait(browser, 10)
    exit_timer = wait.until(EC.text_to_be_present_in_element((By.ID, "countdown"), 'time is up :('))
    
    
    print(for_print)
    browser.quit()