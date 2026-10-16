from utils.api_client import get_forecast, assert_error_response


def test_tc12_missing_latitude():
    resp = get_forecast({"longitude": 13.41})
    assert_error_response(resp, 400)


def test_tc13_missing_longitude():
    resp = get_forecast({"latitude": 52.52})
    assert_error_response(resp, 400)


def test_tc14_latitude_not_numeric():
    resp = get_forecast({"latitude": "abc", "longitude": 13.41})
    assert_error_response(resp, 400)


def test_tc15_latitude_out_of_range():
    resp = get_forecast({"latitude": 95, "longitude": 13.41})
    data = assert_error_response(resp, 400)
    assert "Latitude must be in range" in data["reason"]


def test_tc16_longitude_out_of_range():
    resp = get_forecast({"latitude": 52.52, "longitude": 181})
    assert_error_response(resp, 400)
