import shelve

from person_alternative import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Readle', 37, 50000, 'Dart Veider')

with shelve.open('class_shelve') as db:
    db['bob'] = bob
    db['sue'] = sue
    db['tom'] = tom

if __name__ == '__main__':
    print("\n>>>GOOD<<<\n")