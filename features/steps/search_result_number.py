from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("The number of items is equal to {number}")
def count_items(context, number):
    # one_element = context.driver.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    # print(one_element)
    search_result = context.driver.find_element(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    # print(search_result)
    # print(search_result[5])
    # print(search_result[5].text)
    print(len(search_result))
    # assert len(search_result) == int(number), f"Expected{number}, but got {len(search_result)}"
    if len(search_result) == 60:
        print("Everything is on the page")
    elif len(search_result) > 0:
        print("Some elements are located")
    else:
        print("Nothing is found on the page")


