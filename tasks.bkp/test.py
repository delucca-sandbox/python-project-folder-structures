from invoke import Collection, Context, task

from . import helpers


@task
def unit(ctx):
    handle_unit_test(ctx)


@task
def integration(ctx):
    handle_integration_test(ctx)


@task
def contract(ctx):
    handle_contract_test(ctx)


@task
def acceptance(ctx):
    handle_acceptance_test(ctx)


def handle_unit_test(ctx: Context) -> None:
    helpers.print_header("UNIT TESTS")

    ctx.run("pytest -m unit --cov", pty=True)


def handle_integration_test(ctx: Context) -> None:
    helpers.print_header("INTEGRATION TESTS")

    ctx.run("pytest -m integration", pty=True)


def handle_contract_test(ctx: Context) -> None:
    helpers.print_header("CONTRACT TESTS")

    ctx.run("pytest -m contract", pty=True)


def handle_acceptance_test(ctx: Context) -> None:
    helpers.print_header("ACCEPTANCE TESTS")

    ctx.run("behave", pty=True)


def build_tasks(collection: Collection) -> None:
    tasks = [unit, integration, contract, acceptance]

    for new_task in tasks:
        ns.add_task(new_task)


ns = Collection()
build_tasks(ns)
