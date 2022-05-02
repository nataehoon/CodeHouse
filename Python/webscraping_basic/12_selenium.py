from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe") # 경로 정보
browser.get("http://naver.com")