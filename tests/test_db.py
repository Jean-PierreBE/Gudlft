"""
this package test the download of database
the database should be not empty
"""
from server import loadClubs, loadCompetitions


def test_load_club():
    """
    return false if the db is not of type None
    """
    ret = isinstance(loadClubs(), type(None))
    assert (ret) is False


def test_load_competitions():
    """
    return false if the db is not of type None
    """
    ret = isinstance(loadCompetitions, type(None))
    assert (ret) is False
