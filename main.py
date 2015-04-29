# # Doccu
# ## *Documentation Engine*

# ## Asynchronous Concurrency
# Here, we import gevent, so we can make use of greenlets to allow for a far larger number of concurrent users.
from gevent import monkey

# Using gevent, we monkeypatch Python's routing system, so that we end up using greenlets without having to mess with our routes.
monkey.patch_all()

from bottle import run, CherryPyServer

run(server=CherryPyServer)
