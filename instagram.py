import time
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(4)  # so you let the webpage load
browser.find_element(By.NAME, "username").send_keys("blablabla")
