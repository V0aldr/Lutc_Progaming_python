import pickle

from initdata import db

with open('people_pickle', 'wb') as dbfile:   # в версии 3.X следует использовать
    pickle.dump(db, dbfile)                     # двоичный режим работы с файлами, так как
                                                # данные имеют тип bytes, а не str


