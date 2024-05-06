import pickle_db

from initdata import db

with open('../people_pickle', 'wb') as dbfile:   # в версии 3.X следует использовать
    pickle_db.dump(db, dbfile)                     # двоичный режим работы с файлами, так как
                                                # данные имеют тип bytes, а не str


