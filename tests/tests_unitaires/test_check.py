"""
this package test functions to
       mail for the registration
       number of places
       presence of club or competition
"""
import pytest
from utilities.check import check_mail, check_places, check_name
from server import loadClubs, loadCompetitions
PLACES_AVAILABLE = 25
NUMBER_POINTS = 13
NUMBER_POINTS_BIS = 4

clubs = loadClubs()
competitions = loadCompetitions()


@pytest.mark.parametrize("test_email, expected_result, expected_data", [
    ("", 1, None),  #
    ("stein@mail.be", 2, None),
    ("john@simplylift.co", 0, {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"})
])
def test_checkmail(test_email, expected_result, expected_data):
    result, data = check_mail(test_email, clubs)
    assert result == expected_result
    assert data == expected_data


@pytest.mark.parametrize("test_name_club, expected_result, expected_data", [
    ("", 1, None),  #
    ("stein club", 2, None),
    ("Simply Lift", 0, {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"})
])
def test_checkclub(test_name_club, expected_result, expected_data):
    result, data = check_name(test_name_club, clubs)
    assert result == expected_result
    assert data == expected_data


@pytest.mark.parametrize("test_name_competition, expected_result, expected_data", [
    ("", 1, None),  #
    ("stein festival ", 2, None),
    ("Spring Festival", 0, {"name": "Spring Festival", "date": "2020-03-27 10:00:00", "numberOfPlaces": "25"})
])
def test_checkcompetition(test_name_competition, expected_result, expected_data):
    result, data = check_name(test_name_competition, competitions)
    assert result == expected_result
    assert data == expected_data


@pytest.mark.parametrize("test_places, expected_result", [
    (4, 0),
    ("", 1),
    (0, 2),
    (-2, 3),
    (26, 4),
    (13, 5)
])
def test_checkplaces(test_places, expected_result):
    result = check_places(test_places, PLACES_AVAILABLE, NUMBER_POINTS)
    assert result == expected_result


@pytest.mark.parametrize("test_places_bis, expected_result", [
    (4, 0),
    (5, 6)
])
def test_checkplacesbis(test_places_bis, expected_result):
    result = check_places(test_places_bis, PLACES_AVAILABLE, NUMBER_POINTS_BIS)
    assert result == expected_result
