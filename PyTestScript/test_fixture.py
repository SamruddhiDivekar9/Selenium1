import pytest

@pytest.fixture()
def setup():
    print("precondition")
    yield
    print("postcondition")

def test_start1(setup):
    print("start1")
def test_start2(setup):
    print("start2")