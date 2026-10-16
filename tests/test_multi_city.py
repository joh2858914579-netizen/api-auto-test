import pytest

from utils.api_client import get_forecast


@pytest.mark.parametrize("latitude,longitude,city", [
    (0, 0, "赤道本初子午线"),
    (39.90, 116.40, "北京"),
    (-33.87, 151.21, "悉尼"),
])
def test_tc22_multiple_cities(latitude, longitude, city):
    resp = get_forecast({"latitude": latitude, "longitude": longitude})
    assert resp.status_code == 200, f"{city}请求失败"
