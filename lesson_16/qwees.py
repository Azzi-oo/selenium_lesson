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
from selenium.webdriver import Keys

options = Options()


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# select_locator = ("xpath", "//select[@id='dropdown']")

select_locator = ("xpath", "//input[@id='react-select-3-input']")

time.sleep(1)

driver.get("https://demoqa.com/select-menu")

driver.find_element(*select_locator).send_keys("Ms.")
driver.find_element(*select_locator).send_keys(Keys.ENTER)