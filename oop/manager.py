from person_start import Person


class Manager(Person):
    def give_raise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


if __name__ == '__main__':
    tom = Manager(name='Tom Doe', age=50, pay=50000)
    print(tom.last_name())
    tom.give_raise(.20)
    print(tom.pay)
    print([attr for attr in dir(tom) if not attr.startswith('__')])
    print(tom.__dict__ )
    tom.job = 'manager'
    print(tom.__dict__)