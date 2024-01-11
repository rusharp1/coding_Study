from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Chrome()
browser.get("https://flight.naver.com/flights/domestic/GMP-CJU-20240130/CJU-GMP-20240205?adult=1&fareType=YC")
browser.maximize_window()

# 1. 로딩 기다려주는 방법
# time.sleep(10)

# 2. element가 나올때까지 기다리기
# '//span[text() = "항공권 검색"]' 가 나올때까지 최대 10초동안 기다림
try:
    elem = WebDriverWait(browser, 20).until(EC.presence_of_all_elements_located
                                        ((By.XPATH, '//span[text() = "항공권 검색"]')))
    print("성공")
except:
    print("실패")
