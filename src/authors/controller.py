import json
from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from . import service as authors_service
from .dto.create_author import CreateAuthorDTO
from .dto.get_author_by_id import GetAuthorByIdDTO
from .dto.edit_author import EditAuthorDTO


router = Blueprint("authors", __name__, url_prefix="/authors")


@router.route("/", methods=["GET"])
def get_authors():
    return authors_service.get_authors()

@router.route("/<id>", methods=["GET"])
def get_author_by_id(id):
    # Validate the input data
    try:
        author_id = GetAuthorByIdDTO(id=id)
        return authors_service.get_author_by_id(author_id)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json())
        })

@router.route("/", methods=["POST"])
def create_author():
    data = request.get_json()
    # Validate the input data
    try:
        author_data = CreateAuthorDTO(**data)
        return authors_service.create_author(author_data)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json()),
        })


@router.route("/<id>", methods=["PUT"])
def edit_author(id: str):
    try:
        author_id = GetAuthorByIdDTO(id=id)
        data = request.get_json()
        author_data = EditAuthorDTO(**data)
        return authors_service.edit_author(author_id, author_data)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json())
        })

@router.route("/<id>", methods=["DELETE"])
def delete_author(id: str):
    try:
        author_id = GetAuthorByIdDTO(id=id)
        return authors_service.delete_author(author_id.id)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json())
        })
