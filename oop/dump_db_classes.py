import shelve

with shelve.open('class_shelve') as db:
    for obj in db:
        print(f"{obj} => {db[obj].name}, {db[obj].pay}")

    bob = db['bob']
    print(bob.last_name())
    print(db['tom'].last_name())
