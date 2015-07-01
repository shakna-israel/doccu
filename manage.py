import pickle
import sys
import subprocess
import requests
from os.path import expanduser
import os

try:
   input = raw_input
except NameError:
   pass

def generate_id(name,code):
    db = pickle.load(open("ids.dbs", "rb"))
    if code in db.values():
        print("Code not unique!")
        wait = input("Press enter to exit.")
        sys.exit()
    if name in db.keys():
        print("User already exists!")
        choice = input("Overwrite? Y/N")
        if choice == 'y':
            print("Overwriting...")
        elif choice == 'Y':
            print("Overwriting...")
        else:
            print("Not overwriting.")
            wait = input("Press enter to exit.")
            sys.exit()
    db[name] = code
    pickle.dump(db,open("ids.dbs","wb"))
    print("User written to database!")

def remove_id(name):
    db = pickle.load(open("ids.dbs", "rb"))
    del db[name]
    pickle.dump(db,open("ids.dbs","wb"))
    print("User removed from database!")

def update_js():
    url_request = requests.get('https://raw.githubusercontent.com/bpampuch/pdfmake/master/build/pdfmake.min.js', stream=True)
    with open('static/js/pdfmake.min.js','wb') as fileOpen:
        for chunk in url_request.iter_content(chunk_size=1024):
            if chunk:
                fileOpen.write(chunk)
                fileOpen.flush()
    url_request = requests.get('https://raw.githubusercontent.com/bpampuch/pdfmake/master/build/vfs_fonts.js', stream=True)
    with open('static/js/vfs_fonts.js','wb') as fileOpen:
        for chunk in url_request.iter_content(chunk_size=1024):
            if chunk:
                fileOpen.write(chunk)
                fileOpen.flush() 

def gen_folder_struct():
    doccu_home = expanduser("~/.doccu")
    doccu_docs = expanduser("~/.doccu/documents")
    if os.path.isdir(doccu_home):
        if os.path.isdir(doccu_docs):
            return True
        else:
            os.makedirs(doccu_docs)
    else:
        os.makedirs(doccu_home)
        os.makedirs(doccu_docs)

def main():
    gen_folder_struct()
    choice = input("Enter 1 to ADD a user, and 2 to REMOVE a User, 3 to START the server, and 4 to updated browser-based dependencies:")
    if str(choice) == '1':
        unique_name = input("Enter a users UNIQUE name, e.g. Trevor Clough: ")
        unique_name = unique_name.strip()
        unique_name = unique_name.lower()
        unique_code = input("Enter a users UNIQUE code, e.g. 00226677 ")
        unique_code = unique_code.strip()
        generate_id(unique_name,unique_code)
        print("Done!")
        wait = input("Press enter to try exit.")
        sys.exit()
    elif str(choice) == '2':
        unique_name = input("Enter the user's UNIQUE name, e.g. Trevor Clough: ")
        unique_name = unique_name.strip()
        remove_id(unique_name)
        print("Done!")
        wait = input("Press enter to try exit.")
        sys.exit()
    elif str(choice) == '3':
        try:
            subprocess.call(["python","app.py"])
        except SystemExit:
            try:
                subprocess.call(["python","app.py"])
            except SystemExit:
                subprocess.call(["python","app.py"])
            except KeyboardInterrupt:
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()
    elif str(choice) == '4':
        print("Updating javascript dependencies...")
        update_js()
        print("Updated!")
    else:
        choice = None
        main()

if __name__ == "__main__":
    main()
