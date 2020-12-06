# manager.py
from person import Person

class Manager( Person ):

    def __init__(self, name, age, pay):
        Person.__init__(self, name, age, pay, 'manager')
    def giveRaise(self, percent, bonus=0.1):
    #    self.pay *= (1.0 + percent + bonus)
    # -or-
        Person.giveRaise(self, percent + bonus)
'''Note -can use either form:
    instance.method(arg1, arg2)
    class.method(instance, arg1, arg2)
'''

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.lastName())
    tom.giveRaise(.20)
    print(tom.pay)
    print(tom)   # prints: <Manager => Tom Jones> because of __str__ method in class Peron

