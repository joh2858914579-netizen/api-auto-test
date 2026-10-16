BASE_URL = "https://api.open-meteo.com/v1"
FORECAST_PATH = "/forecast"
DEFAULT_TIMEOUT = 30      # 单次请求超时（秒），CI 服务器跨境访问较慢，给足余量
MAX_RETRIES = 3           # 网络抖动时的最大尝试次数
RETRY_BACKOFF = 0.5       # 重试间隔基数（秒）
