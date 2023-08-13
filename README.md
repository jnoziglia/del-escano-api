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
None
##### Response
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
#### POST /parties
##### Description
This endpoint adds a new party.
##### Parameters
```json
{
    "name": "PartyA",
    "votes": 100000
}
```
##### Response
```json
{
    "id": 1,
    "name": "PartyA",
    "votes": 100000
}
```
#### GET /parties/:partyId
##### Description
This endpoint returns a single party.
##### Parameters
None
##### Response
```json
{
    "id": 1,
    "name": "PartyA",
    "votes": 100000
}
```
#### PUT /parties/:partyId
##### Description
This endpoint updates a single party.
##### Parameters
```json
{
    "name": "PartyA2",
    "votes": 200000
}
```
##### Response
```json
{
    "id": 1,
    "name": "PartyA2",
    "votes": 200000
}
```
#### DELETE /parties/:partyId
##### Description
This endpoint deletes a single party.
##### Parameters
Id of the party to be deleted
##### Response
```json

```
#### GET /seats
##### Description
This endpoint calculates the distribution of seats.
##### Parameters
Number of seats to be distributed must be sent in the query string. For example: 
```/seats?seat_count=7``` will calculate the distribution of 7 seats.
##### Response example
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
#### GET /history
##### Description
This endpoint returns the history of calculations.
##### Parameters
No parameters
##### Response example
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