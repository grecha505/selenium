from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element_by_id("input_value")
answer = browser.find_element_by_id("answer")
answer.send_keys(calc(int(x.text)))

browser.execute_script("window.scrollBy(0, 120);")

browser.find_element_by_id("robotCheckbox").click()
browser.find_element_by_id("robotsRule").click()
browser.find_element_by_tag_name("button").click()

time.sleep(7)
browser.quit()
