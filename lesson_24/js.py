import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
action = ActionChains(driver)

driver.get("")

EX_2_LOCATOR = ("xpath", "//h3[text()='Example 2: ']")
EX_2 = driver.find_element(*EX_2_LOCATOR)

