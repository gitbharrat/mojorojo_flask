import pytest
from hello import app


@pytest.fixture
def client():
    return app.test_client()


def test_hello(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.data == b'{"Message":"Hi, I am pinging...."}\n'