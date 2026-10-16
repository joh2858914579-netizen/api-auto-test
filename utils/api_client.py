import time

import requests

from config import (
    BASE_URL,
    FORECAST_PATH,
    DEFAULT_TIMEOUT,
    MAX_RETRIES,
    RETRY_BACKOFF,
)


def get_forecast(params, timeout=DEFAULT_TIMEOUT):
    """请求 forecast 接口；网络抖动（连接失败 / 超时）时自动重试。

    注意：只对「网络层异常」重试。4xx / 5xx 是接口的正常响应，不重试。
    """
    url = BASE_URL + FORECAST_PATH
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            return requests.get(url, params=params, timeout=timeout)
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as exc:
            last_error = exc
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_BACKOFF * attempt)
    raise last_error


def assert_error_response(resp, status):
    """负向用例统一断言：状态码 + error 标记 + reason 非空。"""
    assert resp.status_code == status, f"期望 {status}，实际 {resp.status_code}：{resp.text}"
    data = resp.json()
    assert data.get("error") is True, f"应包含 error:true，实际返回 {data}"
    assert data.get("reason"), "应包含非空 reason 字段"
    return data
