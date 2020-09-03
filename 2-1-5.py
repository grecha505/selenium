from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()
browser.get(link)

people_radio = browser.find_element_by_id("peopleRule")

# Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:

people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

value = browser.find_element_by_css_selector("#input_value.nowrap")
input1 = browser.find_element_by_css_selector("#answer.form-control")
input1.send_keys(calc(value.text))

checkbox = browser.find_element_by_css_selector(".form-check-input")
checkbox.click()

radiob = browser.find_element_by_css_selector("#robotsRule")
radiob.click()

submitb = browser.find_element_by_css_selector("button")
submitb.click()

# ожидание чтобы визуально оценить результаты прохождения скрипта
time.sleep(10)
# закрываем браузер после всех манипуляций
browser.quit()