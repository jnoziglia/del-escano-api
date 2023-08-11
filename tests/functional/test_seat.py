

def test_calculate_seats(client, populate_party):
    response = client.get('/history')
    assert response.status_code == 200
    assert response.json == []
    response = client.get('/seats?seat_count=7')
    assert response.status_code == 200
    assert response.json == [
        {'name': 'partyA', 'votes': 340000, 'seats': 3},
        {'name': 'partyB', 'votes': 280000, 'seats': 3},
        {'name': 'partyC', 'votes': 160000, 'seats': 1},
        {'name': 'partyD', 'votes': 60000, 'seats': 0},
        {'name': 'partyE', 'votes': 15000, 'seats': 0}
    ]
    response = client.get('/history')
    assert response.status_code == 200
    assert len(response.json) == 1


def test_get_seats_no_parties(client):
    response = client.get('/seats?seat_count=1')
    assert response.status_code == 404
    assert response.json == {'msg': 'There are no parties to calculate seats'}
