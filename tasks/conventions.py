from invoke import Collection, Context, task


# Until type hinting is fixed, we need to use this workaround:
# https://github.com/pyinvoke/invoke/issues/357#issuecomment-527818509
@task
def format_code(ctx):
  handle_format(ctx)


@task
def import_order(ctx):
  handle_import_order(ctx)


def handle_format(ctx: Context) -> None:
  ctx.run("black", pty=True)


def handle_import_order(ctx: Context) -> None:
  ctx.run("isort -y", pty=True)


def build_tasks(collection: Collection) -> None:
  tasks = [format_code, import_order]

  for new_task in tasks:
    ns.add_task(new_task)


ns = Collection()
build_tasks(ns)
