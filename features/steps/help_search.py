from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.common.keys import Keys

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_SUBMIT = (By.XPATH, "//input[@value ='Go']")
RESLTS_INFO_TEXT = (By.XPATH, "//span[@class ='a-color-state a-text-bold']")



@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)



@when('Click to search')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()



@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    search_result_header = context.driver.find_element(*RESLTS_INFO_TEXT).text
    assert 'Dress' in search_result_header, f"Incorrect header: {search_result_header}"
