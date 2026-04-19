import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


login_field = driver.find_element("xpath", "//input[@id='lofin_email]")
login_field.send_keys("selenium@ya.ru")

password_field = driver.find_element("xpath", "//input[@type='password']")
password_field.send_keys("123")

agree_checkbox = driver.find_element("xpath", "//input[@id='gdpr_checkbox']")
agree_checkbox.click()

submit_button = driver.find_element("xpath", "//button[@id='loginformsubmit']")
submit_button.click()


driver.get()
upload_field = driver.find_element("xpath", "//input[@type='file']")
upload_field.send_keys(f"{os.getcwd()}/downloads/2.jpg")


driver.find_element("xpath", "//input[@type='file']").send_keys(f"{os.getcwd()}/downloads/")

time.sleep(3)