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

# 開始
# 打來 cookie.json 資料
with open("cookie.json") as f:
    cookies = json.load(f)

# 打開瀏覽器
browser.get(url)

# 遍歷所有 cookie 並帶入到網頁中
for cookie in cookies:
    browser.add_cookie(cookie)
# 重新整理網頁
browser.refresh()

time.sleep(6)
browser.quit()
