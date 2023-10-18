"""
this package test the download of database
the database should be not empty
"""
from server import loadClubs, loadCompetitions


def test_load_club():
    """
    return false if the db is not of type None
    """
    clubs = loadClubs()
    assert clubs == [
                {
                    "name":"Simply Lift",
                    "email":"john@simplylift.co",
                    "points":"13"
                },
                {
                    "name":"Iron Temple",
                    "email": "admin@irontemple.com",
                    "points":"4"
                },
                {   "name":"She Lifts",
                    "email": "kate@shelifts.co.uk",
                    "points":"12"
                }
            ]


def test_load_competitions():
    """
    return false if the db is not of type None
    """
    competitions = loadCompetitions()
    assert competitions == [
        {
            "name": "Spring Festival",
            "date": "2020-03-27 10:00:00",
            "numberOfPlaces": "25"
        },
        {
            "name": "Fall Classic",
            "date": "2020-10-22 13:30:00",
            "numberOfPlaces": "13"
        }]
