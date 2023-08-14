

def test_calculate_seats(client, populate_party, token):
    response = client.get('/history', headers={'Authorization': token})
    assert response.status_code == 200
    assert response.json == []
    response = client.get('/seats?seat_count=7', headers={'Authorization': token})
    assert response.status_code == 200
    assert response.json == [
        {'name': 'partyA', 'votes': 340000, 'seats': 3},
        {'name': 'partyB', 'votes': 280000, 'seats': 3},
        {'name': 'partyC', 'votes': 160000, 'seats': 1},
        {'name': 'partyD', 'votes': 60000, 'seats': 0},
        {'name': 'partyE', 'votes': 15000, 'seats': 0}
    ]
    response = client.get('/history', headers={'Authorization': token})
    assert response.status_code == 200
    assert len(response.json) == 1


def test_get_seats_no_parties(client, token):
    response = client.get('/seats?seat_count=1', headers={'Authorization': token})
    assert response.status_code == 404
    assert response.json == {
        'error': 'Not Found',
        'message': 'There are no parties to calculate seats'
    }
