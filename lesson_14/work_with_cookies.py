import os
import time

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
wait = WebDriverWait(driver, 5, poll_frequency=1)

driver.get("https://www.freeconferencecall.com/en/us/login")

# driver.get_cookie(("country_code"))

# driver.add_cookie({
#     "name": "Example",
#     "value": "kukushka"
# })

# print(driver.get_cookie("Example"))

before = driver.get_cookie("split")
print(before)

driver.delete_cookie("split")

driver.add_cookie({
    "name": "split",
    "value": "QWERTY"
})

after = driver.get_cookie("split")
print(after)