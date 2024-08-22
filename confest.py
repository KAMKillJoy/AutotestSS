import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

options = Options()
#  options.add_experimental_option("detach", True)  # отменяет автоматическое закрытие браузера. Нужно было для дебага.
#  driver.quit() в функции browser тоже надо закомментить, чтобы браузер не закрывался.

@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

    