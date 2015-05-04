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
    versions = yaml.load(file)
    previous = '0.0.0'
    for key in versions:
        if key["version"] > previous:
            previous = key["version"]
            previous_name = key["name"]
    file.close()
    return ( previous, previous_name )

@route("/api")
@route("/api/")
def api_information():
    file = open("yaml/versions.yaml",'r')
    grab = get_latest_version(file)
    version = grab[0]
    name = grab[1]
    return { "Version": version, "Name": name }

@route("/api/version")
@route("/api/version/")
def api_version():
    version = doccu_vars()[0]
    return { 'Version': version }

@route("/api/name")
@route("/api/name/")
def api_name():
    name = doccu_vars()[1]
    return { 'Build Name': name }
    
@route("/api/document/<name>", method="GET")
@route("/api/document/<name>/", method="GET")
def document_fetch(name):
    # Fetch from JSON file.
    return { 'Implemented': False }

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
    version = get_latest_version(open("yaml/versions.yaml",'r'))
    print "Running v" + version[0] + ", " + version[1]
    run(host='0.0.0.0', server=CherryPyServer)

if __name__ == "__main__":
    main()
