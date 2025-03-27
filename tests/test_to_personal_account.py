# Переход в личный кабинет
# Проверь переход по клику на «Личный кабинет».

from locators.locators import AllLocators
from url_pages import AllPages
from test_data import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_go_account(chrome_browser):

    chrome_browser.get(AllPages.page_main)

    chrome_browser.find_element(By.XPATH, AllLocators.login_in_acc_button).click()
    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.login_page_text)))

    chrome_browser.find_element(By.XPATH, AllLocators.input_email).send_keys(TestData.email)
    chrome_browser.find_element(By.XPATH, AllLocators.input_pass).send_keys(TestData.password)

    chrome_browser.find_element(By.XPATH, AllLocators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.main_page_all_list)))

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_acc).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.page_accont_button_save)))

    assert chrome_browser.find_element(By.XPATH, AllLocators.page_accont_button_save).text == 'Сохранить'

