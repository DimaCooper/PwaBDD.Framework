from pages.calculator_page import CalculatorPage

class WindowsApplicationBindings:
    def __init__(self):
        self.calculator = CalculatorPage()

    def launch_application(self, app_name):
        if app_name.lower() == "calculator":
            self.calculator.launch_calculator()

    def input_number(self, number):
        for digit in str(number):
            self.calculator.click_button(digit)

    def click_operation(self, operation):
        self.calculator.click_button(operation)

    def get_calculation_result(self):
        return self.calculator.get_result()