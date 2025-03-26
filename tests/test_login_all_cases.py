# вход по кнопке «Войти в аккаунт» на главной
# вход через кнопку «Личный кабинет»
# вход через кнопку в форме регистрации
# вход через кнопку в форме восстановления пароля

from locators.locators import AllLocators
from url_pages import AllPages
from test_data import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# вход по кнопке «Войти в аккаунт» на главной
def test_login_main_page(chrome_browser):

    chrome_browser.get(AllPages.page_main)

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_login).click()
    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.login_page_text)))

    chrome_browser.find_element(By.XPATH, AllLocators.input_email).send_keys(TestData.email)
    chrome_browser.find_element(By.XPATH, AllLocators.input_pass).send_keys(TestData.password)

    chrome_browser.find_element(By.XPATH, AllLocators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.main_page_all_list)))

    assert chrome_browser.find_element(By.XPATH, AllLocators.page_main_button_get_order).text == 'Оформить заказ'

# вход через кнопку «Личный кабинет»
def test_login_button_account(chrome_browser):

    chrome_browser.get(AllPages.page_main)

    chrome_browser.find_element(By.XPATH, AllLocators. main_page_button_acc).click()
    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.login_page_text)))

    chrome_browser.find_element(By.XPATH, AllLocators.input_email).send_keys(TestData.email)
    chrome_browser.find_element(By.XPATH, AllLocators.input_pass).send_keys(TestData.password)

    chrome_browser.find_element(By.XPATH, AllLocators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.main_page_all_list)))

    assert chrome_browser.find_element(By.XPATH, AllLocators.page_main_button_get_order).text == 'Оформить заказ'

# вход через кнопку в форме регистрации
def test_login_button_registration_form(chrome_browser):
    chrome_browser.get(AllPages.page_register)

    chrome_browser.find_element(By.XPATH, AllLocators.page_register_button_login).click()
    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.login_page_text)))

    chrome_browser.find_element(By.XPATH, AllLocators.input_email).send_keys(TestData.email)
    chrome_browser.find_element(By.XPATH, AllLocators.input_pass).send_keys(TestData.password)

    chrome_browser.find_element(By.XPATH, AllLocators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.main_page_all_list)))

    assert chrome_browser.find_element(By.XPATH, AllLocators.page_main_button_get_order).text == 'Оформить заказ'

# вход через кнопку в форме восстановления пароля
def test_login_page_forgot_password(chrome_browser):
    chrome_browser.get(AllPages.page_forgot_password)

    chrome_browser.find_element(By.XPATH, AllLocators.page_register_button_login).click()
    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.login_page_text)))

    chrome_browser.find_element(By.XPATH, AllLocators.input_email).send_keys(TestData.email)
    chrome_browser.find_element(By.XPATH, AllLocators.input_pass).send_keys(TestData.password)

    chrome_browser.find_element(By.XPATH, AllLocators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.main_page_all_list)))

    assert chrome_browser.find_element(By.XPATH, AllLocators.page_main_button_get_order).text == 'Оформить заказ'
