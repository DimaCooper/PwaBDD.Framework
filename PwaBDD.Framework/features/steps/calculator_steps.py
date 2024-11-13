from behave import given, when, then
from bindings.win_app_bindings import WindowsApplicationBindings

@given('open Windows calculator')
def step_launch_calculator(context):
    context.logger.info("Launching Windows calculator")
    context.app_bindings = WindowsApplicationBindings()
    context.app_bindings.launch_application("calculator") #calculator

@when('user enters number "{number}"')
def step_input_number(context, number):
    context.logger.info(f"Entering number: {number}")
    context.app_bindings.input_number(number)

@when('user clicks button "{button}"')
def step_click_button(context, button):
    context.logger.info(f"Clicking button: {button}")
    context.app_bindings.click_operation(button)

@then('result should be "{expected_result}"')
def step_verify_result(context, expected_result):
    actual_result = context.app_bindings.get_calculation_result()
    context.logger.info(f"Verifying result. Expected: {expected_result}, Actual: {actual_result}")
    
    try:
        assert actual_result == expected_result
        context.logger.info("Result verification successful")
    except AssertionError:
        context.logger.error(f"Error! Expected result: {expected_result}, Actual result: {actual_result}")
        raise 