# Open WebUI 接入 EastX：统一多模型连接与团队使用 | Open WebUI Setup

[官网原文 / Canonical guide](https://eastx.ai/zh/community/open-webui-eastx-setup)

## 中文

### 为自建界面提供统一模型入口

Open WebUI 适合希望使用自建聊天界面的团队。EastX 提供模型 API 与用量管理，Open WebUI 提供会话界面。把两者结合，可以保留自己的交互入口，同时减少多个模型供应商的重复连接配置。

### 添加连接

在管理员设置的 Connections 中新增 OpenAI 兼容连接，填写 `https://api.eastx.ai/v1` 和为该部署创建的 EastX API Key，保存并加载模型。核对模型 ID，在新会话选择目标模型，先进行短文本测试。

如果手动限制模型列表，应确保填入真实可调用 ID。多个连接返回相同模型 ID 时容易混淆，使用清楚的连接名称与客户端支持的模型前缀管理方式，确认实际调用来源。

### 自建部署最容易忽略的检查

管理员连接通常由 Open WebUI 服务端发请求。若部署在 Docker 或远程服务器上，测试的应是该服务的 DNS、网络出口和代理，而不是只看自己电脑浏览器能否打开官网。配置 IP 白名单时也应使用实际请求出口。

### 用量与权限怎么分工

EastX Key 用于限制该部署的模型、额度和请求频率；Open WebUI 内部用户的权限与会话管理由你部署的应用负责。一把共享 Key 的消费不能自动区分每位内部用户，团队需要结合应用自身记录核对。对开发、演示和生产部署分别建 Key，更容易控制预算。

### 从基础聊天逐步扩展

先验证文本，再测试流式、图片或工具。不要直接开启有状态 Responses 功能并假设上游会保存会话；EastX 文档列明其 Responses 兼容入口对存储状态与部分字段有明确限制。先用 Chat Completions 路径完成常用流程。

EastX 的优势是把多模型连接、预算与调用记录集中到一处；自建 Open WebUI 则让团队保留自己的使用界面。出现错误时，先对照[排错指南](https://eastx.ai/zh/community/api-errors-429-402-5xx)区分网络、权限与额度。

---

## English

### One model entry point for a self-hosted interface

Open WebUI gives teams a self-hosted chat interface; EastX provides model APIs and usage management. Together, they preserve your interaction layer while reducing repeated provider connections.

### Add the connection

In administrator Connections settings, add an OpenAI-compatible connection with `https://api.eastx.ai/v1` and an EastX key dedicated to the deployment. Save, load models, verify IDs and select a model in a new conversation for a short text test.

If manually restricting the model list, use callable IDs. Identical IDs across connections can be confusing; use clear connection names and supported model-prefix controls, then confirm the actual provider being called.

### Check the deployment's network

Administrator connections generally send requests from the Open WebUI server. For Docker or remote deployments, test that service's DNS, egress and proxy, not only whether your laptop can open the website. IP allowlists must match the real request egress.

### Separate usage and permission responsibilities

An EastX key controls the deployment's models, cap and request rate. Internal user and conversation permissions belong to your application. One shared key does not automatically attribute consumption to each internal user; combine application records with gateway usage. Use separate keys for development, demos and production.

### Expand beyond chat gradually

Test text, then streaming, images or tools. Do not assume stateful Responses features will work: EastX documents restrictions on stored state and some fields in its Responses-compatible endpoint. Start common workflows with Chat Completions.

EastX centralizes model connections, budgets and request usage, while Open WebUI preserves your team's interface. Use the [error guide](https://eastx.ai/zh/community/api-errors-429-402-5xx) to distinguish network, permission and quota problems.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [Open WebUI compatible providers](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible/)
- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)

### 继续阅读 / Related guides

- [EastX 路由与故障转移：价格、速度、可靠性怎么选 | Routing and Failover](https://eastx.ai/zh/community/routing-failover-price-speed-reliability)
- [EastX 可靠性与数据处理 FAQ：Key、日志、上游与任务恢复 | Reliability FAQ](https://eastx.ai/zh/community/api-reliability-data-handling-faq)
