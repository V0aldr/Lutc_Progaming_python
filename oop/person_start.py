class Person:
    """Класс 'Личность' - упражнение"""
    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay *= (1.0 + percent)
        return round(self.pay, 2)

if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    print(bob.name, sue.pay)
    print(bob.name.split()[-1])
    print(sue.pay)
    sue.pay *= 1.10
    print(sue.pay)
    print(sue.last_name())
    print(bob.give_raise(50))