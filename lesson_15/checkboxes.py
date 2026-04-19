import os
import time
import pickle
from selenium import webdriver
from selenium.webdriver.ie.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = Options()


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# checkbox1 = ("xpath", "(//input[@type='checkbox'])[1]")
# checkbox_home_status = ("xpath", "//input[@id='tree-node-home']")
# checkbox_home_action = ("xpath", "//span[@class='rct-checkbox']")
element_one = ("//li[text()='Cras juste odio]")

driver.get("https://demoqa.com/selectable")

before = driver.find_element(*element_one).get_attribute("class")

driver.find_element(*element_one).click()
after = driver.find_element(*element_one).get_attribute("class")

assert "active" in after
# print(driver.find_element(*checkbox1).get_attribute("checked"))

# driver.find_element(*checkbox_home_action).click()
# driver.find_element(*checkbox_home_status).is_selected()
time.sleep(3)


