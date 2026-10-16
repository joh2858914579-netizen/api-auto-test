# api-auto-test

对开源天气 API（Open-Meteo）的接口自动化测试，覆盖正向、边界、非法参数与异常场景，共 20 条用例。

## 技术栈

Python + requests + pytest + pytest-html

## 运行

```bash
pip install -r requirements.txt
pytest
```

运行后在 `reports/report.html` 查看测试报告。

## 用例清单

| 分类 | 文件 | 用例数 |
|---|---|---|
| 正向 | tests/test_positive.py | 6 |
| 边界 | tests/test_boundary.py | 5 |
| 非法参数 | tests/test_invalid.py | 5 |
| 异常与鲁棒 | tests/test_robust.py | 4 |
