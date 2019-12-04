from invoke import Collection

from . import autoformat, lint, test


def build_subcollections(collection: Collection) -> None:
    subcollections = [autoformat, lint, test]

    for subcollection in subcollections:
        collection.add_collection(subcollection)


ns = Collection()
build_subcollections(ns)
