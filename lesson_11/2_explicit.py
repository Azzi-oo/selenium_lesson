import os
from telnetlib import EC
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

wait = WebDriverWait(driver, 15, pull_frequency=1)

driver.get()

REMOVE_BUTTON = ("xpath", "//button[text()='Remove']")

driver.find_element(*REMOVE_BUTTON).click()

wait.until(EC.visibility_of_element_located(REMOVE_BUTTON)).click()