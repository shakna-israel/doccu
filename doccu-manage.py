# Import the database.
import pickle
# Import sys so we can tell what OS we're using, and how it's folders work.
import sys
# Import subprocess so we can run the server in its own forking process.
import subprocess
# Import requests so we can access the web sensibly.
import requests
# Import expanduser so we can tell where the ~ folder is, cross-platform.
from os.path import expanduser
import os

# Import linecache and Regular Expressions to make reading pdfmake's package.json easier.
import linecache
import re

# Import multiprocessing so we can update in the background
from multiprocessing import Pool, Process
import time

# Allow Python3 and Python2 inputs to play nicely together.
try:
   input = raw_input
except NameError:
   pass

def generate_id(name,code):
    """Add a user to Doccu's ID database."""
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
    """Check for and remove a user from Doccu's ID database."""
    doccu_home = expanduser("~/.doccu")
    db = pickle.load(open(doccu_home + "/ids.dbs", "rb"))
    del db[name]
    pickle.dump(db,open(doccu_home + "/ids.dbs","wb"))
    print("User removed from database!")

def download_file(url, fileName):
    """A procedural download, to allow for interruptions and large file sizes."""
    url_request = requests.get(url, stream=True)
    with open(fileName,'wb') as fileOpen:
        for chunk in url_request.iter_content(chunk_size=1024):
            if chunk:
                fileOpen.write(chunk)
                fileOpen.flush()

def update_js(verbosity='Loud'):
    """Download all javascript dependencies of Doccu"""
    doccu_static = expanduser("~/.doccu/static")
    update = True
    try:
        download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/package.json', doccu_static + '/js/check-version')
        check_version = linecache.getline(doccu_static + '/js/check-version', 3)
        check_version = re.findall(r'\d+', check_version)
        current_version = linecache.getline(doccu_static + '/js/current-version', 3)
        current_version = re.findall(r'\d+', current_version)
    except IOError:
        update = True
        check_version = '1'
        current_version = '0'
    if check_version == current_version:
        if verbosity == 'Loud':
            print("Equal version, no need to update.")
        update = False
    if check_version < current_version:
        if verbosity == 'Loud':
            print("A newer version is available, updating.")
        update = True
    # This should never be possible, but we can catch the error anyway:
    if current_version > check_version:
        if verbosity == 'Loud':
            print("Error!")
        assert VersionMismatch
    if update:
        download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/build/pdfmake.min.js', doccu_static + '/js/pdfmake.min.js')
        download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/build/vfs_fonts.js', doccu_static + '/js/vfs_fonts.js')
        download_file('https://raw.githubusercontent.com/bpampuch/pdfmake/master/package.json', doccu_static + '/js/current-version')

def update_doccu_server(verbosity='Loud'):
    """Download the Doccu server, if a new version is released."""
    doccu_home = expanduser("~/.doccu")
    # Download the version file, so we can check if we're up to date
    download_file('https://raw.githubusercontent.com/shakna-israel/doccu-server/master/version', doccu_home + '/check-version')
    check_version_file = open(doccu_home + '/check-version', 'r')
    # Load the version files; both the current one, and the one we have just downloaded.
    try:
        current_version_file = open(doccu_home + '/current-version', 'r')
        for line in check_version_file:
            check_version = line
        for line in current_version_file:
            current_version = line
        check_version_file.close()
        current_version_file.close()
    # If no version is found, force an update.
    except IOError:
        update = True
        check_version = '1'
        current_version = '0'
    if check_version == current_version:
        if verbosity == 'Loud':
            print("Equal version, no need to update.")
        update = False
    if check_version < current_version:
        if verbosity == 'Loud':
            print("A newer version is available, updating.")
        update = True
    # This should never be possible, but we can catch the error anyway:
    if current_version > check_version:
        if verbosity == 'Loud':
            print("Error!")
        assert VersionMismatch
    if update:
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-server/master/doccu-server.py', doccu_home + '/doccu-server.py')
        download_file('https://raw.githubusercontent.com/shakna-israel/doccu-server/master/version', doccu_home + '/current-version')

def update_all_templates(verbosity='Loud'):
    """Download all of Doccu's templates, if a new version has been released."""
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
        if verbosity == 'Loud':
            print("Equal version, no need to update.")
        update = False
    if check_version < current_version:
        if verbosity == 'Loud':
            print("A newer version is available, updating.")
        update = True
    if current_version > check_version:
        if verbosity == 'Loud':
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
    """Create Doccu's folder structure, skipping any folders that already exist."""
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
    """Check if the ID database for Doccu exists, if not, create it."""
    doccu_home = expanduser('~/.doccu')
    if os.path.isfile(doccu_home + '/ids.dbs'):
        return True
    else:
        db = {}
        pickle.dump(db,open(doccu_home + "/ids.dbs","wb"))

def auto_update():
    now = time.time()
    while time.time() < now + 60:
        update_js('silent')
        update_all_templates('silent')
        update_doccu_server('silent')

def main():
    gen_folder_struct()
    check_id_db()
    doccu_home = expanduser('~/.doccu')
    updateProcess = Process(target=auto_update)
    updateProcess.start()

    choice = input("Enter\n1 to run initial setup\n2 to ADD a user\n3 to REMOVE a User\n4 to START the server\n5 to updated browser-based dependencies\n6 to update server-based dependencies\n7 to update the server core:")

    if str(choice) == '1':
        unique_name = input("Enter a users UNIQUE name, e.g. Andrew Conan: ")
        unique_name = unique_name.strip()
        unique_name = unique_name.lower()
        unique_code = input("Enter a users UNIQUE code, e.g. 00226677 ")
        unique_code = unique_code.strip()
        generate_id(unique_name,unique_code)
        print("Done!")
        wait = input("Press enter to move to the next step.")
        print("Updating components...")
        update_js()
        print("30%...")
        update_all_templates()
        print("60%......")
        update_doccu_server()
        print("Done.")
        wait = input("Press enter to move to exit.")
        sys.exit()
    if str(choice) == '2':
        unique_name = input("Enter a users UNIQUE name, e.g. Andrew Conan: ")
        unique_name = unique_name.strip()
        unique_name = unique_name.lower()
        unique_code = input("Enter a users UNIQUE code, e.g. 00226677 ")
        unique_code = unique_code.strip()
        generate_id(unique_name,unique_code)
        print("Done!")
        wait = input("Press enter to try exit.")
        sys.exit()
    elif str(choice) == '3':
        unique_name = input("Enter the user's UNIQUE name, e.g. Trevor Clough: ")
        unique_name = unique_name.strip()
        remove_id(unique_name)
        print("Done!")
        wait = input("Press enter to try exit.")
        sys.exit()
    elif str(choice) == '4':
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
    elif str(choice) == '5':
        print("Updating javascript dependencies...")
        update_js()
        print("Updated!")
    elif str(choice) == '6':
        print("Updating templates...")
        update_all_templates()
        print("Updated!")
    elif str(choice) == '7':
        print("Updating server...")
        update_doccu_server()
        print("Updated!")
    else:
        choice = None
        main()

if __name__ == "__main__":
    main()
