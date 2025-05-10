import pytest

@pytest.fixture(autouse=False,scope="session")
def setup():
    print("start")
    yield
    print("end")
