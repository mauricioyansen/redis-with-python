import redis

r = redis.Redis(host="localhost", port=6379, db=0)

### String
# Add/edit a key
r.set("key_1", "value_1")

# Select
print(r.get("key_1").decode("utf-8"))

# Delete/unlink
r.unlink("key_1")


### Hash
# Add/edit a hash
r.hset("my_hash", "name", "Kartana")
r.hset("my_hash", "age", "30")
r.hset("my_hash", "city", "Valinhos")
r.hset("my_hash", "UF", "SP")

# Select
print(r.hget("my_hash", "name").decode("utf-8"))

# Delete/unlink
print(r.hdel("my_hash", "UF"))


### Check if exists
# 1 exists
# 0 not exists
print(r.exists("key_1"))  # String
print(r.hexists("my_hash", "name"))  # Hash


### TTL
r.set("key_TTL", "this value will be deleted after 12 seconds", 12)
r.expire("my_hash", 20)
