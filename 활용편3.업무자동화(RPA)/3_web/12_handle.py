from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
current_handle = browser.current_window_handle

# current_handle= DC80E3A4BA904E68E39E61C1D87DFF3E 
# 현재 윈도우 핸들 정보
print("current_handle=", current_handle)


browser.find_element(By.XPATH, '//*[@id="main"]/div[2]/a').click()

# 모든 핸들 정보 저장.
handles = browser.window_handles
for handle in handles:
    print(handle)
    # 현재 핸들 위치로 이동됨.
    browser.switch_to.window(handle)
    print(browser.title)
    print()

# 새로 이동된 브라우저에서 자동화 작업 후 브라우저 닫기.
print("현재 핸들 닫기")
browser.close()

print("처음 핸들로 돌아오기")
browser.switch_to.window(current_handle)

print(browser.title)
input("")
browser.quit