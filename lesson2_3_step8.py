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
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #Нажимаем кнопку
    wait1 = WebDriverWait(browser, 12)
    price = wait1.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
    book_button = browser.find_element(By.ID, 'book')
    book_button.click()

    #Заполняем форму и отправляем
    x = browser.find_element(By.ID, 'input_value').text
    input_field = browser.find_element(By.CSS_SELECTOR, '#answer')
    answer = calc(x)
    input_field.send_keys(answer)

    submit_button = browser.find_element(By.ID, 'solve')
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    browser.quit()