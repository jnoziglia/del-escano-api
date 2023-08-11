import pytest


def test_add_party(client):
    response = client.post('/parties', json={
        'name': 'test',
        'votes': 0
    })
    assert response.status_code == 201
    assert response.json == {'id': 1, 'name': 'test', 'votes': 0}


def test_get_empty_parties(client):
    response = client.get('/parties')
    assert response.status_code == 200
    assert response.json == []


def test_get_parties(client, populate_party):
    response = client.get('/parties')
    assert response.status_code == 200
    assert response.json == [
        {'id': 1, 'name': 'partyA', 'votes': 340000},
        {'id': 2, 'name': 'partyB', 'votes': 280000},
        {'id': 3, 'name': 'partyC', 'votes': 160000},
        {'id': 4, 'name': 'partyD', 'votes': 60000},
        {'id': 5, 'name': 'partyE', 'votes': 15000}
    ]


def test_get_empty_party(client):
    response = client.get('/parties/1')
    assert response.status_code == 404


def test_get_party(client, populate_party):
    response = client.get('/parties/1')
    assert response.status_code == 200
    assert response.json == {'id': 1, 'name': 'partyA', 'votes': 340000}


def test_edit_empty_party(client):
    response = client.put('/parties/1', json={
        'name': 'test',
        'votes': 0
    })
    assert response.status_code == 404


def test_edit_party(client, populate_party):
    response = client.put('/parties/1', json={
        'name': 'test',
        'votes': 0
    })
    assert response.status_code == 201
    assert response.json == {'id': 1, 'name': 'test', 'votes': 0}


def test_delete_empty_party(client):
    response = client.delete('/parties/1')
    assert response.status_code == 404


def test_delete_party(client, populate_party):
    response = client.delete('/parties/1')
    assert response.status_code == 204
