def test_get_empty_history(client):
    response = client.get('/history')
    assert response.status_code == 200
    assert response.json == []


def test_get_history(client, populate_history):
    response = client.get('/history')
    assert response.status_code == 200
    assert len(response.json) == 1


def test_delete_history(client, populate_history):
    response = client.delete('/history/1')
    assert response.status_code == 204
    response = client.get('/history')
    assert response.status_code == 200
    assert response.json == []