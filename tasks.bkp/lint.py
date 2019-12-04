from invoke import Collection, Context, task

from . import helpers


@task
def code(ctx):
    handle_code(ctx)


@task
def types(ctx):
    handle_types(ctx)


def handle_code(ctx: Context) -> None:
    helpers.print_header("LINTING CODE")

    ctx.run("flake8", pty=True)


def handle_types(ctx: Context) -> None:
    helpers.print_header("LINTING TYPES")

    ctx.run("mypy", pty=True)


def build_tasks(collection: Collection) -> None:
    tasks = [code, types]

    for new_task in tasks:
        ns.add_task(new_task)


ns = Collection()
build_tasks(ns)
