# Регистрация
# Проверка успешной регистрации

from locators.locators import AllLocators
from url_pages import AllPages
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_register_positive(chrome_browser,random_email,ok_passwd,name_user_for_register):

    chrome_browser.get(AllPages.page_register)

    chrome_browser.find_element(By.CSS_SELECTOR, AllLocators.page_register_input_name).send_keys(name_user_for_register)
    chrome_browser.find_element(By.CSS_SELECTOR, AllLocators.page_register_input_email).send_keys(random_email)
    chrome_browser.find_element(By.XPATH, AllLocators.page_register_input_pass).send_keys(ok_passwd)

    chrome_browser.find_element(By.XPATH, AllLocators.page_register_button_registration).click()

    WebDriverWait(chrome_browser, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, AllLocators.page_login_text_vhod)))
    url = chrome_browser.current_url
    assert url == AllPages.page_login


#Проверка некорректного пароля

def test_register_negative(chrome_browser,random_email,no_passwd,name_user_for_register):

    chrome_browser.get(AllPages.page_register)

    chrome_browser.find_element(By.CSS_SELECTOR, AllLocators.page_register_input_name).send_keys(name_user_for_register)
    chrome_browser.find_element(By.CSS_SELECTOR, AllLocators.page_register_input_email).send_keys(random_email)
    chrome_browser.find_element(By.XPATH, AllLocators.page_register_input_pass).send_keys(no_passwd)

    chrome_browser.find_element(By.XPATH, AllLocators.page_register_button_registration).click()

    assert chrome_browser.find_element(By.XPATH, AllLocators.page_register_error_pass_text).text == 'Некорректный пароль'
