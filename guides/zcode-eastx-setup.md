# ZCode 接入 EastX：桌面端与 CLI 配置、模型切换和预算 | ZCode Setup

[官网原文 / Canonical guide](https://eastx.ai/zh/community/zcode-eastx-setup)

## 中文

### 把编程客户端接到统一模型入口

ZCode 接入 EastX 后，可以围绕不同编程任务选择模型，同时在 EastX 集中管理 Key、额度与用量。适合已经使用 ZCode，但不想为每个模型维护一套独立接入信息的开发者。

### 桌面端设置

打开 Model Settings，添加提供商，API 格式选择 Chat Completions。Base URL 填 `https://api.eastx.ai/v1`，API Key 填专门为 ZCode 创建的 EastX Key。随后从 EastX 模型目录或 `GET /v1/models` 复制模型 ID，添加到客户端。不要省略 `/v1`，也不要在 Base URL 后再拼接完整的聊天路径。

保存后，在当前会话明确选中刚配置的模型。先让模型解释一个小函数，再让它提出修改，最后检查文件修改与测试结果。能聊天只是第一步，真正的编程任务还需验证工具调用和多轮上下文。

### CLI 配置结构

EastX 文档给出的 Windows 配置位置是 `%USERPROFILE%\.zcode\cli\config.json`，macOS/Linux 为 `~/.zcode/cli/config.json`。保留现有其他配置，合并 provider 和 model 字段。下面的模型占位符需要替换：

```json
{
  "provider": {
    "eastx": {
      "kind": "openai-compatible",
      "name": "EastX",
      "options": {
        "baseURL": "https://api.eastx.ai/v1",
        "apiKey": "YOUR_EASTX_API_KEY",
        "apiKeyRequired": true,
        "includeUsage": true
      },
      "models": {
        "YOUR_MODEL_ID": {"name": "My coding model"}
      }
    }
  },
  "model": {
    "main": "eastx/YOUR_MODEL_ID",
    "lite": "eastx/YOUR_MODEL_ID"
  }
}
```

### 主模型与轻量任务分开选择

先用同一可用模型跑通 main 与 lite，再按代码质量、完成时间和整项任务费用分工。复杂修改优先满足工具能力与准确性；简单总结再比较低成本模型。用 ZCode 专用 Key 设置消费上限，避免实验任务影响其他客户端。

### 常见问题

**404**：检查 `/v1` 和精确模型 ID。**403**：检查 Key 的模型权限与来源 IP。**402**：同时检查余额和 Key 额度。配置推理等级时，ZCode 可能使用 `/v1/messages`；EastX 文档说明该兼容入口会做协议转换，`thinking` 参数不直接转发，推理由上游决定。不要用 UI 上的推理开关推断每个模型完全相同的行为。

EastX 的优势在于接入与费用管理统一，而模型选择仍围绕实际代码任务。遇到错误可按[排错指南](https://eastx.ai/zh/community/api-errors-429-402-5xx)定位。

---

## English

### Connect your coding client to one model entry point

EastX lets ZCode users choose models for different coding jobs while managing keys, caps and usage together. It is useful when you want fewer separate provider configurations.

### Desktop setup

In Model Settings, add a provider and choose Chat Completions. Set the base URL to `https://api.eastx.ai/v1` and enter an EastX key dedicated to ZCode. Add exact model IDs from the EastX catalog or `GET /v1/models`. Keep `/v1`, and do not append the full chat endpoint to the base URL.

Select the configured model in the conversation. Start with explaining a small function, then request a change and inspect the edits and tests. A chat reply is only the first check; coding workflows also require tools and multi-turn context.

### CLI configuration

EastX documents `%USERPROFILE%\.zcode\cli\config.json` on Windows and `~/.zcode/cli/config.json` on macOS/Linux. Merge these provider and model fields with existing settings. Replace the placeholders:

```json
{
  "provider": {
    "eastx": {
      "kind": "openai-compatible",
      "name": "EastX",
      "options": {
        "baseURL": "https://api.eastx.ai/v1",
        "apiKey": "YOUR_EASTX_API_KEY",
        "apiKeyRequired": true,
        "includeUsage": true
      },
      "models": {
        "YOUR_MODEL_ID": {"name": "My coding model"}
      }
    }
  },
  "model": {
    "main": "eastx/YOUR_MODEL_ID",
    "lite": "eastx/YOUR_MODEL_ID"
  }
}
```

### Separate primary and lightweight work

First make main and lite work with one available model. Then compare code quality, completion time and whole-task cost before splitting roles. Complex edits need reliable tools and accuracy; simpler summaries can prioritize cost. A dedicated ZCode key and cap keep experiments separate from other clients.

### Common issues

For **404**, check `/v1` and model ID. For **403**, check model permissions and source IP. For **402**, inspect both balance and key cap. Thinking-level configurations may make ZCode use `/v1/messages`. EastX documents protocol translation for this endpoint: the `thinking` parameter is not directly forwarded and reasoning is decided upstream. A UI switch does not establish identical behavior across models.

EastX centralizes integration and spending management while model selection stays task-driven. Use the [error guide](https://eastx.ai/zh/community/api-errors-429-402-5xx) when a request fails.

### 资料与更新 / Sources and updates

更新 / Updated: 2026-11-14

- [EastX API 文档 / API documentation](https://eastx.ai/en/docs)

### 继续阅读 / Related guides

- [EastX API 报错排查：429、402、403 与 5xx | API Error Troubleshooting](https://eastx.ai/zh/community/api-errors-429-402-5xx)
- [SSE 流式输出怎么接：首 Token、结束信号与中断处理 | Streaming Guide](https://eastx.ai/zh/community/sse-streaming-interruption)
