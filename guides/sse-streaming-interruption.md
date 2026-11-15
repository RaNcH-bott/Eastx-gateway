# SSE 流式输出怎么接：首 Token、结束信号与中断处理 | Streaming Guide

[官网原文 / Canonical guide](https://eastx.ai/zh/community/sse-streaming-interruption)

## 中文

### 流式输出解决的是等待体验

SSE 让应用在生成过程中逐步显示文本。它改善用户等待时的反馈，但首 Token 时间与完整响应时间是两个指标。测试时分别记录请求发出、首个可见文本和结束时间，不能用一个数字代表全部体验。

### Python 最小示例

使用已配置的 `EASTX_API_KEY` 和支持流式文本的 `EASTX_MODEL`：

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["EASTX_API_KEY"],
    base_url="https://api.eastx.ai/v1",
    max_retries=0,
    timeout=60.0,
)
stream = client.chat.completions.create(
    model=os.environ["EASTX_MODEL"],
    messages=[{"role": "user", "content": "Explain SSE briefly."}],
    stream=True,
)
try:
    for chunk in stream:
        if not chunk.choices:
            continue
        text = chunk.choices[0].delta.content
        if text:
            print(text, end="", flush=True)
finally:
    stream.close()
```

SDK 会处理 SSE 帧。自行解析 HTTP 时，应按事件边界消费 `data:`，不能假定每个网络包都是完整 JSON。Chat Completions 的文本增量在 `choices[0].delta.content`，空增量不应显示成 `None`。结束标记与 `finish_reason` 也应记录。

### 中断后不要悄悄重放整次任务

已经显示部分文本后发生超时，应在界面标明“输出中断”，保留已收到内容，由用户或应用策略决定是否重新生成。重新发请求可能产生新的输出与费用。Agent 涉及文件或外部工具时，还要检查工具是否已执行，避免重复动作。

### EastX 的接入优势

统一的兼容入口可以复用 SDK 流式代码；更换支持该能力的模型时，应用不必重写整套文本显示逻辑。配合分 Key 用量核对，可以比较不同模型的首 Token、完成时间与整项任务成本。

反向代理或自建客户端若出现“最后一次性输出”，检查响应缓冲、读取方式和超时设置。Messages 与 Responses 使用不同事件结构，不能把 Chat Completions 的解析器直接照搬到所有接口。

---

## English

### Streaming improves feedback while users wait

SSE lets an application display text during generation. Time to first token and total response time remain different metrics. Record request start, first visible text and completion separately.

### Minimal Python example

Configure `EASTX_API_KEY` and an `EASTX_MODEL` supporting streamed text:

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["EASTX_API_KEY"],
    base_url="https://api.eastx.ai/v1",
    max_retries=0,
    timeout=60.0,
)
stream = client.chat.completions.create(
    model=os.environ["EASTX_MODEL"],
    messages=[{"role": "user", "content": "Explain SSE briefly."}],
    stream=True,
)
try:
    for chunk in stream:
        if not chunk.choices:
            continue
        text = chunk.choices[0].delta.content
        if text:
            print(text, end="", flush=True)
finally:
    stream.close()
```

The SDK handles SSE framing. If parsing HTTP yourself, consume `data:` at event boundaries; a network packet is not necessarily a complete JSON object. Chat Completions text is in `choices[0].delta.content`. Do not render empty deltas as `None`. Track completion markers and `finish_reason`.

### Do not silently replay an interrupted task

If a timeout occurs after partial output, show an interrupted state and retain received text. Let the user or application policy decide whether to regenerate. Another request can produce different output and additional charges. For agents, inspect whether file or external-tool actions already occurred before retrying.

### Where EastX helps

A compatible entry point lets you reuse SDK streaming code across models supporting the capability. Separate keys and usage records help compare first-token time, completion time and whole-task cost.

If a proxy or custom client displays everything at the end, inspect buffering, consumption and timeout settings. Messages and Responses use different event structures; a Chat Completions parser is not universal.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)

### 继续阅读 / Related guides

- [EastX API 报错排查：429、402、403 与 5xx | API Error Troubleshooting](https://eastx.ai/zh/community/api-errors-429-402-5xx)
- [EastX 路由与故障转移：价格、速度、可靠性怎么选 | Routing and Failover](https://eastx.ai/zh/community/routing-failover-price-speed-reliability)
