from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pyperclip
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

WebDriverWait(browser, 13).until(
    EC.text_to_be_present_in_element(
        (By.ID, "price"), "100"))

browser.find_element_by_id("book").click()

x = browser.find_element_by_id("input_value")
browser.find_element_by_id("answer").send_keys(calc(int(x.text)))
browser.find_element_by_id("solve").click()

text = browser.switch_to.alert.text
print(text)
text = text.split(": ")[-1]
print(text)
pyperclip.copy(text + "     was copied")

time.sleep(7)
browser.quit()
