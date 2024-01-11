# html body 안쪽에 iframe이 있고,
# 그 안에 html 이 또 있을 수 있음.
# 해당 경우에는 xpath 를 통해 접속할 수 없음.

import time
from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

# 브라우저 내 frame으로 switch
browser.switch_to.frame('iframeResult')
elem = browser.find_element(By.XPATH, '//*[@id="html"]')
elem.click()

# 상위로 다시 빠져나옴
browser.switch_to.default_content()

time.sleep(5)
browser.quit()
