from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



sign_up_url = "http://secure-retreat-92358.herokuapp.com/"
service = Service(executable_path="C:/Development/chromedriver.exe")
driver = Chrome(service=service)
driver.get(sign_up_url)

def fill_in_sign_up(f_name, l_name, email):
    f_name_input = driver.find_element(By.NAME, "fName")
    l_name_input = driver.find_element(By.NAME, "lName")
    email_input = driver.find_element(By.NAME, "email")

    f_name_input.send_keys(f"{f_name}")
    l_name_input.send_keys(f"{l_name}")
    email_input.send_keys(f"{email}")

    email_input.send_keys(Keys.ENTER)



