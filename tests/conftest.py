import pytest
import random
from selenium import webdriver

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def random_email():
    var_number = random.randint(100, 999)
    email = f'georgios_vervelakis_19_{var_number}@yandex.ru'
    return email

@pytest.fixture()
def ok_passwd():
    passwd = random.randint(100000,999999)
    return passwd

@pytest.fixture()
def no_passwd():
    passwd = random.randint(10,99)
    return passwd

@pytest.fixture()
def name_user_for_register():
    name_user_for_register = f'georgios_vervelakis_19'
    return name_user_for_register