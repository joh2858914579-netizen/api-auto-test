from utils.api_client import get_forecast


def test_tc01_basic_request_success(valid_params):
    resp = get_forecast(valid_params)
    assert resp.status_code == 200
    assert "application/json" in resp.headers["Content-Type"]
    data = resp.json()
    for key in ("latitude", "longitude", "timezone", "current_weather"):
        assert key in data, f"响应缺少字段 {key}"


def test_tc02_lat_lon_close_to_request(valid_params):
    data = get_forecast(valid_params).json()
    # 接口会把经纬度吸附到网格，不能用 == 比较，用容差
    assert abs(data["latitude"] - 52.52) < 1
    assert abs(data["longitude"] - 13.41) < 1


def test_tc03_current_weather_schema(valid_params):
    cw = get_forecast(valid_params).json()["current_weather"]
    assert isinstance(cw["temperature"], (int, float))
    assert isinstance(cw["windspeed"], (int, float)) and cw["windspeed"] >= 0
    assert isinstance(cw["weathercode"], int)
    assert cw["is_day"] in (0, 1)


def test_tc04_timezone_param():
    data = get_forecast({"latitude": 52.52, "longitude": 13.41,
                         "timezone": "Asia/Shanghai", "current_weather": "true"}).json()
    assert data.get("timezone"), "应返回 timezone 字段"


def test_tc05_daily_variables():
    data = get_forecast({"latitude": 52.52, "longitude": 13.41,
                         "daily": "temperature_2m_max,temperature_2m_min"}).json()
    daily = data["daily"]
    assert len(daily["time"]) == len(daily["temperature_2m_max"]) == len(daily["temperature_2m_min"])


def test_tc06_hourly_multi_variables():
    data = get_forecast({"latitude": 52.52, "longitude": 13.41,
                         "hourly": "temperature_2m,relative_humidity_2m"}).json()
    hourly = data["hourly"]
    assert "temperature_2m" in hourly and "relative_humidity_2m" in hourly
    assert len(hourly["temperature_2m"]) == len(hourly["relative_humidity_2m"])
