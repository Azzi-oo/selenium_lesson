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
from selenium.webdriver.support.select import Select

options = Options()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

for_business_button_locator = ("xpath", "(//a[text()=' For Business '])")
start_free_button = ("xpath", "(//a[text()='Start for Free'])")

driver.get("https://hyperskill.org/courses")

# driver.find_element(*for_business_button_locator).click()

# tabs = driver.window_handles
# driver.switch_to.window(tabs[1])

# driver.find_element(*start_free_button).click()

driver.switch_to.new_window('tab')