from flask import Blueprint, jsonify


router = Blueprint("authors", __name__, url_prefix="/authors")


@router.route("/", methods=["GET"])
def get_authors():
    authors = []
    return { "authors": authors }, 200

@router.route("/{id}", methods=["GET"])
def get_author_by_id():
    author = {}
    return author, 200

@router.route("/", methods=["POST"])
def create_author():
    author = {}
    return author, 201

@router.route("/{id}", methods=["PUT"])
def edit_author():
    return author, 200

@router.route("/{id}", methods=["DELETE"])
def delete_author():
    return "OK", 200
