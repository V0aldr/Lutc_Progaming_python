from make_db_file import load_Dbase, store_Dbase

db = load_Dbase()
db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'
store_Dbase(db)
