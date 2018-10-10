from redis import StrictRedis


class Db:
    def __init__(self, host='localhost', port=6379, db_c=0):
        self.host = host
        self.port = port
        self.db_c = db_c
        self.db = StrictRedis(host='localhost', port=6379, db=0)

    def get(self, value):
        return self.db.get(value)

    def set(self, key, value):
        return self.db.set(key, value)

    def setnx(self, key, value):
        return self.db.setnx(key, value)

    def rpush(self, key, value):
        return self.db.rpush(key, value)
