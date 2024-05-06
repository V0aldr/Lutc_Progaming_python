import shelve

from initdata import bob, sue


with shelve.open('people_shelve') as db:
    db['sue'] = sue
    db['bob'] = bob
