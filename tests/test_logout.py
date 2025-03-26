# Выход из аккаунта
# проверить выход по кнопке «Выйти» в личном кабинете

from locators.locators import AllLocators
from url_pages import AllPages
from test_data import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_logout_page_account(chrome_browser):

    chrome_browser.get(AllPages.page_main)

    chrome_browser.find_element(By.XPATH, AllLocators.login_in_acc_button).click()
    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.login_page_text)))

    chrome_browser.find_element(By.XPATH, AllLocators.input_email).send_keys(TestData.email)
    chrome_browser.find_element(By.XPATH, AllLocators.input_pass).send_keys(TestData.password)

    chrome_browser.find_element(By.XPATH, AllLocators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.main_page_all_list)))

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_acc).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, AllLocators.account_page_text_profile)))

    chrome_browser.find_element(By.XPATH, AllLocators.button_logout).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.page_login_text_vhod)))

    url = chrome_browser.current_url
    assert url == AllPages.page_login
