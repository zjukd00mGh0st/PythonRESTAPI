from flask import jsonify
from sqlalchemy.exc import IntegrityError
from .dto.create_author import CreateAuthorDTO
from .dto.get_author_by_id import GetAuthorByIdDTO
from .dto.edit_author import EditAuthorDTO
from .dto.get_authors import GetAuthorsDTO
from ..db.db import Author, db_session
from typing import List, Dict


def create_author(data: CreateAuthorDTO):
    author = Author(**data.model_dump())

    with db_session() as session:
        session.add(author)
        session.commit()
        return jsonify({
            "autor": {
                "id": author.id,
                "fecha_creacion": author.fecha_creacion,
                **data.model_dump(),
            },
        }), 201

def get_authors(query: GetAuthorsDTO):
    authors_list: List[Dict] = []
    with db_session() as session:
        authors = session.query(Author).filter_by(**query.model_dump()).all()
        for author in authors:
            authors_list.append({
                "id": author.id,
                "nombre": author.nombre,
                "apellido": author.apellido,
                "fecha_nacimiento": author.fecha_nacimiento,
                "fecha_creacion": author.fecha_creacion,
            })
        return jsonify({ "authors": authors_list })


def get_author_by_id(data: GetAuthorByIdDTO):
    with db_session() as session:
        author = session.query(Author).filter_by(id=data.id).first()
        if not author:
            return jsonify({
                "error": "El autor no existe"
            }), 404

        return jsonify({
            "author": {
                "id": author.id,
                "nombre": author.nombre,
                "apellido": author.apellido,
                "fecha_nacimiento": author.fecha_nacimiento,
                "fecha_creacion": author.fecha_creacion,
            },
        })


def edit_author(data: EditAuthorDTO):
    with db_session() as session:
        author = session.query(Author).filter_by(id=data.id).first()
        if not author:
            return jsonify({
                "error": "El autor no existe"
            }), 404

        if data.nombre and author.nombre != data.nombre:
            author.nombre = data.nombre
        if data.apellido and author.apellido != data.apellido:
            author.apellido = data.apellido
        if data.fecha_nacimiento and author.fecha_nacimiento != data.fecha_nacimiento:
            author.fecha_nacimiento = data.fecha_nacimiento

        session.add(author)
        session.commit()

        return jsonify({
            "author": {
                "id": author.id,
                "nombre":author.nombre,
                "apellido":author.apellido,
                "fecha_nacimiento":author.fecha_nacimiento,
                "fecha_creacion": author.fecha_creacion,
            },
        })


def delete_author(id: str):
    with db_session() as session:
        author = session.query(Author).filter_by(id=id).first()
        if not author:
            return jsonify({
                "error": "El autor no existe",
            }), 404
        try:
            session.delete(author)
            session.commit()
        except IntegrityError:
            return jsonify({
                "error": "El autor tiene libros asociados (no puede ser eliminado)",
            })

    return "OK", 200