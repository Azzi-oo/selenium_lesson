import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
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
action = ActionChains(driver)

# FROM_NAME_LOCATOR = ("xpath", "//input[@id='RESULT_TextField-0']")
# COPE_TEXT_LOCATOR = ("xpath", "//button[text()='Copy Text']")
# IFRAME_LOCATOR = ("xpath", "//iframe")
# HOVER_BUTTON_LOCATOR = ("xpath", "//button[@id='']")

driver.get("https://demoqa.com/menu")

MENU_ITEM_2_LOCATOR = ("xpath", "//a[text()='Main Item 2']")
SUB_LIST_LOCATOR = ("xpath", "//a[text()='SUB SUB LIST >']")

menu_item_2 = driver.find_element(*MENU_ITEM_2_LOCATOR)
sub_list_menu = driver.find_element(*SUB_LIST_LOCATOR)

action.move_to_element(menu_item_2) \
    .pause(2) \
    .move_to_element(sub_list_menu) \
    .perform()

time.sleep(3)

# driver.switch_to.frame("frame1")
# driver.find_element("xpath", "//body").text

# driver.switch_to.frame(0)
# driver.find_element("xpath", "//body").text

# iframe = driver.find_element(*IFRAME_LOCATOR)

# driver.switch_to.frame("frame-one796546169")

# driver.find_element(*FROM_NAME_LOCATOR).send_keys("Aleksei")

# driver.switch_to.default_content()

# driver.find_element(*COPE_TEXT_LOCATOR).click()

