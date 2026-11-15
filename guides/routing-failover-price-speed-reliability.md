# EastX 路由与故障转移：价格、速度、可靠性怎么选 | Routing and Failover

[官网原文 / Canonical guide](https://eastx.ai/zh/community/routing-failover-price-speed-reliability)

## 中文

### 路由优先级解决什么问题？

同一个模型可能有多个符合条件的上游通道。EastX 路由设置用于安排这些通道的优先顺序，让批量任务、实时交互和稳定性要求不同的业务采用不同偏好。

### 五种配置

- `default`：保留平台默认顺序并追加备用报价。
- `auto`：使用自动策略。
- `price`：按请求预估费用排序，适合可容忍等待的批量任务。
- `speed`：以历史速度信息排序，适合关注交互等待的任务。
- `success_rate`：以历史可靠性信息排序，适合重视成功完成的流程。

速度和可靠性使用租户最近 24 小时的数据，历史不足时采用保守估计。因此应该把设置理解为选择偏好，再通过自己的任务记录评估效果。

### 在 Key 上设置，也可以按请求覆盖

先在 API Key 设置中选默认偏好。单次请求可使用 `routing_priority` 覆盖。优先级依次为 `routing_priority`、`provider.sort`、`x-eastx-routing` 请求头、Key 设置。文档列明支持 Chat Completions 与 Messages。

```json
{
  "model": "YOUR_MODEL_ID",
  "routing_priority": "price",
  "messages": [{"role": "user", "content": "Summarize this note."}]
}
```

### 故障转移与换模型不同

同模型通道切换不等于自动换成另一个模型。如果应用要从一个模型系列切到另一个，需要自己检查工具能力、输出结构和任务质量。流式响应已经输出或外部动作已经执行时，也不能把整次请求当成从未发生。

模型目录提供 `service_status`。没有可用通道时可能返回 503；自动暂停的上游在冷却后可由下一次真实请求尝试恢复。不要为此高频发送空探测。

### 费用要同时看预检查与结算

价格目录展示的费率与最终成功通道、阶梯有关；余额检查覆盖符合条件的最贵备用通道。设置价格优先不代表可以把余额压到只够最低报价。用请求记录核对最终费用。

EastX 的实际价值是让路由偏好与 Key 管理结合：交互客户端和批量脚本可以分别设定，而用量仍在统一平台核对。上线前用同一任务比较完成率、首 Token、总耗时和费用。

---

## English

### What does routing priority solve?

A model may have multiple eligible upstream routes. EastX routing preferences order those routes so batch jobs, interactive clients and reliability-focused workflows can use different priorities.

### Five settings

- `default`: retain platform order and append fallback offers.
- `auto`: use the automatic strategy.
- `price`: rank estimated request cost, useful for batch jobs that tolerate waiting.
- `speed`: rank historical speed, useful for interactive work.
- `success_rate`: rank historical reliability, useful for completion-focused workflows.

Speed and reliability use the tenant's last 24 hours, with conservative estimates when history is missing. Treat them as preferences and evaluate results on your workload.

### Set a key default or override a request

Choose a preference in API key settings. A request can override it with `routing_priority`. Precedence is `routing_priority`, `provider.sort`, the `x-eastx-routing` header, then key settings. The documented endpoints are Chat Completions and Messages.

```json
{
  "model": "YOUR_MODEL_ID",
  "routing_priority": "price",
  "messages": [{"role": "user", "content": "Summarize this note."}]
}
```

### Failover is different from switching models

Changing routes for one model does not mean automatically replacing it with another model. Cross-model fallback requires application checks for tools, output structure and quality. Once streaming output or external actions begin, the request cannot simply be treated as if it never happened.

The catalog exposes `service_status`. No available route can result in 503. Automatically paused upstreams can attempt recovery on a real request after cooldown; avoid high-frequency empty probes.

### Check both reserves and settlement

Final charges depend on the successful route and applicable tier. Balance checks cover the most expensive eligible fallback. Price priority does not mean a balance sufficient only for the lowest offer will pass. Reconcile the final request record.

EastX combines routing preferences with key management: interactive clients and batch scripts can use separate settings while usage stays centralized. Compare completion rate, first-token time, total time and cost before deployment.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)

### 继续阅读 / Related guides

- [EastX API 报错排查：429、402、403 与 5xx | API Error Troubleshooting](https://eastx.ai/zh/community/api-errors-429-402-5xx)
- [EastX 可靠性与数据处理 FAQ：Key、日志、上游与任务恢复 | Reliability FAQ](https://eastx.ai/zh/community/api-reliability-data-handling-faq)
