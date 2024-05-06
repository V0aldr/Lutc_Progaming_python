import pickle, glob


print(f"\n{'----|START|':-<82}\n")

for filename in glob.glob('*.pkl'):  # для ‘bob’,’sue’,’tom’
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(f"{filename} => {record}")


print(f"\n{'----|SUE|':-<82}\n")

suefile = open('sue.pkl', 'rb')
print(f"{pickle.load(suefile)['name'] = }")

print(f"\n{'----|END|':-<82}\n")

