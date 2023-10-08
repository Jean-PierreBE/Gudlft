import pytest
import logging
from check import check_mail, check_places
from server import loadClubs
PLACES_AVAILABLE = 25

clubs = loadClubs()
logging.basicConfig(level=logging.INFO)


@pytest.mark.parametrize("test_email, expected_result, expected_data", [
    ("", 1, None),
    ("stein@mail.be", 2, None),
    ("john@simplylift.co", 0, {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"})
])
def test_checkmail(test_email, expected_result, expected_data):
    result, data = check_mail(test_email, clubs)
    assert result == expected_result
    assert data == expected_data


@pytest.mark.parametrize("test_places, expected_result", [
    ("", 1),
    (0, 2),
    (-2, 3),
    (25, 4),
    (13, 5)
])
def test_checkplaces(test_places, expected_result):
    result = check_places(test_places, PLACES_AVAILABLE)
    assert result == expected_result
