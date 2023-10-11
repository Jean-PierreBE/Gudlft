import pytest
import sys
sys.path.append('../')
from server import app as server_app

def pytest_html_report_title(report):
    report.title = "Test report for Gudlft Project"


@pytest.fixture()
def app():
    #app = create_app()
    server_app.config.update({
        "TESTING": True,
    })

    # other setup can go here

    yield server_app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()