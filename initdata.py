<<<<<<< HEAD
# initdata.py

# initialize data to be stored in files, pickles, shelves
# records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom','age': 50, 'pay': 0, 'job': None}
=======
# initialize data to be stored in files, pickles, shelves

# records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': 0, 'job': None}
>>>>>>> 9e6aeeca776026f127297bbe7bf8df7da39131ab

# database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

<<<<<<< HEAD
if __name__ == '__main__':
    # when run as a script
    for key in db:
        print(key, '=>\n ', db[key])
=======
if __name__ == '__main__': # when run as a script
    for key in db:
        print(key, '=>\n ', db[key])

>>>>>>> 9e6aeeca776026f127297bbe7bf8df7da39131ab
