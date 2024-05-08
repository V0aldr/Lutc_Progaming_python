"""
Альтернативные реализации классов Person и Manager с данными, методами
и с перегрузкой операторов (не используется в объектах, предусматривающих
возможность сохранения)
"""


class Person:
    """
    универсальное представление человека: данные+логика
    """

    def __init__(self, name: str, age: int, pay: float, job: str) -> None:
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def give_raise(self, percent, bonus=0):
        self.pay *= (1.0 + percent + bonus)
    def last_name(self):
        return self.name.split()[-1]

    def __str__(self):
        return f"<{self.__class__.__name__} => {self.name}: {self.job}, {self.pay:.2f}>"


class Manager(Person):
    """
    класс со специализированным методом giveRaise,
    наследующий обобщенные методы lastName и __str__
    """
    # Нафиг не  нужон, т.к. фсё решает наследование


if __name__ == '__main__':
    bob = Person('Bob Smith', 42, 30000, 'software')
    sue = Person('Sue Jones', 45, 40000, 'hardware')
    tom = Person('Tom Readle', 37, 50000, 'Dart Veider')
    print(f"\n__str__: {sue}, \n{sue.pay = }, \n{sue.last_name() = }\n\n{'----FOR OBJ':-<82}\n")
    for obj in bob, sue, tom:
        obj.give_raise(0.1)
        print(obj)

    print(f"\n{'----CHECKING':-<82}\n")
    tom.give_raise(0.1, 0.5)
    print(tom)
    print(f"{tom.pay} && round pay: {tom.pay:.2f}\n")



print(f"\n{'----END':-<82}\n")