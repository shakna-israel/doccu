import pickle
import sys
import subprocess

def generate_id(name,code):
	db = pickle.load(open("ids.dbs", "rb"))
	if code in db.values():
		print("Code not unique!")
		wait = raw_input("Press enter to exit.")
		sys.exit()
	if name in db.keys():
		print("User already exists!")
		choice = raw_input("Overwrite? Y/N")
		if choice == 'y':
			print("Overwriting...")
		elif choice == 'Y':
			print("Overwriting...")
		else:
			print("Not overwriting.")
			wait = raw_input("Press enter to exit.")
			sys.exit()
	db[name] = code
	pickle.dump(db,open("ids.dbs","wb"))
	print("User written to database!")

def remove_id(name):
	db = pickle.load(open("ids.dbs", "rb"))
	del db[name]
	pickle.dump(db,open("ids.dbs","wb"))
	print("User removed from database!")

def main():
	choice = raw_input("Enter 1 to ADD a user, and 2 to REMOVE a User, and 3 to START the server: ")
	if str(choice) == '1':
		unique_name = raw_input("Enter a users UNIQUE name, e.g. Trevor Clough: ")
		unique_name = unique_name.strip()
		unique_name = unique_name.lower()
		unique_code = raw_input("Enter a users UNIQUE code, e.g. 00226677 ")
		unique_code = unique_code.strip()
		generate_id(unique_name,unique_code)
		print("Done!")
		wait = raw_input("Press enter to try exit.")
		sys.exit()
	elif str(choice) == '2':
		unique_name = raw_input("Enter the user's UNIQUE name, e.g. Trevor Clough: ")
		unique_name = unique_name.strip()
		remove_id(unique_name)
		print("Done!")
		wait = raw_input("Press enter to try exit.")
		sys.exit()
	elif str(choice) == '3':
         subprocess.call(["python","app.py"])
	else:
		choice = None
		main()

if __name__ == "__main__":
	main()
