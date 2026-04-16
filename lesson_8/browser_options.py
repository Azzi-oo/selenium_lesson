import re
import time
from unittest import result

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.page_load_strategy = "normal"
# chrome_options.add_argument("--headless")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--window-size=700,700")
chrome_options.add_argument("--dicable-cache")


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.set_window_size(1920, 1080)

start_time = time.time()


driver.get("https://whatismyipaddress.com/")

end_time = time.time()

result = end_time - start_time
print(result)

time.sleep(1)