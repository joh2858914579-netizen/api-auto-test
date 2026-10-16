import requests

from config import BASE_URL, FORECAST_PATH, DEFAULT_TIMEOUT


def get_forecast(params, timeout=DEFAULT_TIMEOUT):
    """请求 forecast 接口，params 是参数字典。"""
    return requests.get(BASE_URL + FORECAST_PATH, params=params, timeout=timeout)


def assert_error_response(resp, status):
    """负向用例统一断言：状态码 + error 标记 + reason 非空。"""
    assert resp.status_code == status, f"期望 {status}，实际 {resp.status_code}：{resp.text}"
    data = resp.json()
    assert data.get("error") is True, f"应包含 error:true，实际返回 {data}"
    assert data.get("reason"), "应包含非空 reason 字段"
    return data
