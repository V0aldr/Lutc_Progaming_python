# инициализировать данные для последующего сохранения в файлах
# записи
bob = {'name': 'Bob Smith', 'age': 42, 'pay': round(30000.00, 2), 'job': 'dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': round(40000.00, 2), 'job': 'hdw'}
tom = {'name': 'Tom', 'age': 50, 'pay': round(0.00, 2), 'job': None}

# база данных
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    for key in db:
        print(key, '=>', db[key])



