"""
    integrations tests for purchase
"""


def test_purchase_ok(client):
    response = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "submit_button": "Book",
        "places": 5,
    })
    assert response.status_code == 200
    assert b"Great-booking complete!" in response.data
    assert b"Welcome, john@simplylift.co" in response.data


def test_purchase_cancel(client):
    response = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "submit_button": "Cancel",
        "places": 5,
    })
    assert response.status_code == 200
    assert b"Great-booking complete!" not in response.data
    assert b"Welcome, john@simplylift.co" in response.data


def test_purchase_error(client):
    response = client.post("/purchasePlaces", data={
        "competition": "Spring Festival",
        "club": "Simply Lift",
        "submit_button": "Book",
        "places": 0,
    })
    assert response.status_code == 200
    assert b"Great-booking complete!" not in response.data
    assert b"Places available:" in response.data
    assert b"number of places = 0 !!" in response.data
