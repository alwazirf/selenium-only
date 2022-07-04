from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

driver.get("https://geeksforgeeks.org/")
element = driver.find_element(By.CLASS_NAME, "cursor-p").send_keys(Keys.RETURN)
