# # Doccu
# ## *Documentation Engine*

# ## Asynchronous Concurrency
# Here, we import gevent, so we can make use of greenlets to allow for a far larger number of concurrent users.
from gevent import monkey

# Using gevent, we monkeypatch Python's routing system, so that we end up using greenlets without having to mess with our routes.
monkey.patch_all()

from bottle import run, CherryPyServer, route
import json

def doccu_vars():
    version = "0.0.1"
    name = "Semantic Arguments"
    return ( version, name )

@route("/api")
@route("/api/")
def api_information():
    version = doccu_vars()[0]
    name = doccu_vars()[1]
    return { 'Version': version, 'Build Name': name }

@route("/api/version")
@route("/api/version/")
def api_version():
    version = doccu_vars()[0]
    return { 'Version': version }

@route("/api/name")
@route("/api/name/")
    name = doccu_vars()[1]
    return { 'Build Name': name }

run(host='0.0.0.0', server=CherryPyServer)
