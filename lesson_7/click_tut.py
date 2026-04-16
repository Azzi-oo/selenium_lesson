import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.freeconferencecall.com/global/pl/login")

login_button = driver.find_element(By.ID, "login_email")
login_button.click()

email_field = driver.find_element(By.ID, "login_email")
email_field.send_keys("dsfdf@ya.ru")
email_field.clear()
# print(email_field.get_attribute("value"))

email_field.send_keys("aaaaa")

time.sleep(3)