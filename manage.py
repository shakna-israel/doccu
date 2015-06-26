import pickle
import sys
import subprocess

def generate_id(name,code):
	db = pickle.load(open("ids.dbs", "rb"))
	db[name] = code
	pickle.dump(db,open("ids.dbs","wb"))

def remove_id(name):
	db = pickle.load(open("ids.dbs", "rb"))
	del db[name]
	pickle.dump(db,open("ids.dbs","wb"))

def main():
	choice = raw_input("Enter 1 to ADD a user, and 2 to REMOVE a User, and 3 to START the server: ")
	if str(choice) == '1':
		unique_name = raw_input("Enter a users UNIQUE name, e.g. Trevor Clough: ")
		unique_name = unique_name.strip()
		unique_code = raw_input("Enter a users UNIQUE code, e.g. 00226677 ")
		unique_code = unique_code.strip()
		generate_id(unique_name,unique_code)
		print("Done!")
		sys.exit()
	elif str(choice) == '2':
		unique_name = raw_input("Enter the user's UNIQUE name, e.g. Trevor Clough: ")
		unique_name = unique_name.strip()
		remove_id(unique_name)
		print("Done!")
		sys.exit()
	elif str(choice) == '3':
         subprocess.call(["python","app.py"])
	else:
		choice = None
		main()

if __name__ == "__main__":
	main()