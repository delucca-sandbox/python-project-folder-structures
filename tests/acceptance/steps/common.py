from behave import given, then
from behave.runner import Context


@given("a placeholder")
def placeholder(context: Context) -> None:
    context.placeholder = "This is a placeholder"


@then("assert true")
def assertion(context: Context) -> None:
    assert True
