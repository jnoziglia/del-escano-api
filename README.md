# Del EsCaño
### Introducción
Del EsCaño es una API que permite calcular cuantos escaños le corresponden a cada lista o partido político en una elección. El cálculo es realizado utilizando el sistema D'Hondt.

Dado que esta API está desarrollada como parte de un desafío técnico, y con el fin de simplificar su ejecución, no se ha implementado un sistema de autenticación robusto. Por lo tanto, se recomienda no utilizar esta API en un entorno de producción. Asimismo, cierta información que en un caso real sería sensible, como por ejemplo la clave de la API, se encuentra dentro del código subido a este repositorio.

### Funcionalidades
* Los usuarios pueden registrarse y loguearse.
* Los usuarios deben estar logueados para poder utilizar la API.
* Los usuarios pueden crear, editar y eliminar listas o partidos políticos.
* Los usuarios pueden calcular la distribución de escaños.
* Los usuarios pueden ver el historial de cálculos realizados.

### Herramientas necesarias
Para correr esta API es necesario contar con Docker.

### Guía de instalación
* Clonar este repositorio (https://github.com/jnoziglia/del-escano-api.git)
* Dentro de la carpeta del proyecto, ejecutar el comando ```docker compose build``` para construir la imagen de Docker.

### Uso
* Ejecutar el comando ```docker compose up``` para levantar el contenedor.
* La API estará disponible en http://localhost:5000.

### Endpoints de la API
| Métodos HTTP | Endpoints         | Acción                                      |
|--------------|-------------------|---------------------------------------------|
| POST         | /users            | Crear un usuario nuevo                      |
| POST         | /users/login      | Ingresar a la API                           |
| GET          | /parties          | Obtener todas las listas                    |
| POST         | /parties          | Agregar una lista                           |
| GET          | /parties/:partyId | Obtener una lista                           |
| PUT          | /parties/:partyId | Editar una lista                            |
| DELETE       | /parties/:partyId | Eliminar una lista                          |
| GET          | /seats            | Calcular la distribución de escaños         |
| GET          | /history          | Obtener el historial de cálculos realizados |

### Códigos de respuesta
| Código | Referencia            | Descripción                                                                                    |
|--------|-----------------------|------------------------------------------------------------------------------------------------|
| 200    | OK                    | Todo funciona según lo esperado                                                                |
| 201    | Created               | El recurso fue creado o editado exitosamente                                                   |
| 204    | No Content            | El recurso fue borrado exitosamente                                                            |
| 400    | Bad Request           | La solicitud no pudo ser procesada. Posiblemente a causa de parámetros faltantes o incorrectos |
| 401    | Unauthorized          | El token de autenticación es inválido o no fue enviado                                         |
| 403    | Forbidden             | La clave de API no tiene permiso para realizar esta acción                                     |
| 404    | Not Found             | El recurso solicitado no existe                                                                |
| 405    | Method not allowed    | La url solicitada no es válida                                                                 |
| 409    | Conflict              | Ya existe otro recurso con el mismo valor de referencia                                        |
| 500    | Internal Server Error | Error interno del servidor                                                                     |

### Solicitudes y respuestas
#### POST /users
##### Descripción
* Este endpoint crea un usuario nuevo.
* Debe enviarse en el body de la solicitud el email del usuario y la contraseña.
* Recibe como respuesta un mensaje de éxito.
##### Parámetros
```json
{
    "email": "test@test.com",
    "password": "123456"
}
```
##### Respuesta
```json
{
    "message": "User created successfully. Use your email and password at /users/login to login to the API"
}
```
------------
#### POST /users/login
##### Descripción
* Este endpoint permite ingresar a la API.
* Debe enviarse en el body de la solicitud el email del usuario y la contraseña.
* Recibe como respuesta un token de autenticación.
* Este token debe ser enviado en el header de las solicitudes a la API.
* El token tiene una duración de 1 hora.
##### Parámetros
```json
{
    "email": "test@test.com",
    "password": "123456"
}
```
##### Respuesta
```json
{
    "message": "Successfully fetched auth token",
    "token": "example_token"
}
```
------------
#### GET /parties
##### Descripción
* Este endpoint devuelve todas las listas o partidos políticos.
* La respuesta incluye el id, nombre y cantidad de votos de cada lista.
##### Parámetros
Ninguno
##### Respuesta
```json
[
    {
        "id": 1,
        "name": "PartyA",
        "votes": 100000
    },
    {
        "id": 2,
        "name": "PartyB",
        "votes": 50000
    }
]
```
------------
#### POST /parties
##### Descripción
* Este endpoint crea una nueva lista o partido político.
* Debe enviarse en el body de la solicitud el nombre y la cantidad de votos de la lista.
* Recibirá como respuesta el id, nombre y cantidad de votos de la lista creada.
##### Parámetros
```json
{
    "name": "PartyA",
    "votes": 100000
}
```
##### Respuesta
```json
{
    "id": 1,
    "name": "PartyA",
    "votes": 100000
}
```
------------
#### GET /parties/:partyId
##### Descripción
* Este endpoint devuelve una lista o partido político.
* La respuesta incluye el id, nombre y cantidad de votos de la lista.
##### Parámetros
Ninguno
##### Respuesta
```json
{
    "id": 1,
    "name": "PartyA",
    "votes": 100000
}
```
------------
#### PUT /parties/:partyId
##### Descripción
* Este endpoint edita una lista o partido político.
* Debe enviarse en el body de la solicitud el nombre y/o la cantidad de votos de la lista.
* Recibirá como respuesta el id, nombre y cantidad de votos de la lista editada.
##### Parámetros
```json
{
    "name": "PartyA2",
    "votes": 200000
}
```
##### Respuesta
```json
{
    "id": 1,
    "name": "PartyA2",
    "votes": 200000
}
```
------------
#### DELETE /parties/:partyId
##### Descripción
* Este endpoint elimina una lista o partido político.
* Recibirá como respuesta un objeto vacío y el código de respuesta 204.
##### Parámetros
Ninguno
##### Respuesta
```json

```
------------
#### GET /seats
##### Descripción
* Este endpoint calcula la distribución de escaños.
* Debe enviarse en la query string la cantidad de escaños a distribuir.
##### Parámetros
Cantidad de escaños a distribuir. Por ejemplo: 
```/seats?seat_count=7``` calculará la distribución de 7 escaños.
##### Respuesta
```json
[
    {
        "name": "PartyA",
        "votes": 100000,
        "seats": 5
    },
    {
        "name": "PartyB",
        "votes": 50000,
        "seats": 2
    }
]
```
------------
#### GET /history
##### Descripción
* Este endpoint devuelve el historial de cálculos realizados.
* La respuesta incluye la fecha de creación, el id y el resultado de cada cálculo.
##### Parámetros
Ninguno
##### Respuesta
```json
[
    {
        "created_at": "2023-13-08T00:00:00.000Z",
        "id": "1",
        "result": [
            {
                "name": "PartyA",
                "votes": 100000,
                "seats": 5
            },
            {
                "name": "PartyB",
                "votes": 50000,
                "seats": 2
            }
        ]
    }
]
```

### Tecnologías y paquetes utilizadas
* [Python](https://www.python.org/) - Lenguaje de programación
* [Pipenv](https://pipenv.pypa.io/en/latest/) - Entorno virtual
* [Flask](https://flask.palletsprojects.com/en/2.3.x/) - Framework
* [Marshmallow](https://marshmallow.readthedocs.io/en/stable/) - Serialización y deserialización de objetos
* [Flask-Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) - Integración de Marshmallow con Flask
* [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/) - ORM
* [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/) - Migraciones de la base de datos
* [Marshmallow-SQLAlchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/) - Integración de Marshmallow con SQLAlchemy
* [Pytest](https://docs.pytest.org/en/7.4.x/) - Testing
* [Coverage](https://coverage.readthedocs.io/en/7.3.0/) - Cobertura de código
* [SQLite](https://www.sqlite.org/index.html) - Base de datos
* [PyJWT](https://pyjwt.readthedocs.io/en/stable/) - Autenticación con JWT
* [Docker](https://www.docker.com/) - Contenedores