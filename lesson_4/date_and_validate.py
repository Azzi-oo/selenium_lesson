import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.wikimedia.org/")

url = driver.current_url

print(f"url: {url}")

current_title = driver.title
print(current_title)

assert url == "https://www.wikimedia.ru/", "Error in url"

time.sleep(3)