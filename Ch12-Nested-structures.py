#Ch12-Nested-structures.py

bob2 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'age': 42,
        'job': ['software', 'writing'],
        'pay': (40000, 50000)}

print( bob2['name'])
print( bob2['name']['last'] )

for job in bob2['job']: print(job)
print( bob2['job'][-1] )  # last job

bob2['job'].append('janitor')
print( 'Bob2 jobs: ', bob2['job'])

# Dictionaries of dictionaries
bob = dict(name='Bob Smith', age=42, pay=30000, job='dev')
sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')

db = {}
db['bob'] = bob  # reference in a dict of dicts
db['sue'] = sue
db['bob']['pay'] = 50000

print( db )   #{'bob': {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}}
print('\n')
# using pretty-print module
import pprint
pprint.pprint( db )

print( db.keys() )  # dict_keys(['bob', 'sue'])
for key in db: 
    print( key, '=>', db[key]['name'])

for key in db:
    print(db[key]['name'].split()[-1])

for record in db.values(): print(record['name'])

x = [db[key]['name'] for key in db]
print( x )  # ['Bob Smith', 'Sue Jones']

# -or -
x = [rec['name'] for rec in db.values()]
print( x )

# Add new record
db['tom'] = dict(name='Tom', age=50, job=None, pay=0)

