import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("okrrr")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("okrrr")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("okrrr")
    filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "file.txt")
    inputFile = browser.find_element(By.ID, "file")
    inputFile.send_keys(filePath)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
