Feature: Test Scenarios for Amazon Sign in functionality

  Scenario: Logged out user Sign in page when clicking Orders
    Given Open 'Amazon' page
    When Click "Orders"
    Then Verify Sign in page opened