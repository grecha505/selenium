from selenium import webdriver
import time
import math
import os

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

browser.find_element_by_css_selector("[name=\"firstname\"]").send_keys("Ivan")
browser.find_element_by_css_selector("[name=\"lastname\"]").send_keys("Ivanov")
browser.find_element_by_css_selector("[name=\"email\"]").send_keys("Ivan.iva@iva.iva")

current_dir = os.path.abspath(os.path.dirname(__file__))

browser.find_element_by_id("file").send_keys(current_dir + "\\test.txt")

browser.find_element_by_tag_name("button").click()


time.sleep(7)
# browser.quit()
