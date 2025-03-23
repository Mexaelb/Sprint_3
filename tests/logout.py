# Выход из аккаунта
# Проверь выход по кнопке «Выйти» в личном кабинете.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site")

email = "test23@test.ru"
password = "1Q73H-lDKB"

element = driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button")
element.click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > h2")))

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(email)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)

element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button")
element.click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[2]")))

element = driver.find_element(By.XPATH, "/html/body/div[1]/div/header/nav/a/p")
element.click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > nav > ul > li:nth-child(1) > a")))

element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/nav/ul/li[3]/button")
element.click()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/main/div/h2")))

url = driver.current_url
assert url == 'https://stellarburgers.nomoreparties.site/login'

driver.quit()
