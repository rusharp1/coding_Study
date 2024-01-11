import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://shopping.naver.com/home")

# 무선마우스 입력
browser.find_element(By.XPATH,'//input[@class="_searchInput_search_text_3CUDs"]').send_keys("무선마우스")
browser.find_element(By.XPATH, '//button[@class="_searchInput_button_search_1n1aw"]').click()
time.sleep(2)

# 1. 지정한 위치로 스크롤 내리기
# 자바 스크립트 기능 사용.
# 모니터 위치인 1080 위치로 스크롤 내리기
browser.execute_script('window.scrollTo(0,1080)')
time.sleep(1)
browser.execute_script('window.scrollTo(0,2080)')
time.sleep(1)

# 2. 화면 가장 아래로 스크롤 내리기
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적 스크롤에 대해 마지막 스크롤 수행
interval = 1
while True:
    # 현재 문서 높이 저장.
    prev_height = browser.execute_script('return document.body.scrollHeight')
    print(prev_height)  
    # 화면 가장 아래로 스크롤 내린 후 대기.
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(interval)
    if prev_height == browser.execute_script('return document.body.scrollHeight'):
        break

# 맨 위로 올리기
browser.execute_script('window.scrollTo(0,0)')

input("")