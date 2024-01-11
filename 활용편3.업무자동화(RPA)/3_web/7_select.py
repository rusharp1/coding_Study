# html body 안쪽에 iframe이 있고,
# 그 안에 html 이 또 있을 수 있음.
# 해당 경우에는 xpath 를 통해 접속할 수 없음.

import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
# 창 최대화
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

# 브라우저 내 frame으로 switch
browser.switch_to.frame('iframeResult')

# option[1] : 첫번째 항목
# option[2] : 두번째 항목 ...
# 드롭박스에서 n번째 항목을 클릭.
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[4]')
elem.click()
time. sleep(1)

# 텍스트 값을 통해 선택
# 옵션 중 텍스트가 Saab 인 값을 선택.
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[text()="Saab"]')
elem.click()
time. sleep(1)

# 텍스트 값이 일부 일치하는 항목을 선택
# 옵션 중 텍스트에 "vol" 이 포함된 값을 선택.
elem = browser.find_element(By.XPATH, '//*[@id="cars"]/option[contains(text(),"Vol")]')
elem.click()


time.sleep(5)
