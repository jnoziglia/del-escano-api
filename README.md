# Del EsCaño
### Introduction
Del EsCaño es una API que permite calcular cuantos escaños le corresponden a cada lista o partido político en una elección. El cálculo es realizado utilizando el sistema D'Hondt.
### Project Support Features

### Installation Guide

### Usage

### API Endpoints
| HTTP Verbs | Endpoints         | Action                                      |
|------------|-------------------|---------------------------------------------|
| GET        | /parties          | Obtener todas las listas                    |
| POST       | /parties          | Agregar una lista                           |
| GET        | /parties/:partyId | Obtener una lista                           |
| PUT        | /parties/:partyId | Editar una lista                            |
| DELETE     | /parties/:partyId | Eliminar una lista                          |
| GET        | /seats            | Calcular la distribución de escaños         |
| GET        | /history          | Obtener el historial de cálculos realizados |
### Sample Requests and Responses
#### GET /parties
##### Description
This endpoint returns all parties.
##### Parameters
No parameters
##### Response example
```json
[
    {
        "name": "PartyA",
        "votes": 100000
    },
    {
        "name": "PartyB",
        "votes": 50000
    }
]
```
#### POST /parties
##### Description
This endpoint adds a new party.
##### Parameters
No parameters
##### Request example
```json
{
    "name": "PartyA",
    "votes": 100000
}
```
##### Response
```json
{
    "message": "Lista agregada exitosamente",
    "data": {
        "_id": "5d0f1b3b1c9d440000d1c9d4",
        "name": "Partido de la U",
        "votes": 100000,
        "createdAt": "2019-06-23T20:54:03.000Z",
        "updatedAt": "2019-06-23T20:54:03.000Z",
        "__v": 0
    }
}
```
#### GET /parties/:partyId
##### Description
This endpoint returns a single party.
##### Parameters
Id of the party to be returned
##### Response example
```json
{
    "message": "Lista obtenida exitosamente",
    "data": {
        "_id": "5d0f1b3b1c9d440000d1c9d4",
        "name": "Partido de la U",
        "votes": 100000,
        "createdAt": "2019-06-23T20:54:03.000Z",
        "updatedAt": "2019-06-23T20:54:03.000Z",
        "__v": 0
    }
}
```
#### PUT /parties/:partyId
##### Description
This endpoint updates a single party.
##### Parameters
Id of the party to be updated
##### Request example
```json
{
    "name": "PartyA",
    "votes": 100000
}
```
##### Response example
```json
{
    "message": "Lista actualizada exitosamente",
    "data": {
        "_id": "5d0f1b3b1c9d440000d1c9d4",
        "name": "Partido de la U",
        "votes": 100000,
        "createdAt": "2019-06-23T20:54:03.000Z",
        "updatedAt": "2019-06-23T20:54:03.000Z",
        "__v": 0
    }
}
```
#### DELETE /parties/:partyId
##### Description
This endpoint deletes a single party.
##### Parameters
Id of the party to be deleted
##### Response example
```json
{
    "message": "Lista eliminada exitosamente",
    "data": {
        "_id": "5d0f1b3b1c9d440000d1c9d4",
        "name": "Partido de la U",
        "votes": 100000,
        "createdAt": "2019-06-23T20:54:03.000Z",
        "updatedAt": "2019-06-23T20:54:03.000Z",
        "__v": 0
    }
}
```
#### GET /seats
##### Description
This endpoint calculates the distribution of seats.
##### Parameters
Number of seats to be distributed
##### Response example
```json
{
    "message": "Cálculo realizado exitosamente",
    "data": [
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
```
#### GET /history
##### Description
This endpoint returns the history of calculations.
##### Parameters
No parameters
##### Response example
```json
{
    "message": "Historial obtenido exitosamente",
    "data": [
        {
            "_id": "5d0f1b3b1c9d440000d1c9d4",
            "name": "Partido de la U",
            "votes": 100000,
            "createdAt": "2019-06-23T20:54:03.000Z",
            "updatedAt": "2019-06-23T20:54:03.000Z",
            "__v": 0
        },
        {
            "_id": "5d0f1b3b1c9d440000d1c9d4",
            "name": "Partido de la U",
            "votes": 100000,
            "createdAt": "2019-06-23T20:54:03.000Z",
            "updatedAt": "2019-06-23T20:54:03.000Z",
            "__v": 0
        }
    ]
}
```