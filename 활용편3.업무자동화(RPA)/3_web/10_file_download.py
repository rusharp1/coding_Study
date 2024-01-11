import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 다운로드 위치를 지정 후 chrome option 에 추가해줌.
chrome_options = Options()
chrome_options.add_experimental_option('prefs',
                            {'download.default_directory' : r'C:\Users\owner\Desktop\coding'})
browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()
browser.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download")

browser.switch_to.frame('iframeResult')
elem = browser.find_element(By.XPATH, '/html/body/p[2]/a')
elem.click()
time.sleep(1)