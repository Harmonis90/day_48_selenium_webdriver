from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

cookie_clicker_url = "https://orteil.dashnet.org/cookieclicker/"


class CookieClicker:
    def __init__(self):
        self.driver = self.init_game()
        self.cookie_element = self.driver.find_element(By.ID, "bigCookie")
        self.cookie_count = self.get_cookie_count()
        self.unlocked_upgrade_elements = self.get_unlocked_elements()

    def init_game(self):
        service = Service("C:/Development/chromedriver.exe")
        temp_driver = Chrome(service=service)
        temp_driver.get(cookie_clicker_url)
        return temp_driver

    def click_cookie(self):
        self.cookie_element.click()

    def get_cookie_count(self):
        self.cookie_count = self.driver.find_element(By.CSS_SELECTOR, '#cookies')
        return self.cookie_count

    def get_unlocked_elements(self):
        temp_element_list = []
        unlocked_elements = self.driver.find_elements(By.CLASS_NAME, "product.unlocked.enabled")
        for element in unlocked_elements:
            temp_element_list.append(element)
        return temp_element_list







start_time = time.time()
time_delta = 5
counter = 0



clicker = CookieClicker()
is_running = True
while is_running:
    current_time = time.time()
    elapsed_time = current_time - start_time
    clicker.click_cookie()
    if elapsed_time > time_delta:
        start_time = time.time()

        print(clicker.get_cookie_count().text)
        unlocked = clicker.get_unlocked_elements()
        if unlocked:
            unlocked[-1].click()


        # cursor_element = driver.find_element(By.ID, "product0")
        # cursor_element.click()


