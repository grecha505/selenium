from selenium import webdriver
import time
import unittest

class My_unit_test(unittest.TestCase):

    def test1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # код который заполняет обязательные поля
        input = browser.find_element_by_css_selector(".first_block .form-group .first")
        input.send_keys("Ivan")
        input = browser.find_element_by_css_selector(".first_block .form-group .second")
        input.send_keys("Ivanov")
        input = browser.find_element_by_css_selector(".first_block .form-group .third")
        input.send_keys("ivan.ivanov@ivanovich.org")
        input = browser.find_element_by_css_selector(".second_block .form-group .first")
        input.send_keys("+79211234567")
        input = browser.find_element_by_css_selector(".second_block .form-group .second")
        input.send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_el = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text_from_el = welcome_text_el.text

        welcome_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, welcome_text_from_el)


    def test2(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # код который заполняет обязательные поля
        input = browser.find_element_by_css_selector(".first_block .form-group .first")
        input.send_keys("Ivan")
        input = browser.find_element_by_css_selector(".first_block .form-group .second")
        input.send_keys("Ivanov")
        input = browser.find_element_by_css_selector(".first_block .form-group .third")
        input.send_keys("ivan.ivanov@ivanovich.org")
        input = browser.find_element_by_css_selector(".second_block .form-group .first")
        input.send_keys("+79211234567")
        input = browser.find_element_by_css_selector(".second_block .form-group .second")
        input.send_keys("Russia")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_el = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text_from_el = welcome_text_el.text

        welcome_text = "Congratulations! You have successfully registered!"

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, welcome_text_from_el)


if __name__ == "__main__":
    unittest.main()
