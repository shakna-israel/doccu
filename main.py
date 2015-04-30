# # Doccu
# ## *Documentation Engine*

# ## Asynchronous Concurrency
# Here, we import gevent, so we can make use of greenlets to allow for a far larger number of concurrent users.
from gevent import monkey

# Using gevent, we monkeypatch Python's routing system, so that we end up using greenlets without having to mess with our routes.
monkey.patch_all()

from bottle import run, CherryPyServer
import lazyjson

@route("/api/")
@route("/api/version")
def api_version():
  version_file = lazyjson.File('json/version.json')
  return version_file

run(server=CherryPyServer)
