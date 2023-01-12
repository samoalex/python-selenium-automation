Feature: Test Scenarios for Amazon Search functionality

  Scenario: User can search for a product
    Given Open Amazon page
    When Input Dress into search field
    And Click to search
    Then Product results for Dress are shown
   #  And First result contains Dress
