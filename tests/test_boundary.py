from utils.api_client import get_forecast, assert_error_response


def test_tc07_lat_lower_bound():
    resp = get_forecast({"latitude": -90, "longitude": 13.41})
    assert resp.status_code == 200


def test_tc08_lat_upper_bound():
    resp = get_forecast({"latitude": 90, "longitude": 13.41})
    assert resp.status_code == 200


def test_tc09_lon_lower_bound():
    resp = get_forecast({"latitude": 52.52, "longitude": -180})
    assert resp.status_code == 200


def test_tc10_lon_upper_bound():
    resp = get_forecast({"latitude": 52.52, "longitude": 180})
    assert resp.status_code == 200


def test_tc11_lat_just_over_bound():
    resp = get_forecast({"latitude": 90.01, "longitude": 13.41})
    assert_error_response(resp, 400)

def test_tc21_equator_and_prime_meridian():
    resp = get_forecast({"latitude":0,"longitude":0})
    assert resp.status_code == 200
