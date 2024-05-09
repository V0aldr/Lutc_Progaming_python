import shelve


with shelve.open('class_shelve') as db:
    sue = db['sue']
    tom = db['tom']
    bob = db['bob']
    print(f"{sue.pay = }", f"{bob.pay = }", sep='\n')
    sue.give_raise(.10)
    bob.give_raise(.20)
    print(f"AFTER RAISE: \n{sue.pay = }", f"{bob.pay = }", sep='\n')
    # Refresh DB
    db['sue'] = sue
    db['tom'] = tom
    db['bob'] = bob

    print("\n\t\t\tEND\n")