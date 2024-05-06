import shelve

print(f"{'----|SHELVE|':-<82}\n")
with shelve.open('people_shelve') as db:
    for key in db:
        print(f"{key} => {db[key]}")
    print(f"\n{'----|SUE|':-<82}\n")
    print(f"{db['sue']['name'] = }")
print(f"\n{'----|END|':-<82}")