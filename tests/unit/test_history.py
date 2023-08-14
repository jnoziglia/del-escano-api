from api.schema import history


def test_get_empty_history(client, token):
    response = client.get('/history', headers={'Authorization': token})
    assert response.status_code == 200
    assert response.json == []


def test_get_history(client, populate_history, token):
    response = client.get('/history', headers={'Authorization': token})
    assert response.status_code == 200
    assert len(response.json) == 1
