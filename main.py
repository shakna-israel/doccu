# # Doccu
# ## *Documentation Engine*

# ## Asynchronous Concurrency
# Here, we import gevent, so we can make use of greenlets to allow for a far larger number of concurrent users.
from gevent import monkey

# Using gevent, we monkeypatch Python's routing system, so that we end up using greenlets without having to mess with our routes.
monkey.patch_all()

from bottle import run, CherryPyServer, route
import yaml
import uuid
import base64

def get_latest_version(file):
    openfile = open(file,'r')
    versions = yaml.load(openfile)
    previous = '0.0.0'
    for key in versions:
        if key["version"] > previous:
            previous = key["version"]
            previous_name = key["name"]
    openfile.close()
    return ( previous, previous_name )

def get_document_features(file):
    openfile = open(file,'r')
    yaml_data = yaml.load(openfile)
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
    openfile.close()
    return ( version, title, author, signer, group, category, timestamp, body )            

@route("/api")
@route("/api/")
def api_information():
    file = "yaml/versions.yaml"
    grab = get_latest_version(file)
    version = grab[0]
    name = grab[1]
    return { "Version": version, "Name": name }

@route("/api/version")
@route("/api/version/")
def api_version():
    file = "yaml/versions.yaml"
    version = get_latest_version(file)[0]
    return { 'Version': version }

@route("/api/name")
@route("/api/name/")
def api_name():
    file = "yaml/versions.yaml"
    name = get_latest_version(file)[1]
    return { 'Build Name': name }
    
@route("/api/document/<name>", method="GET")
@route("/api/document/<name>/", method="GET")
def document_fetch(name):
    openfile = "yaml/" + str(name) + ".yaml"
    grab_latest = get_document_features(openfile)
    version = grab_latest[0]
    title = grab_latest[1]
    author = grab_latest[2]
    signer = grab_latest[3]
    group = grab_latest[4]
    category = grab_latest[5]
    timestamp = grab_latest[6]
    body = grab_latest[7]
    return { "Version": version, "Title": title, "Author": author, "Signer": signer, "Group": group, "Category": category, "Timestamp": timestamp, "Body": body }
    
@route("/api/document/<name>", method="PUT")
@route("/api/document/<name>/", method="PUT")
def document_fetch(name):
    # If not locked, lock.
        # Store JSON into Python object.
        # Make modifications.
        # Return Python object to JSOn file.
        # Unlock.
    # Else if locked, fail.
    return { 'Implemented': False }

def get_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return r_uuid.replace('=', '_')

def main():
    version = get_latest_version("yaml/versions.yaml")
    print "Running v" + version[0] + ", " + version[1]
    run(host='0.0.0.0', server=CherryPyServer)

if __name__ == "__main__":
    main()
