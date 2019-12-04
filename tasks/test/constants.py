TEST_PHASES_ALLOWED = "unit,integration,contract,acceptance"

MESSAGE_PHASE_RUNNING = "{} tests"

COMMANDS = dict(
    unit="pytest -m unit --cov",
    integration="pytest -m integration",
    contract="pytest -m contract",
    acceptance="behave",
)
