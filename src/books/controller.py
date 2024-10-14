import json
from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from urllib.parse import parse_qs
from .dto.create_book import CreateBookDTO
from .dto.edit_book import EditBookDTO
from .dto.get_books import GetBooksDTO
from ..common.dto.get_entity_by_id import GetEntityByIDDTO
from ..common.parser.parse_query_dict import parse_query_dict
from . import service as books_service


router = Blueprint("books", __name__, url_prefix="/books")

@router.route("/", methods=["GET"])
def get_books():
    query = parse_qs(request.query_string.decode())
    try:
        query_data = GetBooksDTO(**parse_query_dict(query))
        return books_service.get_books(query_data)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json())
        })

@router.route("/", methods=["POST"])
def create_book():
    data = request.get_json()
    try:
        book_data = CreateBookDTO(**data)
        return books_service.create_book(book_data)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json()),
        })

@router.route("/<id>", methods=["GET"])
def get_book_by_id(id):
    try:
        GetEntityByIDDTO(id=id)
        return books_service.get_book_by_id(id)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json()),
        })

@router.route("/<id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()
    try:
        book_data = EditBookDTO(**data, id=id)
        return books_service.update_book(book_data)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json())
        })

@router.route("/<id>", methods=["DELETE"])
def delete_book(id):
    try:
        GetEntityByIDDTO(id=id)
        return books_service.delete_book(id)
    except ValidationError as e:
        return jsonify({
            "error": json.loads(e.json())
        })
