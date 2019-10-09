import pytest


@pytest.fixture(scope="function")
def app():
    from flask_test.api import app

    return app


@pytest.fixture
def client(app):
    client = app.test_client()

    return client
