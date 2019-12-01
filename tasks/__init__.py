from invoke import Collection

from . import tests, conventions, validators


def build_subcollections(collection: Collection) -> None:
  subcollections = [tests, conventions, validators]

  for subcollection in subcollections:
    collection.add_collection(subcollection)


ns = Collection()
build_subcollections(ns)
