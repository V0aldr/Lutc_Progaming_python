"""
Сохраняет в файл базу данных, находящуюся в оперативной памяти, используя
собственный формат записи; предполагается, что в данных отсутствуют строки
‘endrec.’, ‘enddb.’ и ‘=>’; предполагается, что база данных является словарем
словарей; внимание: применение функции eval может быть опасным – она
выполняет строки как программный код; с помощью функции eval() можно также
реализовать сохранение словарей-записей целиком; кроме того, вместо вызова
print(key,file=dbfile) можно использовать вызов dbfile.write(key + ‘\n’);
"""

dbfilename = 'people_file'
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def store_Dbase(db, dbfilename=dbfilename):
    "сохраняет базу данных в файл"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print(key, file=dbfile)
        for (name, value) in db[key].items():
            print(f"{name}{RECSEP}{repr(value)}", file=dbfile)
        print(ENDREC, file=dbfile)
    print(ENDDB, file=dbfile)
    dbfile.close()

def load_Dbase(dbfilename=dbfilename):
    "восстанавливает данные, реконструируя базу данных"
    dbfile = open(dbfilename)
    import sys
    sys.stdin = dbfile
    db = {}
    key = input()
    while key != ENDDB:
        rec = {}
        field = input()
        while field != ENDREC:
            name, value = field.split(RECSEP)
            rec[name] = eval(value)
            field = input()
        db[key] = rec
        key = input()
    return db


if __name__ == '__main__':
    from initdata import db
    store_Dbase(db)






