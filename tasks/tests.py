from invoke import Collection, Context, task


# Until type hinting is fixed, we need to use this workaround:
# https://github.com/pyinvoke/invoke/issues/357#issuecomment-527818509
@task
def unit(ctx):
  handle_unit_test(ctx)


@task
def integration(ctx):
  handle_integration_test(ctx)


@task
def acceptance(ctx):
  handle_acceptance_test(ctx)


def handle_unit_test(ctx: Context) -> None:
  ctx.run("pytest -k foo", pty=True)


def handle_integration_test(ctx: Context) -> None:
  ctx.run("pytest -k integration", pty=True)


def handle_acceptance_test(ctx: Context) -> None:
  ctx.run("behave", pty=True)


def build_tasks(collection: Collection) -> None:
  tasks = [unit, integration, acceptance]

  for new_task in tasks:
    ns.add_task(new_task)


ns = Collection()
build_tasks(ns)
