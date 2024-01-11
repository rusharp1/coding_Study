# 1. https://www.w3schools.com  접근
# 2. 화면 중간 LERN HTML 클릭
# 3. 상단 메뉴 중 HOW TO 클릭
# 4. 좌측 메뉴 중 Contact Form 메뉴 클릭
# 5. 입력란에 아래 값 입력.
#     First Name : 나도
#     Last Name : 코딩
#     Country : Canada
#     Subject : 퀴즈 완료하였습니다.
# 6. 5초 대기 후 Submit 버튼 클릭.
# 7. 5초 대기 후 브라우저 종료

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_until(path):
    try:
        elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located
                                            ((By.XPATH, path)))
        return elem
    except:
        print("실패")


browser = webdriver.Chrome()
browser.get("https://www.w3schools.com")

# Lern HTML 버튼 클릭
wait_until('//a[text()="Learn HTML"]')[0].click()
# How To 버튼 클릭
wait_until('//a[text()="HOW TO"]')[0].click()
# Contact Form 버튼 클릭
wait_until('//a[text()="Contact Form"]')[0].click()

# 텍스트 입력.
wait_until('//*[@id="fname"]')[0].send_keys("나도")
wait_until('//*[@id="lname"]')[0].send_keys("코딩")
wait_until('//option[text()="Canada"]')[0].click()
wait_until('//textarea[@class="test"]')[0].send_keys("퀴즈 완료하였습니다.")

time.sleep(5)

browser.find_element(By.XPATH, '//*[@id="main"]/div[3]/a').click()
time.sleep(5)
browser.quit

