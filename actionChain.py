# import webdriver
from selenium import webdriver

# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.LINK_TEXT, "Machine Learning")
lement = driver.find_element(By.LINK_TEXT, "C++")

# create action chain object
action = ActionChains(driver)

# klik kanan pada elemet dan klik kiri pada lement
action.context_click(on_element=element)
action.click(on_element=lement)

# aksi dijalankan
action.perform()
