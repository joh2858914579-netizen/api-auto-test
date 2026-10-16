import pytest
import requests

from config import BASE_URL, FORECAST_PATH
from utils.api_client import get_forecast


def test_tc17_nonexistent_path():
    resp = requests.get(BASE_URL + "/v1/nonexistent", timeout=10)
    assert resp.status_code == 404
    assert resp.json().get("error") is True


def test_tc18_post_method_rejected():
    resp = requests.post(BASE_URL + FORECAST_PATH,
                         params={"latitude": 52.52, "longitude": 13.41}, timeout=10)
    assert resp.status_code >= 400, f"POST 应被拒绝，实际 {resp.status_code}"


def test_tc19_timeout_is_surfaced():
    with pytest.raises(requests.exceptions.Timeout):
        get_forecast({"latitude": 52.52, "longitude": 13.41}, timeout=0.001)


def test_tc20_units_metadata_present(valid_params):
    data = get_forecast(valid_params).json()
    assert "current_weather_units" in data
    units = data["current_weather_units"]
    assert "temperature" in units and "windspeed" in units
