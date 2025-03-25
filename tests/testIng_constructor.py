# Раздел «Конструктор»
# Проверь, что работают переходы к разделам:
# «Булки»,
# «Соусы»,
# «Начинки».

from locators.locators import all_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

email = "test23@test.ru"
password = "1Q73H-lDKB"

def test_login_go_account_go_sous(chrome_browser):

    chrome_browser.get(all_locators.page_main)

    chrome_browser.find_element(By.XPATH, all_locators.main_page_button_login).click()
    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, all_locators.login_page_text)))

    chrome_browser.find_element(By.XPATH, all_locators.input_email).send_keys(email)
    chrome_browser.find_element(By.XPATH, all_locators.input_pass).send_keys(password)

    chrome_browser.find_element(By.XPATH, all_locators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, all_locators.main_page_all_list)))

    chrome_browser.find_element(By.XPATH, all_locators.main_page_button_sous).click()
    assert chrome_browser.find_element(By.XPATH, all_locators.main_page_section_sous).text == 'Соусы'

def test_login_go_account_go_nachinka(chrome_browser):
    chrome_browser.get(all_locators.page_main)

    chrome_browser.find_element(By.XPATH, all_locators.main_page_button_login).click()
    WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, all_locators.login_page_text)))

    chrome_browser.find_element(By.XPATH, all_locators.input_email).send_keys(email)
    chrome_browser.find_element(By.XPATH, all_locators.input_pass).send_keys(password)

    chrome_browser.find_element(By.XPATH, all_locators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, all_locators.main_page_all_list)))

    chrome_browser.find_element(By.XPATH, all_locators.main_page_button_nachinka).click()
    assert chrome_browser.find_element(By.XPATH, all_locators.main_page_section_nachinka).text == 'Начинки'

def test_login_go_account_go_bulka(chrome_browser):
    chrome_browser.get(all_locators.page_main)

    chrome_browser.find_element(By.XPATH, all_locators.main_page_button_login).click()
    WebDriverWait(chrome_browser, 3).until(
            expected_conditions.visibility_of_element_located((By.XPATH, all_locators.login_page_text)))

    chrome_browser.find_element(By.XPATH, all_locators.input_email).send_keys(email)
    chrome_browser.find_element(By.XPATH, all_locators.input_pass).send_keys(password)

    chrome_browser.find_element(By.XPATH, all_locators.login_button).click()
    WebDriverWait(chrome_browser, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, all_locators.main_page_all_list)))

    chrome_browser.find_element(By.XPATH, all_locators.main_page_button_sous).click()

    chrome_browser.find_element(By.XPATH, all_locators.main_page_button_bulki).click()
    assert chrome_browser.find_element(By.XPATH, all_locators.main_page_section_bulki).text == 'Булки'
