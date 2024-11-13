class CalculatorLocators:
    # Calculator button locators
    BUTTON_PATTERN = "Button{}"  # Pattern allows forming a complete locator for each button (BUTTON_PATTERN.format("135") -> "Button135")
    RESULT_FIELD = "158"
    
    # Dictionary mapping text values to button identifiers
    BUTTON_MAP = {
        "5": "135",
        "plus": "93",
        "equals": "121"
    } 