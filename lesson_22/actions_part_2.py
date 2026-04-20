import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("https://the-internet.herokuapp.com/drag_and_drop")

# COLUMN_A = ("xpath", "//div[@id='column-a']")
# COLUMN_B = ("xpath", "//div[@id='column-b']")

# A = driver.find_element(*COLUMN_A)
# B = driver.find_element(*COLUMN_B)

# time.sleep(3)
# action.drag_and_drop(A, B).perform()

ITEM = ("xpath", "(//div[@class='grid__item'])[3]")
SIDEBAR = ("xpath", "(//div[@class='drop-area__item'])[3]")

action.click_and_hold(driver.find_element(*ITEM)) \
    .pause(1.5) \
    .move_to_element(driver.find_element(*SIDEBAR)) \
    .release() \
    .perform()
    
time.sleep(3)