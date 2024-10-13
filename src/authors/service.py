from flask import jsonify
# from ..decorators.db_session import inject_db_session
from .dto.create_author import CreateAuthorDTO
from .dto.get_author_by_id import GetAuthorByIdDTO
from .dto.edit_author import EditAuthorDTO
from .dto.get_authors import GetAuthorsDTO


def get_authors(query: GetAuthorsDTO):
    print("This is the query")
    print(query)

    authors = []
    return jsonify({ "authors": authors })


def get_author_by_id(data: GetAuthorByIdDTO):
    print("This is the data")
    print(data)
    return jsonify({
        "author": {},
    })


def create_author(data: CreateAuthorDTO):
    print("This is the data") 
    print(data)

    return jsonify({
        "author": data.model_dump(),
    })


def edit_author(id: str, data: EditAuthorDTO):
    print("This is the data") 
    print(id)
    print(data)
    return jsonify({
        "author": {},
    })



def delete_author(id: str):
    return jsonify({
        "deleted": True,
    })