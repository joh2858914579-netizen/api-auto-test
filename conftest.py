import pytest


@pytest.fixture
def valid_params():
    """一组保证合法的参数，正向用例复用。"""
    return {"latitude": 52.52, "longitude": 13.41, "current_weather": "true"}
