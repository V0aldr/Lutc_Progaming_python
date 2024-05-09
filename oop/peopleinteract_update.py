import shelve

from person_start import Person

fieldnames = ('name', 'age', 'pay', 'job')

with shelve.open('class_shelve') as db:
    while True:
        print(f"\n{'|INPUT NAME|':-^41}\n")
        key = input("\nkey? => ")
        print(f"\n{'|DATA|':-^41}\n")
        if not key:
            print(f"{'--|NO DATA|--': ^41}")
            break

        if key in db:
            record = db[key]  # извлечь запись по ключу и вывести
        else:
            record = Person()
        for field in fieldnames: print(f"{field} => {getattr(record, field)}")
        for field in fieldnames:
            currval = getattr(record, field)
            print(f"\n{'--|CHANGE DATA?|--':-^41}\n")
            newtext = input(f'\t[{field}]= {currval}\n\t\tnew?= > ')
            if not newtext: break
            if newtext.isspace(): continue

            setattr(record, field, newtext)

    db[key] = record

print(f"\n{'|EXIT|':-^41}\n")
