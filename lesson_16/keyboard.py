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

keyboard_locator = ("xpath", "//input[@id='target']")

driver.find_element(*keyboard_locator).send_keys("azaaa")

driver.get("https://the-internet.herokuapp.com/key_presses")

driver.find_element(*keyboard_locator).send_keys(Keys.ENTER)

time.sleep(2)
