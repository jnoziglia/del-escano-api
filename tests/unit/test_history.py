def test_get_empty_history(client):
    response = client.get('/history')
    assert response.status_code == 200
    assert response.json == []


def test_get_history(client, populate_history):
    response = client.get('/history')
    assert response.status_code == 200
    assert len(response.json) == 1
