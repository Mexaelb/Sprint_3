# Раздел «Конструктор»
# Проверь, что работают переходы к разделам:
# «Булки»,
# «Соусы»,
# «Начинки».

from locators.locators import AllLocators
from url_pages import AllPages
from test_data import TestData
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_login_go_account_go_sous(chrome_browser):

    chrome_browser.get(AllPages.page_main)

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_login).click()
    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.login_page_text)))

    chrome_browser.find_element(By.XPATH, AllLocators.input_email).send_keys(TestData.email)
    chrome_browser.find_element(By.XPATH, AllLocators.input_pass).send_keys(TestData.password)

    chrome_browser.find_element(By.XPATH, AllLocators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.main_page_all_list)))

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_sous).click()
    assert chrome_browser.find_element(By.XPATH, AllLocators.main_page_section_sous).text == 'Соусы'

def test_login_go_account_go_nachinka(chrome_browser):
    chrome_browser.get(AllPages.page_main)

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_login).click()
    WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.login_page_text)))

    chrome_browser.find_element(By.XPATH, AllLocators.input_email).send_keys(TestData.email)
    chrome_browser.find_element(By.XPATH, AllLocators.input_pass).send_keys(TestData.password)

    chrome_browser.find_element(By.XPATH, AllLocators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.main_page_all_list)))

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_nachinka).click()
    assert chrome_browser.find_element(By.XPATH, AllLocators.main_page_section_nachinka).text == 'Начинки'

def test_login_go_account_go_bulka(chrome_browser):
    chrome_browser.get(AllPages.page_main)

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_login).click()
    WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.login_page_text)))

    chrome_browser.find_element(By.XPATH, AllLocators.input_email).send_keys(TestData.email)
    chrome_browser.find_element(By.XPATH, AllLocators.input_pass).send_keys(TestData.password)

    chrome_browser.find_element(By.XPATH, AllLocators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.main_page_all_list)))

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_sous).click()

    chrome_browser.find_element(By.XPATH, AllLocators.main_page_button_bulki).click()
    assert chrome_browser.find_element(By.XPATH, AllLocators.main_page_section_bulki).text == 'Булки'
