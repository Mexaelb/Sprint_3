# Регистрация
# Проверка успешной регистрации

import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def random_email():
    var_number = random.randint(100, 999)
    email = f'georgios_vervelakis_19_{var_number}@yandex.ru'
    return email

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/register")

name = f'georgios_vervelakis_19'
passwd = random.randint(100000,999999)

driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input").send_keys(random_email())
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(passwd)

element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button")
element.click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/div/h2[text() = 'Вход']")))
url = driver.current_url
assert url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()

#Проверка некорректного пароля

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/register")

name = f'georgios_vervelakis_19'
passwd = random.randint(10,99)

driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(1) > div > div > input").send_keys(name)
driver.find_element(By.CSS_SELECTOR, "#root > div > main > div > form > fieldset:nth-child(2) > div > div > input").send_keys(random_email())
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[3]/div/div/input").send_keys(passwd)

element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button")
element.click()

assert driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/form/fieldset[3]/div/p").text == 'Некорректный пароль'

driver.quit()
