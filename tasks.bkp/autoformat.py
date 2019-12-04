from invoke import Collection, Context, task

from . import helpers


@task
def code(ctx):
    handle_code(ctx)


@task
def imports(ctx):
    handle_imports(ctx)


def handle_code(ctx: Context) -> None:
    helpers.print_header("FORMATING CODE")

    ctx.run("black .", pty=True)


def handle_imports(ctx: Context) -> None:
    helpers.print_header("FORMATING IMPORTS")

    ctx.run("isort -y", pty=True)


def build_tasks(collection: Collection) -> None:
    tasks = [code, imports]

    for new_task in tasks:
        ns.add_task(new_task)


ns = Collection()
build_tasks(ns)
