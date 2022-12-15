"""First hug API (local and HTTP access)"""
import hug
messages = []
from hug.middleware import CORSMiddleware

api = hug.API(__name__)
api.http.add_middleware(CORSMiddleware(api))

@hug.get("/messages")
@hug.local()
def read():
    return messages
    
@hug.options("/messages")
@hug.local()
def read():
    return "mess"

@hug.post("/messages")
@hug.local()
def save(body=None):
  print(body)
  messages.append(body)
  return { "status": "ok" }