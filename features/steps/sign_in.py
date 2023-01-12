from selenium.webdriver.common.by import By
from behave import given, when, then

ORDERS = (By.ID, 'nav-orders')
EMAIL_FILD = (By.ID, 'ap_email')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Orders')
def click_order(context):
    context.driver.find_element(*ORDERS).click()


@then('Verify Sign in page opened')
def verify_signin_opened(context):
    context.driver.find_element(*EMAIL_FILD)
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url, \
        f'Url is incorrect, got {context.driver.current_url}'
    print(context.driver.current_url)
