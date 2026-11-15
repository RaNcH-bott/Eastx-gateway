# 大模型 API 费用怎么算：输入、输出、缓存与阶梯计费 | Understanding API Costs

[官网原文 / Canonical guide](https://eastx.ai/zh/community/api-pricing-input-output-cache-tiers)

## 中文

### 先统一单位：每百万 Token，不是每次对话

比较模型价格时，先确认币种、计费单位、输入与输出价格。若价格按每百万 Token 标示，基础公式为：输入 Token ÷ 1,000,000 × 输入单价，加上输出 Token ÷ 1,000,000 × 输出单价。图片、视频等可能采用其他计费方式，不应套用文本公式。

### 缓存命中怎么计费

当上游报告缓存命中时，应把命中的输入与普通输入分开计算：未命中输入 × 普通输入价，命中输入 × 缓存命中价，再加输出费用，最后按计费单位换算。重复发送相同文字并不自动证明命中；看返回用量和账单记录。

### 为什么页面最低价不是每次请求的价格

部分模型存在阶梯价，与输入长度、推理模式或其他适用条件有关。EastX 价格页的 Tiered 标记可以展开查看各档。比较长文档或 Agent 任务时，应使用任务实际所在档位，而不是只取最低档。推理用量也可能计入输出，回答字数不能完整代表费用。

### 余额预检查与最终结算

请求发送前，平台会评估输入与最大输出的费用；可用备用通道也可能影响预留要求。因此，余额看似够支付一条短回答，仍可能因为较大的最大输出设置返回 402。把最大输出设为任务真正需要的范围，并查看 Key 消费上限。最终核对使用实际用量、成功通道和适用档位。

### Agent 预算要看整项任务

WorkBuddy、ZCode 或其他 Agent 可能多次读取上下文、调用工具、再请求模型。应记录整项任务的总输入、总输出、重试和人工修正，而不是只看最后一轮。EastX 的分 Key 额度和 RPM 适合把不同客户端分开管理；统一用量记录则方便比较模型和任务配置。

### 实用核对清单

先核对模型 ID、价格单位和档位；再核对普通输入、缓存输入与输出；最后对照请求时间、请求标识和控制台消费。发现差异时，把这些信息一起提交支持团队，比仅发送余额截图更易定位。

**如何降低费用？** 缩短无关上下文、限制不必要的输出、为重复前缀观察缓存效果、按任务选择合适模型，并对 Agent 设置预算。先降低无效调用，再比较单价。

---

## English

### Start with the unit: per million tokens, not per conversation

Check currency, billing units and separate input/output prices. When rates are per million tokens, the basic calculation is input tokens divided by 1,000,000 times the input rate, plus output tokens divided by 1,000,000 times the output rate. Image and video endpoints may use different units.

### Account for cache hits separately

When the upstream reports a cache hit, split ordinary input from cached input. Multiply each by its applicable rate, add output cost and convert using the billing unit. Repeating text alone does not prove a cache hit; inspect usage and billing records.

### The lowest listed rate is not every request's rate

Some models use tiers based on input length, reasoning mode or other applicable conditions. Expand the Tiered badge on EastX pricing. Long-document and agent comparisons should use the tier actually reached. Reasoning usage may count as output, so visible answer length is not the complete bill.

### Balance prechecks versus final settlement

Before forwarding a request, the platform estimates input and maximum output cost. Eligible fallback routes may affect the required reserve. A balance sufficient for a short answer can therefore still produce 402 with a large output limit. Set realistic maximum output and check the key cap. Reconcile the final charge against actual usage, the successful route and the applicable tier.

### Budget for the entire agent task

WorkBuddy, ZCode and other agents may read context, use tools and call the model repeatedly. Measure total input, output, retries and manual corrections across the task. EastX key-level caps and RPM separate clients, while centralized usage makes model and configuration comparisons easier.

### A practical reconciliation order

Check model ID, unit and tier first, then ordinary input, cached input and output. Match the request time and identifier to the console record. Give support these details instead of only a balance screenshot.

**How can I reduce cost?** Remove irrelevant context, limit unnecessary output, observe cache behavior for repeated prefixes, choose a model suited to the task and cap agent budgets. Eliminate wasted calls before comparing unit rates.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)
- [模型与定价 / Models and pricing](https://eastx.ai/en/pricing)

### 继续阅读 / Related guides

- [EastX USDT 充值教程：网络、金额、TxID 与到账排查 | USDT Top-up Guide](https://eastx.ai/zh/community/usdt-topup-troubleshooting)
- [EastX 路由与故障转移：价格、速度、可靠性怎么选 | Routing and Failover](https://eastx.ai/zh/community/routing-failover-price-speed-reliability)
