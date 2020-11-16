# Dictionary - unordered elements
d = {"server": "mpilgrim", "database": "master"}
print(d)

print("server    =", d["server"])
print("database = ", d["database"])

# Modifying dictionary
d["database"] = "pubs"   # assigning new value to existing key
d["uid"] = "sa"          # adding a key-value pair

print(d)

# Note: keys are key-sensitive
d = {}
d["key"] = "value"
d["key"] = "other value"
print(d)

d["Key"] = "third value"
print(d)

# Mixing Datatypes in a Dictionary
d = {"server": "mpilgrim", "database": "master"}
d["retrycount"] = 3
d[42] = "douglas"
print(d)

del d[42]   # delete item by key
print(d)

d.clear()   # detele all items by using .clear() method of dictionary object
print(d)
