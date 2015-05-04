# # Doccu
# ## *Documentation Engine*

# ## Asynchronous Concurrency
# Here, we import gevent, so we can make use of greenlets to allow for a far larger number of concurrent users.
from gevent import monkey

# Using gevent, we monkeypatch Python's routing system, so that we end up using greenlets without having to mess with our routes.
monkey.patch_all()

# Here we import the tools from bottle we'll use to run the REST server.
from bottle import run, CherryPyServer, route
import yaml

# This is a little function to find out what version of the REST Server we are running.
def get_latest_version(file):
    openfile = open(file,'r')
    versions = yaml.load(openfile)
    openfile.close()
    previous = '0.0.0'
    for key in versions:
        if key["version"] > previous:
            previous = key["version"]
            previous_name = key["name"]
    return ( previous, previous_name )

# This is a little function to grab all the features of a document stored in our data.
def get_document_features(file):
    try:
        openfile = open(file,'r')
        yaml_data = yaml.load(openfile)
        openfile.close()
        version = '0.0.0'
        for key in yaml_data:
            if key["version"] > version:
                version = key["version"]
                title = key["name"]
                author = key["author"]
                signer = key["signer"]
                group = key["group"]
                category = key["category"]
                timestamp = key["timestamp"]
                body = key["body"]
        return ( version, title, author, signer, group, category, timestamp, body )            
    except IOError:
        return ( False )

# This is a simple function to check that your password hash is in the database, otherwise you won't be allowed to do anything.
def get_auth(auth):
    authorised = False
    authorised_group = False
    file = open("yaml/users.yaml",'r')
    yaml_data = yaml.load(file)
    file.close()
    for key in yaml_data:
        if key["hash"] == auth:
            authorised = True
            authorised_group = key["group"]
    return ( authorised, authorised_group )

# A little bit of a complicated function to sign off on documents.
def sign_doc(auth, group_required, doc):
    authorised = False
    authorised_group = False
    file = open("yaml/users.yaml",'r')
    yaml_data = yaml.load(file)
    file.close()
    for key in yaml_data:
        if key["hash"] == auth:
           authorised = True
           authorised_group = key["group"]
           sign_user = key["username"]
           sign_name = key["name"]
    if authorised:
        if authorised_group = group_required:
            return ( True, sign_user, sign_name  )
    else:
        return ( False )

# This is a URL where you can find all the current information about the API.
@route("/api")
@route("/api/")
def api_information():
    file = "yaml/versions.yaml"
    grab = get_latest_version(file)
    version = grab[0]
    name = grab[1]
    return { "Version": version, "Name": name }

# This URL will give you the current version number of the REST Server.
@route("/api/version")
@route("/api/version/")
def api_version():
    file = "yaml/versions.yaml"
    version = get_latest_version(file)[0]
    return { 'Version': version }

# This URL will give you the current version name of the REST Server.
@route("/api/name")
@route("/api/name/")
def api_name():
    file = "yaml/versions.yaml"
    name = get_latest_version(file)[1]
    return { 'Build Name': name }
    
# This URL will allow you to fetch all the information about a particular document stored in our data.
@route("/api/document/<name>", method="GET")
@route("/api/document/<name>/", method="GET")
def document_fetch(name):
    openfile = "yaml/" + str(name) + ".yaml"
    grab_latest = get_document_features(openfile)
    # TODO: Some sort of ifloop to ensure latest is signed.
    if grab_latest:
        version = grab_latest[0]
        title = grab_latest[1]
        author = grab_latest[2]
        group = grab_latest[4]
        category = grab_latest[5]
        timestamp = grab_latest[6]
        body = grab_latest[7]
        return { "Version": version, "Title": title, "Author": author, "Signer": signer, "Group": group, "Category": category, "Timestamp": timestamp, "Body": body }
    else:
        return ( False )

# This URL will give you a specific version of a document.
# You cannot edit a spcefic version of a document.
@route("/api/document/<name>/<ver>", method="GET")
@route("/api/document/<name>/<ver>/", method="GET")
def get_document_version(name, ver):
    # TODO: Some sort of loop to fetch the specific version of the document.
    return ( False )

# This is a PUT method to modify documents stored in our data. It takes two arguments: The document, and your authorisation.
@route("/api/document/<name>/<auth>/<content>", method="GET")
@route("/api/document/<name>/<auth>/<content>", method="GET")
def document_fetch(name, auth):
    if get_auth(auth):
        # TODO: Lock file for editing.
        # TODO: Increment file version
        # TODO: Update file with content.
        print content
        # TODO: Remove sign for latest version.
        # TODO: Unlock file.
    return ( False )

# This URL allows you to sign off on a document, if you have appropriate permissions.
@route("/api/document/<name>/<auth>/sign", method="GET")
@route("/api/document/<name>/<auth>/sign/", method="GET")
def document_sign(name, auth):
    if sign_doc(auth, group_required, doc):
        # TODO: Lock file for editing.
        # TODO: Sign the specific version of the document.
        # TODO: Unlock file.
        print("Some sort of sign off here.")
    else:
        return ( False )

# This is a URL that allows you to download a file as a particular format.
@route("/api/document/<name>/download/<format>")
@route("/api/document/<name>/download/<format>/")
def download_doc(name, format):
    # TODO: Send the filename and preferred format to a pandoc wrapper.
    # TODO: Return the file to be downloaded.
    return ( False )

# This URL allows a user to fetch a reset-password command.
@route("/api/user/forgot/<user>">
@route("/api/user/forgot/<user>">
def forgotten_password:
    # TODO: Set user password to a random string.
    # TODO: Require user to change password on next login.
    # TODO: Email random string to user linked email address.
    return ( False )

# This URL allows an authorised user to create a new user.
@route("/api/user/create/<auth>/<username>/<name>/<email>")
@route("/api/user/create/<auth>/<username>/<name>/<email>/")
def generate_user(auth, username, name, email):
    # TODO: Check authorisation.
    # TODO: Check if user already exists.
    # TODO: Create new user with random string.
    # TODO: Require user to change password on next login.
    # TODO: Email random string to user linked email address.
    return ( False )

@route("/api/user/<auth>/<username>/<group>")
@route("/api/user/<auth>/<username>/<group>/")
def group_user(auth, group, user):
    # TODO: Check authorisation.
    # Check if user exists.
    # If user exists, assign relevant group.
    return ( False )

# This is the main function that runs the REST Server for us.
def main():
    version = get_latest_version("yaml/versions.yaml")
    print "Running v" + version[0] + ", " + version[1]
    run(host='0.0.0.0', server=CherryPyServer)

if __name__ == "__main__":
    main()
