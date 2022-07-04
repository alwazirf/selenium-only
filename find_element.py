from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://facebook.com/")

byId = driver.find_element(By.ID, 'email').send_keys('Hallo')
byName = driver.find_element(By.NAME, 'email').send_keys('LOLO')
# byXpath = driver.find_element(
#     By.XPATH, '/html/body/form[2]').send_keys('xpath')
# byLink = driver.find_element(
#     By.LINK_TEXT, 'Forgotten password?').send_keys(Keys.RETURN)
# byPartialLink = driver.find_element(
#     By.PARTIAL_LINK_TEXT, 'password').send_keys(Keys.RETURN)
# byTagName = driver.find_element(By.TAG_NAME, 'h2').get_attribute("innerHTML")
# print(byTagName)

byCssSelector = driver.find_element(
    By.CSS_SELECTOR, 'h2._8eso').get_attribute("innerHTML")
print(byCssSelector)


time.sleep(2)
driver.quit()
