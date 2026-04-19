import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(10)

driver.get()

VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']")

driver.find_element(*VISIBLE_AFTER_BUTTON).click()
