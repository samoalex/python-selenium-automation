#noinspection CucumberUndefinedStep
Feature: Empty cart

  Scenario: Check that the cart is empty
    Given Open Amazon page
    When Click on cart icon
    Then Check that the page conains Your Amazon cart is empty text

