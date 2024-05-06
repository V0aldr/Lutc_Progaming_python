import pickle

from pprint import pprint

with open('people_pickle', 'rb') as dbfile:
    db = pickle.load(dbfile)
    for key in db:
        pprint(f"{key} => {db[key]}")

print(f"{'----|CHECK PERSON|':-<80}")
pprint(db['sue']['name'])


