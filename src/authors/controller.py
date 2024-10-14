import json
from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from urllib.parse import parse_qs
from . import service as authors_service
from .dto.create_author import CreateAuthorDTO
from .dto.get_author_by_id import GetAuthorByIdDTO
from .dto.edit_author import EditAuthorDTO
from .dto.get_authors import GetAuthorsDTO
from ..common.parser.parse_query_dict import parse_query_dict


router = Blueprint("authors", __name__, url_prefix="/authors")


@router.route("/", methods=["GET"])
def get_authors():
    try:
        query = parse_qs(request.query_string.decode())
        query_data = GetAuthorsDTO(**parse_query_dict(query))
        return authors_service.get_authors(query_data)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json()),
        })


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
        data = request.get_json()
        author_data = EditAuthorDTO(**data, id=id)
        return authors_service.edit_author(author_data)
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
