# вход по кнопке «Войти в аккаунт» на главной
# вход через кнопку «Личный кабинет»
# вход через кнопку в форме регистрации
# вход через кнопку в форме восстановления пароля

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

email = "test23@test.ru"
password = "1Q73H-lDKB"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site")

element = driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button")
element.click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > h2")))

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(email)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)

element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button")
element.click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[2]")))

assert driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").text == 'Оформить заказ'

driver.quit()

# вход через кнопку «Личный кабинет»

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site")

element = driver.find_element(By.XPATH, "/html/body/div/div/header/nav/a/p")
element.click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > h2")))

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(email)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)

element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button")
element.click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[2]")))

assert driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").text == 'Оформить заказ'

driver.quit()

# вход через кнопку в форме регистрации

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/register")

element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/p/a")
element.click()
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > h2")))

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(email)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)

element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button")
element.click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[2]")))

assert driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").text == 'Оформить заказ'

driver.quit()

# вход через кнопку в форме восстановления пароля

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://stellarburgers.nomoreparties.site/forgot-password")

element = driver.find_element(By.XPATH, "/html/body/div[1]/div/main/div/div/p/a")
element.click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#root > div > main > div > h2")))

driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input").send_keys(email)
driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/fieldset[2]/div/div/input").send_keys(password)

element = driver.find_element(By.XPATH, "/html/body/div/div/main/div/form/button")
element.click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div/main/section[1]/div[2]")))

assert driver.find_element(By.XPATH, "/html/body/div/div/main/section[2]/div/button").text == 'Оформить заказ'

driver.quit()
