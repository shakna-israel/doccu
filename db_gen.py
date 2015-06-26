import pickle

def gen_ids():
	db = {'Trevor Clough':'019282','James Milne':'002255'}
	pickle.dump(db,open("ids.dbs","wb"))

if __name__ == "__main__":
    gen_ids()
