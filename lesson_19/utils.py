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
user_1 = webdriver.Chrome(options=options)

LOGIN_FIELD = ("xpath", "//input[@type='email']")
PASSWORD_FIELD = ("xpath", "//input[@type='password']")
SUBMIT_BUTTON  = ("xpath", "//button[@type='submit']")

driver.get("https://hyperskill.org/login")

driver.find_element(*LOGIN_FIELD).send_keys("alekseik@ya.ru")
driver.find_element(*PASSWORD_FIELD).send_keys("Qwerty132!")
driver.find_element(*SUBMIT_BUTTON).click()
time.sleep(3)
user_1.close()

user_2 = webdriver.Chrome(options=options)
user_2.get("https://hyperskill.org/login")