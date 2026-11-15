# WorkBuddy 接入 EastX：自定义模型、API 地址与费用管理 | WorkBuddy Setup

[官网原文 / Canonical guide](https://eastx.ai/zh/community/workbuddy-eastx-custom-model)

## 中文

### WorkBuddy 为什么接入 EastX？

当办公 Agent 需要换模型、比较处理效果或控制多轮任务费用时，统一 API 入口比反复切换账户更便于管理。EastX 可以为 WorkBuddy 单独分配 Key 和消费上限，与 ZCode、SDK 项目分别核对用量，同时共享账户内的模型与余额管理。

### 在模型设置中添加自定义服务

WorkBuddy 当前官方文档提供图形化自定义模型管理。在设置页的模型管理中选择自定义服务，填写服务地址、API Key 和模型名称。为 EastX 使用专用 Key，模型 ID 从 EastX 当前目录复制。

标准 Chat Completions 接入的 Base URL 为 `https://api.eastx.ai/v1`。WorkBuddy 的默认模式会校验并补全聊天路径；如果启用了“自定义协议”，它会直接使用所填地址，此时应提供完整请求地址 `https://api.eastx.ai/v1/chat/completions`。两种模式不要混用，否则容易出现重复路径或 404。

### 保存后，明确选择刚添加的模型

回到会话选择对应自定义模型，再运行一个小任务，例如“读取这份简短资料，输出三条结论和待办”。之后检查结果以及 EastX 用量。涉及文件或工具的任务，再确认模型具备工具能力、客户端实际执行了工具，而不是只生成一段说明。

### 按办公任务配置模型与预算

资料摘要先比较完成成本；多步骤办公任务优先检查工具执行和结果准确性；图片理解选支持视觉输入的模型。不要因为客户端显示某个能力开关，就给不支持该能力的模型启用它。为 WorkBuddy 设置独立额度，有助于控制多轮尝试与重试产生的费用。

### 三个高频问题

**404 或 Invalid URL**：检查自定义协议开关与 URL 形式是否匹配，尤其是重复的 `/chat/completions`。

**配置保存了但没有走 EastX**：确认会话实际选中的是新建模型，而不是其他默认或自动模式；再看 EastX 对应 Key 的用量。

**聊天成功但任务没完成**：检查工具调用、文件权限与模型能力，再用小任务定位。换模型时保留同一份任务样本，比较最终成果和总费用。

EastX 在这里的优势是统一模型入口、专用 Key 预算和集中用量，帮助你把“能聊”推进到“可管理地完成工作”。

---

## English

### Why connect WorkBuddy to EastX?

Office agents benefit from a consistent API entry point when comparing models and controlling multi-turn costs. Give WorkBuddy its own EastX key and cap, separate its usage from ZCode or SDK projects, and manage models and balance in one account.

### Add a custom service in model settings

WorkBuddy's current official guide supports graphical custom-model management. In model settings, choose a custom service and enter its URL, key and model name. Use a dedicated EastX key and an exact ID from the current catalog.

For standard Chat Completions, the base URL is `https://api.eastx.ai/v1`. WorkBuddy's default mode validates and completes the chat path. When Custom Protocol is enabled, it sends directly to the supplied address; use the full endpoint `https://api.eastx.ai/v1/chat/completions`. Mixing the two modes can duplicate the path and cause 404.

### Explicitly select the saved model

Return to the conversation and select your new custom model. Start with a short document and ask for three conclusions and action items. Inspect the result and EastX usage. For file or tool workflows, also verify model tool support and actual execution, not just a textual description.

### Match models and budgets to office work

Compare completion cost for summaries, tool execution and accuracy for multi-step work, and vision support for images. A client capability switch does not add a capability the model lacks. A dedicated WorkBuddy cap helps control repeated agent turns and retries.

### Three common problems

**404 or Invalid URL:** match Custom Protocol mode to the URL format and remove duplicated `/chat/completions`.

**Saved but not using EastX:** check the model selected in the conversation instead of assuming the default or automatic mode uses it. Confirm usage on the dedicated key.

**Chat works but the task fails:** inspect tools, file permissions and model capabilities with a small task. Keep the task sample fixed when comparing final output and total cost across models.

EastX combines one model entry point, dedicated-key budgets and centralized usage so WorkBuddy workflows are easier to manage beyond the first chat response.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [WorkBuddy 模型设置 / Model settings](https://www.workbuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Model)
- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)

### 继续阅读 / Related guides

- [EastX API 报错排查：429、402、403 与 5xx | API Error Troubleshooting](https://eastx.ai/zh/community/api-errors-429-402-5xx)
- [大模型 API 费用怎么算：输入、输出、缓存与阶梯计费 | Understanding API Costs](https://eastx.ai/zh/community/api-pricing-input-output-cache-tiers)
