#Ch1-1-fieldlabels.py
NAME, AGE, PAY = range(3)   # 0..2
print(NAME, AGE, PAY)

bob = ['Bob Smith', 42, 10000]
print(bob[NAME])
print(PAY, bob[PAY])

bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

# and then ..
for person in people:
    print(person[0][1], person[2][1])

# and then ..
def field(record, label):
    for (fname, fvalue) in record:
        if fname == label: # find any field by name
            return fvalue

print( field(bob,'name') )
print( field(sue, 'pay') )

for rec in people:
    print( field(rec, 'age') )

# Use Dictionaries instead ..
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}

print( bob['name'].split()[-1])
sue['pay'] *= 1.10
print(sue['pay'])

sue = dict(name='Sue Jones', age=45, pay=40000, job='hdw')
# -or-
sue = {}
sue['name'] = 'Sue Jones'
sue['age'] = 45
sue['pay'] = 40000
sue['job'] = 'hdw'
sue
print( sue )

# -or-
names = [ 'name','age', 'pay', 'job']
values = [ 'Sue Jones', 45, 40000, 'hdw']

list(zip(names, values)) 
sue = dict(zip(names, values))

# -or-
fields = ( 'name', 'age', 'job', 'pay')
record = dict.fromkeys( fields, 'placeholder')
print(record)

# list of dictionaties
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
people = [bob, sue]
print( people)

for person in people:
    print( person['name'], person['pay'], sep= ', ' )

for person in people:
    if person['name'] == 'Sue Jones':
        print(person['pay'])


print( list(map(lambda x: x['name'], people))  )   # ['Bob Smith', 'Sue Jones']

sum( person['pay'] for person in people)

# (!) interesting 
[ rec['name'] for rec in people if rec['age'] >=45 ]

[ print(rec['age'] **2) if rec['age'] >= 45 else print(rec['age']) for rec in people ]

G = ( rec['name'] for rec in people if rec['age'] >= 45)  # G - generator object
print( next( G ) )  # Sue Jones

G = ( (rec['age'] ** 2 if rec['age'] >= 45 else rec['age']) for rec in people )
print( G.__next__() )  #42

for person in people:
    print( person['name'].split()[-1])
    person['pay'] *= 1.10
    print( person['pay'], '\n' )

for person in people: print( person['pay'])
