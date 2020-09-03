from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/simple_form_find_task.html"
    driver = webdriver.Chrome()  # <- Путь до файла хромдрайвера
    driver.get(link)


except Exception as error:
    print(f'Произошла ошибка, вот её трэйсбэк: {error}')

finally:
    driver.close()
    time.sleep(2)
    driver.quit()