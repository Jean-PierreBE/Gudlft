import pytest

def test_acces_gudlft(client):
    response = client.get("/")
    assert response.status_code == 200

def test_logout(client):
    response = client.get("/logout", follow_redirects=True)
    assert response.status_code == 200
    assert b"Welcome to the GUDLFT Registration Portal!" in response.data

def test_dashboard(client):
    response = client.get("/dashboard", follow_redirects=True)
    assert response.status_code == 200
    assert b"Dashboard of clubs" in response.data
    assert b"Return to the login page" in response.data