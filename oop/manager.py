from person_start import Person


class Manager(Person):

    def __init__(self, name, age, pay, job):
        super().__init__(name, age, pay, 'manager')
        Person.__init__(self, name, age, pay, 'manager')

    def give_raise(self, percent, bonus=0.1):
        # self.pay *= (1.0 + percent + bonus)
        # Person.give_raise(self, percent + bonus)
        super().give_raise(percent + bonus)

if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000, job='manager')
    tom2 = Manager('Tom Joe', 50, 50000, 'manager')
    print(tom.last_name())
    tom.give_raise(.20)
    print(tom.pay)
    print([attr for attr in dir(tom) if not attr.startswith('__')])
    print(tom.__dict__ )
    tom.job = 'manager'
    print(tom.__dict__)
    print(tom2.__dict__)