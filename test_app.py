import pytest
import logging
from check import check_mail
from server import loadClubs


clubs = loadClubs()
logging.basicConfig(level=logging.INFO)


@pytest.mark.parametrize("test_email, expected_result, expected_data", [
    ("", 1, None),
    ("stein@mail.be", 2, None),
    ("john@simplylift.co", 0, {"name": "Simply Lift", "email": "john@simplylift.co", "points": "13"})
])
def test_checkmail(test_email, expected_result, expected_data):
    result, data = check_mail(test_email, clubs)
    logging.info('This is an info message')
    assert result == expected_result
    assert data == expected_data
