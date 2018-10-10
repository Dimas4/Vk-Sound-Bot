import importlib


def initialize(db):
    module = importlib.import_module(db, ".")
    return module.db
