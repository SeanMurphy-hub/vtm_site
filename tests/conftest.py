import pytest
from app import app as flask_app



@pytest.fixure()
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return client.test_client()
