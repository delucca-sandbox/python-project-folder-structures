from behave import when
from behave.runner import Context

import foo


@when("call entrypoint")
def call_entrypoint(context: Context) -> None:
    foo.say_hi()
