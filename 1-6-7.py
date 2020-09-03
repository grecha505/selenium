import time
from selenium import webdriver

link = "http://suninjuly.github.io/huge_form.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_css_selector('[type="text"]')
    for element in elements:
        element.send_keys("ZzZz")
    time.sleep(3)
    button = browser.find_element_by_css_selector('[type="submit"]')
    button.click()


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    time.sleep(10)
    browser.close()
    browser.quit()

# не забываем оставить пустую строку в конце файла
