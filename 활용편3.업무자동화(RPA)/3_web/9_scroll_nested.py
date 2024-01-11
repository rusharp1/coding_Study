import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.w3schools.com/html")

# //*[@id="leftmenuinnerinner"]/a[67]
# 스크롤 하고자 하는 element가
elem = browser.find_element(By.XPATH,'//a[text() = "HTML Tag List"]')

# 1. Action Chain 사용
actions = ActionChains(browser)
actions.move_to_element(elem).perform()

time.sleep(3)

browser.execute_script('window.scrollTo(0, 0)')
time.sleep(1)
# 2. elem.location_once_scrolled_into_view ( element의 좌표 정보 가져옴 )
xy = elem.location_once_scrolled_into_view #변수
print(xy)


input("")