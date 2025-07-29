from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin

link = "https://suninjuly.github.io/math.html"
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
    radio.click()
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
    exit()
