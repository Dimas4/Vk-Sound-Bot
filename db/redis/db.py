from redis import StrictRedis

db = StrictRedis(host='localhost', port=6379, db=0)
