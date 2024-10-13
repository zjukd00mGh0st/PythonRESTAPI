from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from . import service as authors_service
from .dto.create_author import CreateAuthorDTO


router = Blueprint("authors", __name__, url_prefix="/authors")


@router.route("/", methods=["GET"])
def get_authors():
    return authors_service.get_authors()

@router.route("/{id}", methods=["GET"])
def get_author_by_id():
    return authors_service.get_author_by_id()

@router.route("/", methods=["POST"])
def create_author():
    data = request.get_json()
    # Validate the input data
    try:
        author_data = CreateAuthorDTO(**data)
        return authors_service.create_author(author_data)
    except ValidationError as e:
        return jsonify({
            "error": e.errors(),
        })


@router.route("/{id}", methods=["PUT"])
def edit_author():
    return authors_service.edit_author()

@router.route("/{id}", methods=["DELETE"])
def delete_author():
    return authors_service.delete_author()
