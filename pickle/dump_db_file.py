from make_db_file import load_Dbase

db = load_Dbase()
for key in db:
    print(key, '=> ', db[key])

print(db['sue']['name'])
