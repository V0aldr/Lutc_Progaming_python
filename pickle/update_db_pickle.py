import pickle

with open('../people_pickle', 'rb') as dbfile:
    db = pickle.load(dbfile)
    for key in db:
        print(f"{key} => {db[key]}")

db['tom']['name'] = 'Toms Sawyer'
db['sue']['pay'] *= 1.10

with open('../people_pickle', 'wb') as dbfile:
    pickle.dump(db, dbfile)







