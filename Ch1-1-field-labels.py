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
sue

# -or-
fields = ( 'name', 'age', 'job', 'pay')
record = dict.fromkeys( fields, '?')
record