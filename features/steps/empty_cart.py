from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def click_cart(context):
    cart_icon = context.driver.find_element(By.ID, "nav-cart")
    cart_icon.click()

@then("Check that the page conains {key_phrase} text")
def check_text(context, key_phrase):
    cart_header = context.driver.find_element(By.CSS_SELECTOR, "div.a-row.sc-your-amazon-cart-is-empty h2")
    assert "Your Amazon cart is empty" in cart_header.text, f"Expected {key_phrase}, but got {cart_header.text}"


