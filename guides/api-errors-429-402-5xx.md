# EastX API 报错排查：429、402、403 与 5xx | API Error Troubleshooting

[官网原文 / Canonical guide](https://eastx.ai/zh/community/api-errors-429-402-5xx)

## 中文

### 先看错误类型，再决定是否重试

API 中转站报错时，反复点击“重试”通常不能解决余额不足、模型权限或地址配置问题。EastX 返回的 HTTP 状态码与错误类型可以帮助你把问题分到配置、账户、限流和上游四类。先记录发生时间、模型 ID、状态码、错误类型和请求标识，再处理对应原因。

### 402：余额不足与 Key 额度是两回事

`insufficient_balance` 表示余额预检查未通过；`cap_reached` 则应检查密钥消费上限。不要只看账户余额。请求的最大输出长度越大，预检查所需余额可能越高；支持多个可用通道时，检查还会覆盖符合条件的备用通道。降低不必要的最大输出、补足余额或调整该 Key 额度后再试。实际结算仍需看用量记录，预估不是最终扣费。

### 429：控制并发，而不是叠加重试

区分单 Key 限流与 `tenant_rate_limit_exceeded`。客户端、SDK 和任务队列同时重试，会放大请求量。选择一层统一重试，遵循服务端提供的 Retry-After，设置最大次数和总等待上限，并加入随机退避。为批量任务建立队列，比同时启动几十个客户端更易控制。

### 401、403、404：先修配置

- 401：确认使用 EastX API Key，复制完整且未撤销。
- 403：检查 Key 是否启用、到期、允许调用该模型，以及当前出口 IP 是否在白名单内。
- 404：核对完整模型 ID 和接口路径。Base URL 通常填 `https://api.eastx.ai/v1`，不要重复拼接 `/v1` 或 `/chat/completions`。

### 502、503、504 与网络超时

502 对应上游异常；503 时应检查模型服务状态与可用通道；504 和客户端超时需结合具体接口判断。文本响应丢失不等于请求未执行。视频任务已有 ID 时继续查询原任务，尤其不要在 `pending_confirmation` 状态下反复创建任务。

### 把排错变成可管理的流程

EastX 的按 Key 额度、RPM 和模型权限设置，适合为 WorkBuddy、编程助手、测试环境分别建立 Key。这样发现异常时能暂停对应入口，并在统一用量中定位问题。提交支持请求时提供脱敏的错误信息，不要发送完整 API Key。

**什么时候换模型？** 配置与额度确认无误、原模型上游不可用，且备用模型满足任务的工具调用、上下文和输出格式要求时。更换模型后应重新检查任务结果。

**第一步该做什么？** 先跑[最小 SDK 请求](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart)，将客户端配置问题与 API 问题分开。

---

## English

### Read the error type before retrying

Repeated retries cannot fix a missing balance, denied model or incorrect endpoint. EastX HTTP status codes and error types help separate configuration, account, rate-limit and upstream problems. Record the time, model ID, status, error type and request identifier before changing anything.

### 402: balance and key caps are separate

For `insufficient_balance`, check the balance precheck. For `cap_reached`, inspect the key spending cap. A large maximum output can increase the required reserve, and eligible fallback routes can affect the precheck. Reduce unnecessary output limits, fund the account or adjust the key cap, then retry. The estimate is not the final charge; reconcile against usage records.

### 429: control concurrency instead of stacking retries

Distinguish a key limit from `tenant_rate_limit_exceeded`. Retries in the client, SDK and job queue can multiply traffic. Pick one retry layer, follow Retry-After when supplied, set attempt and total-wait limits, and use randomized backoff. A queue makes batch work easier to control than many clients firing simultaneously.

### 401, 403 and 404: fix configuration first

- 401: use a complete, active EastX key.
- 403: check whether the key is enabled, expired, allowed to call the model and permitted from the current egress IP.
- 404: verify the exact model ID and endpoint. A base URL is normally `https://api.eastx.ai/v1`; avoid duplicating `/v1` or `/chat/completions`.

### 502, 503, 504 and network timeouts

502 indicates an upstream error. With 503, inspect model service status and available routes. Interpret 504 and client timeouts in the context of the endpoint. A lost response does not prove the request never ran. When a video task already has an ID, query that task; do not repeatedly create tasks in `pending_confirmation`.

### Make troubleshooting manageable

EastX key-level caps, RPM and model permissions let you separate WorkBuddy, coding tools and test environments. You can pause the affected entry point and inspect usage in one place. Send redacted error details to support, never a complete API key.

**When should I switch models?** When configuration and limits are correct, the original upstream is unavailable, and the alternative supports the required tools, context and output format. Recheck the task result after switching.

**Where should I start?** Run the [minimal SDK request](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart) to separate client configuration problems from API problems.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)

### 继续阅读 / Related guides

- [使用 OpenAI SDK 接入 EastX：首次调用与常见错误 | OpenAI SDK Quickstart](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart)
- [EastX 路由与故障转移：价格、速度、可靠性怎么选 | Routing and Failover](https://eastx.ai/zh/community/routing-failover-price-speed-reliability)
