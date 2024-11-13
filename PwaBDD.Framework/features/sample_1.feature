# language: en

Feature: Windows Calculator

  @automated
  Scenario: Adding two numbers
    Given open Windows calculator
    When user enters number "5"
    And user clicks button "plus"
    And user enters number "5"
    And user clicks button "equals"
    Then result should be "10"

  @skip
  Scenario: Adding three positive numbers
    Given open Windows calculator
    When user enters number "5"
    And user clicks button "plus"
    And user enters number "5"
    And user clicks button "plus"
    And user enters number "5"
    And user clicks button "equals"
    Then result should be "15"