import pytest
from server import loadClubs, loadCompetitions

def test_load_club():
    ret = isinstance(loadClubs(), type(None))
    assert (ret) == False

def test_load_competitions():
    ret = isinstance(loadCompetitions, type(None))
    assert (ret) == False
