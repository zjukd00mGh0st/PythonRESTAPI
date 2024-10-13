from flask import Flask
from dotenv import load_dotenv
from .authors.controller import router as authors_router
from .db.db import init_db

load_dotenv()


app = Flask(__name__)

init_db()

# Healthcheck
@app.route("/")
def index():
    return "OK", 200

# API ROUTES
# Authors
app.register_blueprint(authors_router)

# Books
