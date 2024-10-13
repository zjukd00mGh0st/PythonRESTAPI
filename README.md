## Tecnologias usadas

## Ejecutar proyecto

### Base de datos

El servicio de la base de datos se obtiene mediante docker para poder tener el contenedor y no instalar el software de DB directamente en el sistema.

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
