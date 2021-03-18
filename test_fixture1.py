from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    @classmethod
    def setup_class(self):
        print("\nstart browser before the test")
        self.browser = webdriver.Chrome()

    @classmethod
    def teardown_class(self):
        print("\nclose browser after test complete")
        self.browser.quit()


    def test_abs(self):
        self.browser.get(link)
        self.browser.find_element_by_css_selector("#id_q")