from . import scan as sc
import pytest

@pytest.fixture
def host_number():
    return "bagel"
    
def test_ping_server(host_number):
    response = sc.ping_server(host_number)
    assert response == 0