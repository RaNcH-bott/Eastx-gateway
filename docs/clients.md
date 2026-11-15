# EastX 客户端接入 / EastX client setup

## 中文

为每个项目或客户端创建独立 Key，从 [API 文档](https://eastx.ai/en/docs) 核对模型 ID 与接口能力。客户端要求 Base URL 时使用 `https://api.eastx.ai/v1`。按官方教程处理需要完整端点的设置。先做一次短文本调用，再为代理任务验证工具调用、流式行为和多轮上下文。

| 客户端 | 接入重点 |
|---|---|
| [WorkBuddy](https://eastx.ai/zh/community/workbuddy-eastx-custom-model) | 添加自定义模型。核对协议选项、完整端点和会话实际选中的模型。 |
| [Cherry Studio](https://eastx.ai/zh/community/cherry-studio-eastx-setup) | 添加 OpenAI 兼容服务商，核对 API 主机和准确模型 ID。 |
| [Cline](https://eastx.ai/zh/community/cline-eastx-openai-compatible) | 选 OpenAI Compatible。在小型编码任务里验证工具调用并检查用量。 |
| [Open WebUI](https://eastx.ai/zh/community/open-webui-eastx-setup) | 由管理员添加 OpenAI 兼容连接，检查服务器出站和模型命名。 |
| [ZCode](https://eastx.ai/zh/community/zcode-eastx-setup) | 添加 Chat Completions 提供商。CLI 按教程配置 main 和 lite。 |

## English

Create a dedicated key for each client or project. Use the [API docs](https://eastx.ai/en/docs) to check model IDs and endpoint capabilities. Set `https://api.eastx.ai/v1` when a client asks for a base URL. Follow the linked guide when the client asks for a full endpoint. Start with one text request, then test tool calls, streaming, and multi-turn context for agent workloads.

| Client | What to check |
|---|---|
| [WorkBuddy](https://eastx.ai/zh/community/workbuddy-eastx-custom-model) | Add a custom model and check protocol, endpoint, and the model selected in the conversation. |
| [Cherry Studio](https://eastx.ai/zh/community/cherry-studio-eastx-setup) | Add an OpenAI-compatible provider and verify its host and exact model ID. |
| [Cline](https://eastx.ai/zh/community/cline-eastx-openai-compatible) | Select OpenAI Compatible. Verify tool calls on a small coding task and check usage. |
| [Open WebUI](https://eastx.ai/zh/community/open-webui-eastx-setup) | Add an OpenAI-compatible connection as an admin. Check server egress and model naming. |
| [ZCode](https://eastx.ai/zh/community/zcode-eastx-setup) | Add a Chat Completions provider. Follow the guide for CLI main and lite settings. |
