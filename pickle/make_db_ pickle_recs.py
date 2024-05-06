import pickle

from initdata import bob, sue, tom

for (key, record) in (('bob', bob), ('tom', tom), ('sue', sue)):
    with open(f"{key}.pkl", 'wb') as recfile:
        pickle.dump(record, recfile)
