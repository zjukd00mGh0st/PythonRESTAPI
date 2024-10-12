from flask import Flask, jsonify
from .authors.service import router as authors_router


app = Flask(__name__)

# Healthcheck
@app.route("/")
def index():
    return "OK", 200

# API ROUTES
# Authors
app.register_blueprint(authors_router)

# Books
