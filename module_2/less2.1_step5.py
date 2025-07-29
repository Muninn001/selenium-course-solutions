from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
try:
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    value = log(abs(12*sin(int(x))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(str(value))
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()
    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
    exit()
