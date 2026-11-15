# Cline 接入 EastX：OpenAI Compatible、工具调用与成本控制 | Cline Setup

[官网原文 / Canonical guide](https://eastx.ai/zh/community/cline-eastx-openai-compatible)

## 中文

### 从“能回答”到“能完成代码任务”

Cline 的价值在于围绕项目使用工具完成工作。接入 EastX 时，除了地址和密钥，还要选择适合工具调用的模型，核对上下文与输出限制。EastX 的统一入口与专用 Key 额度，适合把编程 Agent 与其他客户端的消费分开管理。

### 配置 OpenAI Compatible

打开 Cline 设置，API Provider 选择 OpenAI Compatible。Base URL 填 `https://api.eastx.ai/v1`，API Key 填为 Cline 创建的 EastX Key，Model ID 填目录中的精确值。高级配置中的上下文、最大输出与图片支持应按该模型实际能力填写。

### 用小仓库完成首次验证

先让 Cline 阅读一个函数并解释，再提出一项明确修改，最后运行已有测试。检查它实际改了哪些文件、工具是否成功、测试是否通过。不要一开始就让新模型大范围重构。

### 三个最常见的成本来源

较长的项目上下文、Agent 多轮工具交互，以及失败后的重复尝试。用 EastX 专用 Key 设置消费上限；在 Cline 中给任务明确边界，避免把整个仓库与无关历史反复带入。比较模型时统计完成一个任务的总费用和人工修正，而不只看单轮价格。

### 常见问题

**401/404**：核对服务商选项、Base URL 与模型 ID。**工具不执行**：检查模型工具能力和客户端配置。**402**：检查账户余额、Key 上限及最大输出。**429**：降低并发，避免客户端与外围脚本同时重试。

EastX 帮助你在同一接入与账单体系下比较不同编程模型；Cline 负责具体项目工具与交互。将两者的职责分开，排查会更直接。进一步阅读[API 错误排查](https://eastx.ai/zh/community/api-errors-429-402-5xx)。

---

## English

### Move from answering to completing coding tasks

Cline uses project tools to get work done. Connecting EastX requires an appropriate tool-capable model as well as a URL and key. Check context and output limits. A unified entry point and dedicated key cap help separate coding-agent spending from other clients.

### Configure OpenAI Compatible

In Cline settings, choose OpenAI Compatible as API Provider. Enter `https://api.eastx.ai/v1`, a dedicated EastX key and the exact catalog model ID. Set context, maximum output and image support to match the model's real capabilities.

### Validate with a small repository

Ask Cline to read and explain a function, make one clearly defined change, and run existing tests. Inspect changed files, tool execution and test results. Avoid starting with a broad refactor on a new model.

### Three common cost drivers

Large project context, multi-turn tool interaction and repeated failed attempts. Set a dedicated EastX key cap and give Cline a bounded task. Avoid repeatedly including the whole repository and irrelevant history. Compare total completed-task cost and manual corrections rather than one-turn prices.

### Common issues

For **401/404**, check provider type, base URL and ID. For missing tool execution, check model and client capabilities. For **402**, inspect balance, key cap and maximum output. For **429**, reduce concurrency and avoid retries in both client and wrapper scripts.

EastX supports model comparison within one integration and billing system; Cline handles project tools and interaction. Keeping those roles clear makes troubleshooting easier. See the [API error guide](https://eastx.ai/zh/community/api-errors-429-402-5xx).

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [Cline OpenAI Compatible](https://github.com/cline/cline/blob/main/docs/provider-config/openai-compatible.mdx)
- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)

### 继续阅读 / Related guides

- [ZCode 接入 EastX：桌面端与 CLI 配置、模型切换和预算 | ZCode Setup](https://eastx.ai/zh/community/zcode-eastx-setup)
- [EastX API 报错排查：429、402、403 与 5xx | API Error Troubleshooting](https://eastx.ai/zh/community/api-errors-429-402-5xx)
