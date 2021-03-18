import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


def calculate_answer():
    answer = math.log(int(time.time()))
    return answer


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestUFOAnswer:

    @pytest.mark.parametrize('link', links)
    def test_feedback(self, browser, link):
        valid_feedback_text = "Correct!"
        browser.get(f"{link}")
        wait = WebDriverWait(browser, 10)

        input_field = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "string-quiz__textarea"))
        )
        answer = str(calculate_answer())
        input_field.send_keys(answer)

        submit_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
        )
        submit_button.click()

        feedback_box = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
        )
        feedback_message = feedback_box.text

        assert feedback_message == valid_feedback_text, "Текст в опциональном фидбеке полностью совпадает с 'Correct!'"
