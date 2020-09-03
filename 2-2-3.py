from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)

num1 = browser.find_element_by_id("num1")
num2 = browser.find_element_by_id("num2")
num = int(num1.text) + int(num2.text)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(num))

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(5)
browser.quit()
