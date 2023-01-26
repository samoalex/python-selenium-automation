Feature: Search results

  #noinspection CucumberUndefinedStep
  Scenario: Check the number of search results
    Given Open Amazon page
    When Input lego into search
    When Click to search
    Then The number of items is equal to 60
