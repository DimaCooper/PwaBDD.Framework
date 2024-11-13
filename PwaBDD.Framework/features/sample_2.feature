# language: en

Feature: Windows Calculator negative
  
  @automated
  Scenario: Adding two numbers negative test
    Given open Windows calculator
    When user enters number "5"
    And user clicks button "plus"
    And user enters number "5"
    And user clicks button "equals"
    Then result should be "22"