import shelve

from initdata import tom

with shelve.open('people_shelve') as db:
    sue = db['sue']         # извлекает объект sue
    sue['pay'] = round(sue['pay'] * 1.50, 2)
    db['sue'] = sue         # изменяет объект sue
    db['tom'] = tom         # добавляет новую запись

    print(f"{db['sue']['pay'] = }")
    print(f"{db['tom'] = }")
