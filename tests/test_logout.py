# Выход из аккаунта
# проверить выход по кнопке «Выйти» в личном кабинете

from locators.locators import all_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_logout_page_account(chrome_browser):

    chrome_browser.get(all_locators.page_main)

    email = "test23@test.ru"
    password = "1Q73H-lDKB"

    chrome_browser.find_element(By.XPATH, all_locators.login_in_acc_button).click()
    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, all_locators.login_page_text)))

    chrome_browser.find_element(By.XPATH, all_locators.input_email).send_keys(email)
    chrome_browser.find_element(By.XPATH, all_locators.input_pass).send_keys(password)

    chrome_browser.find_element(By.XPATH, all_locators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, all_locators.main_page_all_list)))

    chrome_browser.find_element(By.XPATH, all_locators.main_page_button_acc).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, all_locators.account_page_text_profile)))

    chrome_browser.find_element(By.XPATH, all_locators.button_logout).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, all_locators.page_login_text_vhod)))

    url = chrome_browser.current_url
    assert url == all_locators.page_login
