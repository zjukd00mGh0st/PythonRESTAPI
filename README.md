# API REST de una libreria

El siguiente proyecto consiste de una API REST de eventos donde se pueden agregar reservas.
Dados los requerimientos del proyecto se llevo a cabo lo siguiente:

## Tecnologias usadas

- python
- flask
- sqlalchemy (orm)
- postgresql
- docker

**IMPORTANTE**

Es necesario tener **docker** instalado para poder ejecutar la base de datos localmente y el proyecto en general.

### Creacion de la base de datos MySQL

Para crear la base de datos mysql solo es necesario ejecutar el siguiente comando:

```sh
docker compose up -d pydb
```

### Acceder a terminal Postgresql

Para acceder a la terminal postgresql y administrar o explorar la base de datos se debe ejecutar:

```sh
docker exec -it pydb pgsql -U <user> -d <database>
```

### Migraciones

Mediante el uso de la libreria "alembic" es como se llevan a cabo las migraciones de la base de datos en caso de que una columna sea modificada.

```sh
# Inicializar alembic y sus carpetas
alembic init alembic
```

Es importante que los siguientes archivos sean modificados:

- env.py
- alembic.ini

Cuando una columna de la base de datos es modificada se debe crear la migracion mediante el siguiente comando:

```sh
# Crear migracion
alembic revision --autogenerate -m '<migration-message>'
```

```sh
# Aplicar migration
alembic upgrade head
```

### Ejecutar el proyecto

Para poder ejecutar el proyecto solo basta con correr el siguiente comando:

```sh
docker compose up -d nodeapi
```

En este momento los contenedores de docker son instanciados y se pueden realizar peticiones a la API.
