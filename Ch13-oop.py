# Ch13-oop.py
from person_start import Person
bob = Person('Bob Smith', 42)
sue = Person('Sue Jones', 45, 40000)

people = [bob, sue] # a "database" list
for person in people:
    print(person.name, person.pay)

x = [(person.name, person.pay) for person in people]
print( x )

[print( rec.name ) for rec in people if rec.age >= 45]   # SQL-ish query
[( print(rec.age ** 2) if rec.age >= 45 else print(rec.age)) for rec in people]

#--
from person import Person
from manager import Manager

bob = Person(name='Bob Smith', age=42, pay=10000)
sue = Person(name='Sue Jones', age=45, pay=20000)
tom = Manager(name='Tom Doe', age=55, pay=30000)
db = [bob, sue, tom]

for obj in db:
    obj.giveRaise(.10)  # default or custom

for obj in db:
    print(obj.lastName(), '=>', obj.pay)