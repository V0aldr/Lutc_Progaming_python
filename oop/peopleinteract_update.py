import shelve

from person_start import Person

fieldnames = ('name', 'age', 'pay', 'job')

with shelve.open('class_shelve') as db:
    while True:

        print(f"\n{'|INPUT NAME|':-^41}\n")
        key = input("\nkey? => ")
        if not key:
            print(f"{'--|NO DATA|--': ^41}")
            break
        if key == 'q':
            print(f"\n{'|QUIT|':!^41}\n")
            quit()

        if key in db:
            record = db[key]  # извлечь запись по ключу и вывести
            print(f"\n{'|DATA|':-^41}\n")
            for field in fieldnames: print(f"{field} => {getattr(record, field)}")
        else:
            record = Person()

        for field in fieldnames:
            currval = getattr(record, field)
            print(f"\n{'--|CHANGE DATA?|--':-^41}\n")
            newtext = input(f'\t[{field}]= {currval}\n\t\tnew?= > ')
            if not newtext: break
            if newtext.isspace(): continue
            if newtext == 'q':  quit()

            setattr(record, field, eval(newtext))

    db[key] = record


print(f"\n{'|EXIT|':-^41}\n")
