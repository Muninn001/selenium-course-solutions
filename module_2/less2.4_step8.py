from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from math import log, sin
browser = webdriver.Chrome()


browser.get("http://suninjuly.github.io/explicit_wait2.html")
WebDriverWait(browser, 15).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
button = browser.find_element(By.ID, "book")
button.click()
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
value = str(log(abs(12 * sin(int(x)))))
answer = browser.find_element(By.ID, "answer")
answer.send_keys(value)
submit = browser.find_element(By.ID, "solve")
submit.click()
time.sleep(10)

browser.quit()
exit()