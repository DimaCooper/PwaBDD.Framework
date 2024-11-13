from pywinauto.application import Application
from locators.calculator_locators import CalculatorLocators
import logging

class CalculatorPage:
    def __init__(self):
        self.app = None
        self.main_window = None
        self.locators = CalculatorLocators()
        self.logger = logging.getLogger('TestLogger')

    def launch_calculator(self):
        try:
            self.app = Application(backend='uia').start('calc.exe')
            self.main_window = self.app.window(title='Калькулятор') #Calculator
            self.main_window.wait('visible')
            self.logger.info("Calculator launched successfully")
        except Exception as e:
            self.logger.error(f"Error launching calculator: {str(e)}")
            raise

    def click_button(self, button_text):
        try:
            button_id = self.locators.BUTTON_MAP.get(button_text)
            if button_id:
                self.main_window.child_window(auto_id=button_id).click()
                self.logger.debug(f"Button pressed: {button_text}")
            else:
                self.logger.error(f"Button not found: {button_text}")
                raise ValueError(f"Unknown button: {button_text}")
        except Exception as e:
            self.logger.error(f"Error pressing button {button_text}: {str(e)}")
            raise

    def get_result(self):
        try:
            result = self.main_window.child_window(
                auto_id=self.locators.RESULT_FIELD
            ).window_text()
            self.logger.debug(f"Result obtained: {result}")
            return result.strip('Display value is ')
        except Exception as e:
            self.logger.error(f"Error getting result: {str(e)}")
            raise