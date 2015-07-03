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
    doccu_home = expanduser("~/.doccu")
    db = pickle.load(open(doccu_home + "/ids.dbs", "rb"))
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
    pickle.dump(db,open(doccu_home + "/ids.dbs","wb"))
    print("User written to database!")

def remove_id(name):
    doccu_home = expanduser("~/.doccu")
    db = pickle.load(open(doccu_home + "/ids.dbs", "rb"))
    del db[name]
    pickle.dump(db,open(doccu_home + "/ids.dbs","wb"))
    print("User removed from database!")

def download_file(url, fileName):
    url_request = requests.get(url, stream=True)
    with open(fileName,'wb') as fileOpen:
        for chunk in url_request.iter_content(chunk_size=1024):
            if chunk:
                fileOpen.write(chunk)
                fileOpen.flush()

def update_js():
    doccu_static = expanduser("~/.doccu/static")
    download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/package.json', doccu_static + '/check-version')
    check_version_file = open(doccu_home + '/check-version', 'r')
    try:
        current_version_file = open(doccu_home + '/current-version', 'r')
        check_version = check_version_file[2]
        current_version = current_version_file[2]
        check_version_file.close()
        current_version_file.close()
    except IOError:
        update = True
        check_version = '1'
        current_version = '0'
    if check_version == current_version:
        print("Equal version, no need to update.")
        update = False
    if check_version < current_version:
        print("A newer version is available, updating.")
        update = True
    if current_version > check_version:
        print("Error!")
        assert VersionMismatch
    if update:
        download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/build/pdfmake.min.js', doccu_static + '/js/pdfmake.min.js')
        download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/build/vfs_fonts.js', doccu_static + '/js/vfs_fonts.js')
        download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/package.json', doccu_static + '/current-version')

def update_doccu_server():
    doccu_home = expanduser("~/.doccu")
    download_file('https://raw.githubusercontent.com/shakna-israel/doccu-server/master/version', doccu_home + '/check-version')
    check_version_file = open(doccu_home + '/check-version', 'r')
    try:
        current_version_file = open(doccu_home + '/current-version', 'r')
        for line in check_version_file:
            check_version = line
        for line in current_version_file:
            current_version = line
        check_version_file.close()
        current_version_file.close()
    except IOError:
        update = True
        check_version = '1'
        current_version = '0'
    if check_version == current_version:
        print("Equal version, no need to update.")
        update = False
    if check_version < current_version:
        print("A newer version is available, updating.")
        update = True
    if current_version > check_version:
        print("Error!")
        assert VersionMismatch
    if update:
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-server/master/doccu-server.py', doccu_home + '/doccu-server.py')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-server/master/version', doccu_home + '/current-version')

def update_all_templates():
    doccu_templates = expanduser('~/.doccu/templates')
    download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/version', doccu_templates + '/check-version')
    check_version_file = open(doccu_templates + '/check-version', 'r')
    try:
        current_version_file = open(doccu_templates + '/current-version', 'r')
        for line in check_version_file:
            check_version = line
        for line in current_version_file:
            current_version = line
        check_version_file.close()
        current_version_file.close()
    except IOError:
        update = True
        check_version = '1'
        current_version = '0'
    if check_version == current_version:
        print("Equal version, no need to update.")
        update = False
    if check_version < current_version:
        print("A newer version is available, updating.")
        update = True
    if current_version > check_version:
        print("Error!")
        assert VersionMismatch
    if update:
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/index.html', doccu_templates + '/index.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/styles.html', doccu_templates + '/styles.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/sidebar.html', doccu_templates + '/sidebar.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/new_document_submitted.html', doccu_templates + '/new_document_submitted.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/new_document_denied.html', doccu_templates + '/new_document_denied.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/new_document.html', doccu_templates + '/new_document.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/header.html', doccu_templates + '/header.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/edit_document.html', doccu_templates + '/edit_document.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/document.html', doccu_templates + '/document.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/category.html', doccu_templates + '/category.html')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-templates/master/version', doccu_templates + '/current-version')

def gen_folder_struct():
    doccu_home = expanduser("~/.doccu")
    doccu_docs = expanduser("~/.doccu/documents")
    doccu_static = expanduser("~/.doccu/static")
    doccu_js = expanduser("~/.doccu/static/js")
    doccu_templates = expanduser("~/.doccu/templates")
    if os.path.isdir(doccu_home):
        if os.path.isdir(doccu_docs):
            if os.path.isdir(doccu_static):
                if os.path.isdir(doccu_js):
                    if os.path.isdir(doccu_templates):
                        return True
                    else:
                        os.makedirs(doccu_templates)
                else:
                    os.makedirs(doccu_js)
                    os.makedirs(doccu_templates)
            else:
                os.makedirs(doccu_static)
                os.makedirs(doccu_js)
                os.makedirs(doccu_templates)
        else:
            os.makedirs(doccu_docs)
            os.makedirs(doccu_static)
            os.makedirs(js)
            os.makedirs(doccu_templates)
    else:
        os.makedirs(doccu_home)
        os.makedirs(doccu_docs)
        os.makedirs(doccu_static)
        os.makedirs(doccu_js)
        os.makedirs(doccu_templates)

def check_id_db():
    doccu_home = expanduser('~/.doccu')
    if os.path.isfile(doccu_home + '/ids.dbs'):
        return True
    else:
        db = {}
        pickle.dump(db,open(doccu_home + "/ids.dbs","wb"))

def main():
    gen_folder_struct()
    check_id_db()
    doccu_home = expanduser('~/.doccu')
    choice = input("Enter\n1 to ADD a user\n2 to REMOVE a User\n3 to START the server\n4 to updated browser-based dependencies\n5 to update server-based dependencies\n6 to update the server core:")
    if str(choice) == '1':
        unique_name = input("Enter a users UNIQUE name, e.g. Andrew Conan: ")
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
            subprocess.call(["python", doccu_home + "/doccu-server.py"])
        except SystemExit:
            try:
                subprocess.call(["python", doccu_home + "/doccu-server.py"])
            except SystemExit:
                subprocess.call(["python", doccu_home + "/doccu-server.py"])
            except KeyboardInterrupt:
                sys.exit()
        except KeyboardInterrupt:
            sys.exit()
    elif str(choice) == '4':
        print("Updating javascript dependencies...")
        update_js()
        print("Updated!")
    elif str(choice) == '5':
        print("Updating templates...")
        update_all_templates()
        print("Updated!")
    elif str(choice) == '6':
        print("Updating server...")
        update_doccu_server()
        print("Updated!")
    else:
        choice = None
        main()

if __name__ == "__main__":
    main()
