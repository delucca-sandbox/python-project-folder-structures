from invoke import Collection, Context, task


# Until type hinting is fixed, we need to use this workaround:
# https://github.com/pyinvoke/invoke/issues/357#issuecomment-527818509
@task
def conventions(ctx):
  handle_conventions(ctx)


@task
def static_types(ctx):
  handle_static_types(ctx)


def handle_conventions(ctx: Context) -> None:
  ctx.run("flake8", pty=True)


def handle_static_types(ctx: Context) -> None:
  ctx.run("mypy", pty=True)


def build_tasks(collection: Collection) -> None:
  tasks = [conventions, static_types]

  for new_task in tasks:
    ns.add_task(new_task)


ns = Collection()
build_tasks(ns)
