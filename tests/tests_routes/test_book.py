
def test_book_ok(client):
    response = client.get('/book/Spring Festival/Simply Lift', follow_redirects=True)
    assert response.status_code == 200
    assert not b"this competition is unknown !" in response.data
    assert not b"this club is unknown !" in response.data


def test_book_wrong_club(client):
    response = client.get('/book/Spring Festival/Simply Lift1', follow_redirects=True)
    assert response.status_code == 200
    assert not b"this competition is unknown !" in response.data
    assert b"this club is unknown !" in response.data


def test_book_wrong_competition(client):
    response = client.get('/book/jps/Simply Lift', follow_redirects=True)
    assert response.status_code == 200
    assert b"this competition is unknown !" in response.data
    assert not b"this club is unknown !" in response.data
