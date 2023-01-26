from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@then("Locate hamburger menu")
def locate_item(context):
    context.driver.find_element(By.ID, "nav-hamburger-menu")