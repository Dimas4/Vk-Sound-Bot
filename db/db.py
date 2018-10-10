class Db:
    def __init__(self, db):
        self.db = db

    def get(self, value):
        return self.db.get(value)

    def set(self, key, value):
        return self.db.set(key, value)

    def setnx(self, key, value):
        return self.db.setnx(key, value)

    def rpush(self, key, value):
        return self.db.rpush(key, value)
