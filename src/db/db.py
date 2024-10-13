import uuid
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship, sessionmaker, scoped_session
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from contextlib import contextmanager
from ..config import DATABASE_URL


engine = create_engine(DATABASE_URL)
Session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()


# Class to implement a singleton (single db instance across the app)
class DBSession:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = Session()
        return cls._instance

# Database entities
class Author(Base):
    __tablename__ = "authors"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    fecha_nacimiento = Column(Date(), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)


class Book(Base):
    __tablename__ = "books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    author_id = Column(UUID, ForeignKey("authors.id"), nullable=False)
    titulo = Column(String(300), nullable=False)
    fecha_publicacion = Column(DateTime(timezone=True), nullable=False)
    fecha_creacion = Column(DateTime(timezone=True), default=datetime.utcnow, nullable=False)


@contextmanager
def db_session():
    session = DBSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def init_db():
    print("Initializing the database")
    print(DATABASE_URL)
    Base.metadata.create_all(engine)