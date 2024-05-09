import shelve

fieldnames = ('name', 'age', 'pay', 'job')
maxfield = max(len(f) for f in fieldnames)

with shelve.open('class_shelve') as db:
    while True:
        print(f"\n{'|INPUT NAME|':-^41}\n")
        key = input("\nkey? => ")
        print(f"\n{'|DATA|':-^41}\n")
        if not key:
            print(f"{'--|NO DATA|--': ^41}")
            break
        try:
            record = db[key]  # извлечь запись по ключу и вывести
        except:
            print(f"No such {key}")
        else:
            for field in fieldnames:
                print(f"{field.ljust(maxfield)} => {getattr(record, field)}")


print(f"\n{'|EXIT|':-^41}\n")

