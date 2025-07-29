from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from math import log, sin
browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    browser.switch_to.window(browser.window_handles[1])
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    value = str(log(abs(12 * sin(int(x)))))
    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(value)
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
    exit()