from flask import jsonify
# from ..decorators.db_session import inject_db_session
from .dto.create_author import CreateAuthorDTO


def get_authors(filters = []):
    authors = []

    return jsonify({ "authors": authors })


def get_author_by_id(id: str):
    pass


def create_author(data: CreateAuthorDTO):
    print("This is the data") 
    print(data)

    return jsonify({
        "author": data.model_dump()
    })


def edit_author(id: str, data):
    pass


def delete_author(id: str):
    pass
