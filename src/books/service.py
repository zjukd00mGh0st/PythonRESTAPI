from flask import jsonify
from ..db.db import Book
from .dto.create_book import CreateBookDTO
from .dto.edit_book import EditBookDTO
from .dto.get_books import GetBooksDTO
from ..db.db import db_session


def create_book(data: CreateBookDTO):
    book = Book(**data.model_dump())

    with db_session() as session:
        session.add(book)
        session.commit()
        return jsonify({
            "libro": {
                "id": book.id,
                "author_id": book.author_id,
                "titulo": book.titulo,
                "fecha_publicacion": book.fecha_publicacion,
                "fecha_creacion": book.fecha_creacion,
            },
        }), 201


def get_books(query: GetBooksDTO):
    books = []

    return jsonify({
        "libros": books,
    })


def get_book_by_id(id: str):
    with db_session() as session:
        book = session.query(Book).filter_by(id=id).first() 
        if not book:
            return jsonify({
                "error": "El libro no existe"
            }), 404
        return jsonify({
            "libro": {
                "id": book.id,
                "author_id": book.author_id,
                "titulo": book.titulo,
                "fecha_publicacion": book.fecha_publicacion,
                "fecha_creacion": book.fecha_creacion,
            }
        })


def update_book(data: EditBookDTO):
    with db_session() as session: 
        book = session.query(Book).filter_by(id=data.id).first()
        if not book:
            return jsonify({
                "error": "El libro no existe"
            }), 404

        if data.titulo and book.titulo != data.titulo:
            book.titulo = data.titulo
        if data.fecha_publicacion and book.fecha_publicacion != data.fecha_publicacion:
            book.fecha_publicacion = data.fecha_publicacion

        session.add(book)
        session.commit()
        
        return jsonify({
            "libro": {
                "id": book.id,
                "author_id": book.author_id,
                "titulo": book.titulo,
                "fecha_publicacion": book.fecha_publicacion,
                "fecha_creacion": book.fecha_creacion,
            }
        })


def delete_book(id: str):
    with db_session() as session: 
        book = session.query(Book).filter_by(id=id).first()
        if not book:
            return jsonify({
                "error": "El libro no existe"
            }), 404

        session.delete(book)
        session.commit()
    
        return "OK", 200