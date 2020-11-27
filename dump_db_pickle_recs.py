# dump_db_pickle_recs.py

import pickle, glob
for filename in glob.glob('*.pkl'): # for 'bob','sue','tom'
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n ', record)

suefile = open('sue.pkl', 'rb')
print(pickle.load(suefile)['name']) # fetch sue's name