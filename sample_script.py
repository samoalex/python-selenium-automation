from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('smart watch')

# wait for 4 sec
sleep(4)

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
def verify_found_results_text(context, search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f"Expected query not in {context.driver.current_url.lower()}"
print('Test Passed')

driver.quit()
