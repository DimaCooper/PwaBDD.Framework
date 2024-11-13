from utils.logger import TestLogger

def before_all(context):
    # Logger initialization
    context.logger = TestLogger().logger
    context.logger.info("Starting test execution")

def before_feature(context, feature):
    context.logger.info(f"\nStarting feature execution: {feature.name}")

def before_scenario(context, scenario):
    if "skip" in scenario.tags:
        scenario.skip("Marked with @skip")
    if "wip" in scenario.tags:
        scenario.skip("Test is Work in Progress")
    if "manual" in scenario.tags:
        scenario.skip("This is a manual test")
    # Don't skip automated tests, they should be executed
    context.logger.info(f"\nStarting scenario execution: {scenario.name}")

def after_scenario(context, scenario):
    # Log scenario execution result
    if scenario.status == "passed":
        context.logger.success(f"Scenario '{scenario.name}' successfully completed")
    elif scenario.status == "skipped":
        if "skip" in scenario.tags:
            context.logger.warning(f"Scenario '{scenario.name}' skipped: marked with @skip tag")
        elif "wip" in scenario.tags:
            context.logger.warning(f"Scenario '{scenario.name}' skipped: test in development (WIP)")
        elif "manual" in scenario.tags:
            context.logger.warning(f"Scenario '{scenario.name}' skipped: manual test")
    else:
        context.logger.error(f"Scenario '{scenario.name}' failed")
    
    # Application closure
    if hasattr(context, 'app_bindings'):
        if hasattr(context.app_bindings.calculator, 'app'):
            context.app_bindings.calculator.app.kill() # Can add "soft" attribute for safe application termination

def after_feature(context, feature):
    context.logger.info(f"Finishing feature execution: {feature.name}")

def after_all(context):
    context.logger.info("Finishing all tests execution")