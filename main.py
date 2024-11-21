from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
import time
import json

# 轉成 Service 物件
ChromeDriverPath = Service(ChromeDriverManager().install())
# 模擬瀏覽器設定
myOptions = webdriver.ChromeOptions()
# 執行selenium瀏覽器
browser = webdriver.Chrome(service=ChromeDriverPath, options=myOptions)

# 前往目標網址
url = "https://tixcraft.com/"
browser.get(url)

# search = browser.find_element(by="name", value="query")
# search.send_keys("比特幣")
# search.send_keys(Keys.RETURN)

time.sleep(6)

browser.quit()
