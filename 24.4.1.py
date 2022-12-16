from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestFirstTask:
    def setup(self):
        self.base_url = 'https://google.com'
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        self.driver.get(self.base_url)

    def close(self):
        self.driver.quit()

    def test_search_example(self):
        self.open()
        search_input = self.wait.until(EC.presence_of_element_located((By.XPATH,
                '//input[(@title="Поиск" and @aria-label="Найти") or (@name="q" and @class="glFyf")]')))
        search_input.clear()
        search_input.send_keys('my first selenium test for Web UI')
        search_button = self.wait.until(EC.presence_of_element_located((By.XPATH,
                '//input[(@aria-label="Поиск в Google" and @value="Поиск в Google") or (@name="btnk" and @rolle="button")]')))
        search_button.submit()
        self.driver.save_screenshot('result.png')
        self.close()
        
       
