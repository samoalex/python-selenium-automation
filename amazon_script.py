from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
driver.implicitly_wait(4)

input_field = driver.find_element(By.ID, 'twotabsearchtextbox')
input_field.clear()
input_field.send_keys('Dress')
# or optimazed
# driver.find_element(By.ID, 'twotabsearchtextbox').clear().send_keys('Dress')


search_icon = driver.find_element(By.XPATH, "//input[@value ='Go']")
search_icon.click()

text = driver.find_element(By.XPATH, "//span[@class ='a-color-state a-text-bold']").text
assert text == '"Dress"', f'Incorrect text: {text}'
#важно кавычки в слове Dress

driver.quit()
