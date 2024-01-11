# html body 안쪽에 iframe이 있고,
# 그 안에 html 이 또 있을 수 있음.
# 해당 경우에는 xpath 를 통해 접속할 수 없음.

import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
# 창 최대화
browser.maximize_window()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

# 브라우저 내 frame으로 switch
browser.switch_to.frame('iframeResult')
elem = browser.find_element(By.XPATH, '//*[@id="vehicle1"]')

# 체크박스 버튼이 선택되어있는지 확인
# False(체크 X ) 선택이 안되어 ~ 로 출력
if elem.is_selected() == False:
    print("선택이 안되어 있으므로 선택하기.")
    elem.click()
else:
    print("선택되어 있으므로 아무것도 안함.")

time.sleep(5)


# 체크박스 버튼이 선택되어있는지 확인
# False(체크 O) 선택되어 있으므로 ~ 로 출력
if elem.is_selected() == False:
    print("선택이 안되어 있으므로 선택하기.")
    elem.click()
else:
    print("선택되어 있으므로 아무것도 안함.")

