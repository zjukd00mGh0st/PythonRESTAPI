from os import getenv
from dotenv import load_dotenv

load_dotenv()

HOST = getenv("HOST")
if not HOST:
    raise ValueError("'HOST' environment variable is missing")
PORT = getenv("PORT")
if not PORT:
    raise ValueError("'PORT' environment variable is missing")


workers = 1
bind = f"{HOST}:{PORT}"
reload = True