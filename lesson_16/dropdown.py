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

select_locator = ("xpath", "//select[@id='dropdown']")

driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown = Select(driver.find_element(*select_locator))

# dropdown.select_by_visible_text("Option 1")
# dropdown.select_by_value("2")
# dropdown.select_by_index(1)

all_options = dropdown.options
# print(all_options)

# for option in all_options:
#     time.sleep(1)
#     if "Option 1" in option.text:
#         print("Option in")
#     dropdown.select_by_visible_text(option.text)

for option in all_options:
    time.sleep(1)
    dropdown.select_by_value(option.get_attribute("value"))

time.sleep(4)