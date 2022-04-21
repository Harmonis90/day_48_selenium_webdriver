from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



def init_driver():
    driver_path = "C:/Development/chromedriver.exe"
    service = Service(driver_path)
    driver = Chrome(service=service)
    return driver

def check_amazon():
    amazon_path = "https://www.amazon.com/Apple-MacBook-14-inch-8%E2%80%91core-" \
                  "14%E2%80%91core/dp/B09JQSLL92/ref=sr_1_1_sspa?keywords=macbook%2Bpro%2B14&qid" \
                  "=1650335896&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFYQzU0TUNKUDJFQUEmZW5jcn" \
                  "lwdGVkSWQ9QTAyMjU4MTUxT1ZHREJQNE1TTkEmZW5jcnlwdGVkQWRJZD1BMDI5MjMzNjMwVVgxT05EN0ZBOTImd" \
                  "2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1"
    driver.get(amazon_path)
    price = driver.find_element(By.CSS_SELECTOR, "#corePrice_feature_div")
    print(price.text.strip("$"))

# check_amazon()
python_path = "https://www.python.org/"
driver = init_driver()
driver.get(python_path)
# search_bar = driver.find_element(By.NAME, "q")
# docs_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(docs_link.text)

# XPATH
# submit_xpath = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(submit_xpath.text)
# MY WAY!
# event_dict = {}
# event_text = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
# event_list = event_text.text.split("\n")
# for event_index in range(len(event_list))
# print(event_list)

# CORRECT WAY

event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu time")
event_data = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul a")
events = {}
for event in range(len(event_time)):
    events[event] = {
        "date": event_time[event].text,
        "title": event_data[event].text
    }
print(events)




driver.quit()