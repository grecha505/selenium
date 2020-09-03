from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/find_xpath_form"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Sergey")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Grechukha")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Saint Petersburg")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath('//div[6]/button[@type="submit"]')
    button.click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(5)
    browser.close()
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла
