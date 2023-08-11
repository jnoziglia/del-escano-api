def test_add_party(client):
    response = client.get('/parties')
    assert response.status_code == 200
    assert response.json == []
    response = client.post('/parties', json={
        'name': 'test',
        'votes': 0
    })
    assert response.status_code == 201
    assert response.json == {'id': 1, 'name': 'test', 'votes': 0}
    response = client.get('/parties')
    assert response.status_code == 200
    assert response.json == [{'id': 1, 'name': 'test', 'votes': 0}]