# update_db_file.py
from make_db_file import loadDbase, storeDbase

db = loadDbase()   # read db to memory from file

db['sue']['pay'] *= 1.10
db['tom']['name'] = 'Tom Tom'

storeDbase(db)   # safe updated db