# Cherry Studio 接入 EastX：自定义服务商与多模型对比 | Cherry Studio Setup

[官网原文 / Canonical guide](https://eastx.ai/zh/community/cherry-studio-eastx-setup)

## 中文

### 适合桌面多模型工作流的统一入口

Cherry Studio 适合在桌面管理多个模型与对话。接入 EastX 后，可以把 API Key、余额和用量集中到同一平台，再在客户端按任务切换模型。对于经常比较中文写作、总结、代码解释的用户，重点是减少重复配置，并看清每个任务的实际用量。

### 配置步骤

在 Cherry Studio 的模型服务设置中添加自定义提供商，连接格式选择 OpenAI 兼容。名称可写 EastX，API 地址填写 `https://api.eastx.ai/v1`，Key 填 EastX 专用密钥。添加或获取模型列表后，核对模型 ID，再在对话中选中所需模型。

客户端版本对地址字段的自动补全可能不同。连接检查出现 404 时，先确认最终请求应该到达 `/v1/chat/completions`，不要把完整端点与会追加路径的 Base URL 字段混用。先用普通文本验证，再启用图片、工具或其他高级能力。

### 用相同任务做多模型比较

准备一份固定资料和同一条要求，例如“提取结论、证据、待办，保留日期与金额”。记录遗漏信息、输出可用性、等待时间和 EastX 用量。模型能否省去一次人工重写，往往比单次回答长度更值得关注。

### EastX 的优势怎么用到桌面端？

为 Cherry Studio 创建单独 Key，可以与编程或批量任务分开设额度；统一余额便于切换模型时继续使用同一消费体系；集中用量有助于复盘长对话或重复生成的成本。更换模型时仍核对具体能力与价格档位。

### 常见问题

模型不显示时检查服务是否启用、模型 ID 与 Key 权限；能显示但请求失败时检查余额和错误类型。长对话费用增加时，清理无关历史或新开针对性会话。图片理解需要视觉模型，不能靠客户端打开图片按钮来补齐。

先用[最小 SDK 请求](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart)确认 API，再排查客户端配置，可以明显缩短定位路径。

---

## English

### One entry point for desktop multi-model work

Cherry Studio organizes models and conversations on the desktop. With EastX, keys, balance and usage stay together while you choose models in the client. This reduces repeated setup for writing, summarization and code explanation, and makes task usage easier to review.

### Setup

Add a custom provider in Cherry Studio model-service settings and choose an OpenAI-compatible format. Name it EastX, enter `https://api.eastx.ai/v1` and your dedicated EastX key. Add or retrieve models, verify exact IDs and select the model in a conversation.

Address completion can vary by client version. For 404, check that the final request should reach `/v1/chat/completions`; do not put a full endpoint into a base-URL field that appends the path again. Test plain text before enabling images, tools or advanced features.

### Compare models on the same task

Use one document and an identical instruction, such as extracting conclusions, evidence and actions while preserving dates and amounts. Record omissions, usability, waiting time and EastX usage. Avoiding a manual rewrite can matter more than answer length.

### Put EastX's management features to work

A dedicated Cherry Studio key separates desktop budgets from coding or batch jobs. One balance supports model switching, and centralized usage helps explain long-conversation or regeneration costs. Recheck model capabilities and pricing tiers when switching.

### Common issues

For missing models, inspect provider enablement, IDs and key permissions. For request failures, inspect balance and error type. Reduce irrelevant history when long conversations become costly. Image understanding requires a vision model; a client button cannot add that capability.

Use the [minimal SDK request](https://eastx.ai/zh/community/openai-sdk-eastx-quickstart) to confirm the API before investigating client settings.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [Cherry Studio 自定义服务商 / Custom providers](https://www.cherryai.com/docs/en/pre-basic/providers/zi-ding-yi-fu-wu-shang/)
- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)

### 继续阅读 / Related guides

- [Qwen、Kimi、GLM 怎么选：办公、编程与长文档任务 | Model Selection](https://eastx.ai/zh/community/qwen-kimi-glm-model-selection)
- [大模型 API 费用怎么算：输入、输出、缓存与阶梯计费 | Understanding API Costs](https://eastx.ai/zh/community/api-pricing-input-output-cache-tiers)
