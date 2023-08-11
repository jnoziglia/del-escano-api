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


def test_get_seats_no_parties(client):
    with pytest.raises(ValueError):
        client.get('/seats?seat_count=1')


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
