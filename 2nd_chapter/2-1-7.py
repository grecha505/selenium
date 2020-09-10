from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)


valuex = browser.find_element_by_tag_name("img")
valuex = valuex.get_attribute("valuex")

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(calc(valuex))

checkbox = browser.find_element_by_css_selector("#robotCheckbox")
checkbox.click()

radiob = browser.find_element_by_css_selector("#robotsRule")
radiob.click()

submitb = browser.find_element_by_css_selector("button")
submitb.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()