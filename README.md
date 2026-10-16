# api-auto-test

![API Tests](https://github.com/joh2858914579-netizen/api-auto-test/actions/workflows/ci.yml/badge.svg)

对开源天气 API（Open-Meteo）的接口自动化测试项目，共 **24 条用例**，覆盖正向、边界、非法参数与异常四类场景，每次提交都会在 GitHub Actions 上自动回归。

## 测试结果

```
24 passed in ~20s
```

## 技术栈

Python · requests · pytest · pytest-html · GitHub Actions

## 用例设计

| 分类 | 文件 | 用例数 | 验证内容 |
|---|---|---|---|
| 正向 | [tests/test_positive.py](tests/test_positive.py) | 6 | 状态码、Content-Type、字段结构、字段类型与取值范围 |
| 边界 | [tests/test_boundary.py](tests/test_boundary.py) | 6 | 经纬度上下边界（±90 / ±180）、赤道与本初子午线、越界一点点 |
| 非法参数 | [tests/test_invalid.py](tests/test_invalid.py) | 5 | 参数缺失、非数值、超出范围，断言 `error:true` 与 `reason` |
| 异常与鲁棒 | [tests/test_robust.py](tests/test_robust.py) | 4 | 路径不存在（404）、方法不支持、请求超时、单位元数据 |
| 参数化 | [tests/test_multi_city.py](tests/test_multi_city.py) | 3 | 用 `@pytest.mark.parametrize` 一条代码覆盖多组经纬度 |

## 快速开始

```bash
pip install -r requirements.txt
pytest
```

运行结束后打开 `reports/report.html` 查看 HTML 测试报告。

## 项目结构

```
api-auto-test/
├── config.py              # 接口地址、超时、重试配置
├── conftest.py            # pytest fixture（公共参数）
├── pytest.ini             # pytest 配置
├── utils/
│   └── api_client.py      # 请求封装 + 负向断言封装
├── tests/                 # 24 条用例
└── .github/workflows/     # CI：每次提交自动跑测试
```

## 项目设计要点

1. **断言用容差而非相等**：接口会把经纬度吸附到网格点（请求 `52.52` 返回 `52.512604`），因此用 `abs(差值) < 1` 判断，避免误报。
2. **负向用例统一封装**：所有错误场景统一断言「状态码 + `error:true` + `reason` 非空」，不写死错误文案，避免接口文案微调导致用例失效。
3. **网络抖动自动重试**：对连接失败与超时最多重试 3 次；`4xx / 5xx` 属于接口正常响应，**不重试**。
4. **报告与 CI 归档**：`pytest-html` 输出单文件报告，GitHub Actions 在每次 push 与每天定时执行，报告作为 artifact 归档。
