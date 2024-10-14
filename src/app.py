from flask import Flask
from dotenv import load_dotenv
from .authors.controller import router as authors_router
from .books.controller import router as books_router
from .db.db import init_db

load_dotenv()

init_db()

app = Flask(__name__)

# Healthcheck
@app.route("/", methods=["GET"])
def index():
    return "OK", 200

# API ROUTES
# Authors
app.register_blueprint(authors_router)
# Books
app.register_blueprint(books_router)
