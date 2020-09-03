from selenium import webdriver
import time
import math
import os
import pyperclip

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

browser.find_element_by_tag_name("button").click()
windows = browser.window_handles
print(windows)
browser.switch_to.window(windows[1])

x = browser.find_element_by_id("input_value")
browser.find_element_by_id("answer").send_keys(calc(int(x.text)))
browser.find_element_by_tag_name("button").click()

text = browser.switch_to.alert.text
print(text)
text = text.split(": ")[-1]
print(text)
pyperclip.copy(text)

time.sleep(7)
browser.quit()