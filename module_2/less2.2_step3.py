from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/selects2.html")
    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    summ = str(num1 + num2)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(summ)
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit.click()

finally:
    time.sleep(5)
    browser.quit()
    exit()