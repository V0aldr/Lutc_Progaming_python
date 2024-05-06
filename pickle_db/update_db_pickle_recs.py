import pickle_db

with open('sue.pkl', 'rb') as sue_db:
    sue = pickle_db.load(sue_db)
    print(sue)

sue['pay'] = round(sue['pay'] * 1.10, 2)
print(sue['pay'])

with open('sue.pkl', 'wb') as sue_db:
    pickle_db.dump(sue, sue_db)

with open('sue.pkl', 'rb') as sue_db:
    sue = pickle_db.load(sue_db)
    print(f"{sue['pay']:.2f}")