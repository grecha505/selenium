"""
https://stepik.org/lesson/237240/step/3
"""

import pytest
from selenium import webdriver
import time
import math

# список ссылок из задачи
urls = ["https://stepik.org/lesson/236895/step/1",
        "https://stepik.org/lesson/236896/step/1",
        "https://stepik.org/lesson/236897/step/1",
        "https://stepik.org/lesson/236898/step/1",
        "https://stepik.org/lesson/236899/step/1",
        "https://stepik.org/lesson/236903/step/1",
        "https://stepik.org/lesson/236904/step/1",
        "https://stepik.org/lesson/236905/step/1"
        ]


# фукция подсчета ответа
def answer():
    return str(math.log(int(time.time())))


# фикстура открытия/закрытия
@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    # степик грузится долго
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


class TestCase:
    # задаем параметры для тестов
    @pytest.mark.parametrize("url", urls)
    def test_optional_feedback(self, browser, url):
        # Открываем браузер, находим поле ввода
        browser.get(url)
        input1 = browser.find_element_by_css_selector(".ember-text-area")
        # Передаем в поле ввода результат функции
        input1.send_keys(answer())
        button = browser.find_element_by_css_selector(".submit-submission")
        button.click()
        text = "Correct!"
        text_on_page = browser.find_element_by_css_selector(".smart-hints__hint").text
        assert text == text_on_page, f"Message on the page is not {text}, but {text_on_page}"
