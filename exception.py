from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://geeksforgeeks.org/")

element = driver.find_element(By.LINK_TEXT, 'abrakadabra')

print(element.click())
