from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def init_driver():
    service = Service(executable_path="C:/Development/chromedriver.exe")
    driver = Chrome(service=service)
    return driver


driver = init_driver()
wiki = driver.get("https://en.wikipedia.org/wiki/Main_Page")
wiki_input = driver.find_element(By.NAME, "search")
wiki_input.send_keys("Python")
wiki_input.send_keys(Keys.ENTER)
# wiki_search_button = driver.find_element(By.NAME, "go")
# wiki_search_button.click()


def emotional_damage():
    # Any and all references are attributed to Steven He. I claim no ownership of the video linked below.
    youtube = "https://www.youtube.com/watch?v=PWZnenTQDB4&ab_channel=StevenHe"
    driver.get(youtube)
    play = driver.find_element(By.CSS_SELECTOR,
                               "#movie_player > "
                               "div.ytp-chrome-bottom > "
                               "div.ytp-chrome-controls > "
                               "div.ytp-left-controls > "
                               "button")
    play.click()





def open_link(link_text):
    link = driver.find_element(By.LINK_TEXT, f"{link_text}")
    link.click()

# driver.quit()
